#!/usr/bin/env python3

import os
from PIL import Image
#creating a list of files
dest_folder = "/home/student-00-e17d884887f9/supplier-data/images/"
fileees = os.listdir(dest_folder)

#iterating through files in folder and checking their format
for file in fileees:
   old_name = os.path.join(dest_folder, file)
   new_name = old_name.replace('.tiff', '.jpeg')
   os.rename(old_name, new_name)

#resizing, rotating and saving the photos in a JPEG format
for pic in fileees:
   if pic.startswith("0"):
     img = Image.open(os.path.join(dest_folder, pic))
     new_img = img.convert("RGB").resize((600,400)).save(os.path.join(dest_folder, pic), 'JPEG')
     print(new_img.size, new_img.mode, new_img.format)



#########working, optimal code(not mine)#########

#!/usr/bin/env python3

from PIL import Image
from os import listdir
from os.path import isfile, join

for item in listdir("./supplier-data/images"):
 if ".tiff" in item:
  im = Image.open(join("./supplier-data/images",item))
  new_im = im.convert("RGB").resize((600,400))
  new_im.save(join("./supplier-data/images/",item.replace(".tiff","")) + ".jpeg")