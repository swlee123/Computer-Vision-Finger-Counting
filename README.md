# Computer-Vision-Finger-Counting 8/3/2023

In this program we use python OpenCv library to help us to count the number of fingers using Computer Vision


## Prerequisite
- device need to have plugged-in / built-in camera that is accesible
- make sure you have a blank white / other blank color background to maximise the usage of the the program

## Overview

Greyscale
First, we make the image greyscale to reduce usage of computing power

Secondly,we use cv2.findContours() to find the max contour and draw it on the screen 

Next,we draw convexhull using cv2.convexHull(cnt) function. We also record the convexdefectivity using `defects = cv2.convexityDefects(cnt,hull)` 

Defects is a (x,y,4) numpy array, we use 3 points in each and calculate the distance between them as a,b,c.

After that, we use cosine rule to calculate the angle between b and c , if the angle <= 90 , number of fingers +1 , as we know that the angle between fingers won't be >90.

The convexdefect actually is the number of gap betweeen fingers , so at the end we need to increment the nunber of finger by 1 to get the actual number of finger. 

