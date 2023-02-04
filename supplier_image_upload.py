#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://34.67.60.7/upload/"
img_dir= "/home/student-00-e17d884887f9/supplier-data/images/"
files = os.listdir(img_dir)
img_files = [img_dir + f for f in files if f.endswith(".jpeg")]
print(img_files)
for file in img_files:
    with open(file, 'rb') as opened:
        r  = requests.post(url, files={"file": opened })
        print(r.ok)
        print(r.status_code)

