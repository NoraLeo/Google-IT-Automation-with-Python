#!/usr/bin/env python3
import requests
import os


url = "http://localhost/upload/"
img_dir= "{}/supplier-data/images/".format(get.env("HOME"))
files = os.listdir(img_dir)
img_files = [img_dir + f for f in files if f.endswith(".jpeg")]
print(img_files)
for file in img_files:
    with open(file, 'rb') as opened:
        r  = requests.post(url, files={"file": opened })
        print(r.ok)
        print(r.status_code)

