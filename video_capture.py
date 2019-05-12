import cv2
import numpy as np 
import os
from glob import glob
import matplotlib.pyplot as plt 

# Function to exract specific number of video 
# capture frames into the wanted folder 
############## Variables ################
# video_cap : the video to read
# num_of_frames: How many frames you want to extract from the beginning of video. If you do not set
# a value the default would be to read the whole video
# image_folder : What is the image destination folder, if the folder does not exist, it creates it.
# It returns the number of frames produced for probably future use

def extract_frames(video_cap,image_folder,num_of_frames=None):
    currentFrame = 0 
    flag = False
    
    result = os.path.isdir(image_folder)
    
    if result is False: 
        print('Folder does not exist, creating folder with name:',image_folder)
        os.makedirs(image_folder)
    
    if num_of_frames is None: 
        flag = True
    
    while(True):
        ret,frame = video_cap.read()

        
        if not ret: 
            print('out')
            break
        if (flag is not True) and (currentFrame > num_of_frames-1):
            print('sin8iki')
            break

        name = image_folder + "frame" + str(currentFrame) + '.jpg'
    #    print('Creating...' + name)
        cv2.imwrite(name, frame)

        currentFrame += 1 

    video_cap.release()
    cv2.destroyAllWindows
    
    return currentFrame

# Example of running the function

# read the video capture
cap = cv2.VideoCapture('video.mpg')
#specify the name of the destination folder
destination_folder = "new_folder/"
#specify the number of frames 
num_of_frames = None


Num_of_frames = extract_frames(cap,destination_folder,num_of_frames)