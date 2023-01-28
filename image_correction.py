#!/usr/bin/env python3

import os
from PIL import Image
import shutil
#creating a list of files

folder = r"/home/dheenaleo2211/images/"
files = os.listdir(folder)
print(files)

#creating a path for the new folder (/opt/icons/)
path = f"{os.getenv('HOME')}/opt/icons/"

os.makedirs(path)
dest_folder = r"/home/dheenaleo2211/opt/icons/"

#iterating through each file in the files and moving them to new folder
for filename in files:
   source = folder + filename
   print(source)
   destination = dest_folder + filename
   print(destination)
   if os.path.isfile(source):
       shutil.move(source, destination)
       print('Moved:', filename)

#iterating through files in new folder and checking their format
print("===Printing from new directory==")
fileees = os.listdir(dest_folder)
for file in fileees:
   old_name = os.path.join(dest_folder, file)
   new_name = old_name.replace('48dp', '48dp.jpeg')
   os.rename(old_name, new_name)
print(os.listdir(dest_folder))

#resizing, rotating and saving the photos in a JPEG format
for pic in [f for f in os.listdir(dest_folder) if f.startswith("ic_")]:
   img = Image.open(os.path.join(dest_folder,pic))
   if img.mode != 'RGB' and img.format != 'JPEG':
    img = img.rotate(-90).resize((128,128)).convert('RGB').save(os.path.join(dest_folder, pic), 'jpeg')
    print(img.size, img.mode, img.format)