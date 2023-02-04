#!/usr/bin/env python3

import os
import requests

#listing all the .txt files
source = "{}/supplier-data/descriptions/".format(os.getenv("HOME"))
file_names = os.listdir(source)


#read files into lines
def readlines(file):
   with open(source+file) as file:
      lines = file.read().splitlines()
   return lines

feedback =[]
keys = ['name', 'weight', 'description', 'image_name']
for file in file_names:
   lines = readlines(file)
   feedback.append(dict(zip(keys, lines)))

hosturl = "https://localhost/fruits"

for entry in feedback:

   response = requests.post(hosturl, data=entry)
   print(response.status_code)
   print(response.ok)   
