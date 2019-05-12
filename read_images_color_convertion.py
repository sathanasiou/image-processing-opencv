import cv2
import numpy as np 
import os
from glob import glob
import matplotlib.pyplot as plt 

# Function to read multiple images from one folder and convert them into another
# color palette. In the end we display the images

# Inputs: 1) image_directory: where to read the files from 
#         2) convertion_tupe: color palette to convert images to, Default = RGB
# Output : Display the converted images 

# More to be done: 1) Read and display images in the row
#                  2) Save image information into numpy arrays for further modifications

def read_multiple_images_and_convert(image_directory, convertion_type=None):
    img_names = glob(image_directory)
    i = 0 
  
    for frame in img_names:
        print('processing %s...' % frame)
        image_original = cv2.imread(frame)
        
        if convertion_type == None:
            image = image_original
            print('None')
            print(convertion_type)
        elif convertion_type == 'GRAY':
            image = cv2.cvtColor(image_original,cv2.COLOR_RGB2GRAY)
        elif convertion_type == 'HSV':
            image = cv2.cvtColor(image_original,cv2.COLOR_RGB2HSV)
        
        if image is not None:
            cv2.imshow("Image No:", image)
        elif image is None:
            print ("Error loading: " + img_names)
            #end this loop iteration and move on to next image
            continue
            
        key = cv2.waitKey(0)
        if key == 27: # escape
            break
            
        
        print(i)
    cv2.destroyAllWindows()

# How to run examples

# In order to see all pictures you should push enter
# If you want to exit earlier use ESC

image_dir = 'new_folder/*.*' 
convertion_type = 'HSV'

read_multiple_images_and_convert(image_dir,convertion_type)
# read_multiple_images_and_convert(image_dir)