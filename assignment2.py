# -*- coding: utf-8 -*-
import sys
import os, os.path, hashlib

search_directory = sys.argv[1]

# dupe_dictionary: absolute_path -> file_size
# search_dictionary: file_size -> list of absolute_path
#dictionary_printing: hash -> list of duplicate files
dupe_dictionary, search_dictionary, hash_dictionary = dict(), dict(), dict()
dictionary_printing = {}

def get_hash(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def match_on_hash(dupe_file):
    for search_file in search_dictionary[file_size]:
        if search_file != dupe_file:
            if search_file not in hash_dictionary:
                hash_dictionary[search_file] = get_hash(search_file)
            if dupe_file not in hash_dictionary:
                hash_dictionary[dupe_file] = get_hash(dupe_file)
            search_hash = hash_dictionary[search_file]
            dupe_hash = hash_dictionary[dupe_file]
            if search_hash == dupe_hash:
                if search_hash not in dictionary_printing:
                    s = set()
                    s.add(search_file)
                    dictionary_printing [search_hash] = s
                else:
                    dictionary_printing [search_hash].add(search_file)          
    
for dirpath, dirnames, filenames in os.walk(search_directory):
    for filename in filenames:
        absolute_path = os.path.join(dirpath, filename)
        file_size =  os.path.getsize(absolute_path)
        dupe_dictionary[absolute_path] = file_size
        if file_size not in search_dictionary:
           search_dictionary[file_size] = [] 
        search_dictionary[file_size].append(absolute_path)
        
for dupe_file in dupe_dictionary:
    file_size = dupe_dictionary[dupe_file]
    if file_size in search_dictionary:
        match_on_hash(dupe_file)

print("The duplicates files are:\n")
for k in dictionary_printing.keys():
    print((dictionary_printing[k]))
    print()
            
     
               
        
        
        
        
        
   
        
