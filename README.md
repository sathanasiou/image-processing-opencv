# image-processing-opencv
This github repository is giving some functions that I created regarding image processing and video processing 
with main purpose to use them for my thesis. 

I am using Python for development and OpenCV as main library for image processing.



 ### def read_multiple_images_and_convert(image_directory, convertion_type=None) :  
 
  Function to read multiple images from one folder and convert them into another  
  color palette. In the end we display the images  

  -- Inputs:   
1) image_directory: where to read the files from  
2) convertion_tupe: color palette to convert images to, Default = RGB  
  
  -- Output : 
Display the converted images   

-- More to be done: 
1) Read and display images in the row  
2) Save image information into numpy arrays for further modifications  

### def extract_frames(video_cap,image_folder,num_of_frames=None):
Function to exract specific number of video capture frames into the wanted folder.  

  -- Inputs: 
1) video_cap : the video to read  
2) num_of_frames: How many frames you want to extract from the beginning of video. The default would be to read the whole video  
3) image_folder : What is the image destination folder, if the folder does not exist, it creates it.    

-- Output:  
It returns the number of frames produced for probably future use.  

-- More to be done:   
We can see multiple images of the same frame. Image is changing every 5 frames. See if it is an expected or not behavior.
