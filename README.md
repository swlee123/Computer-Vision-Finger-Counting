# Computer-Vision-Finger-Counting 8/3/2023

In this program we use python OpenCv library to help us to count the number of fingers using Computer Vision


## Prerequisite
- device need to have plugged-in / built-in camera that is accesible
- make sure you have a blank white / other blank color background to maximise the usage of the the program

## Overview

### Greyscale
  > We can make the image greyscale to reduce usage of computing power.
    More data to process will take time. Since the colour of the video has no effect on our project we convert to greyscale to ease the workload.

### Bluring
 > Bluring is the process of using `cv2.GaussianBlur(grey,(35,35),0)` to make our image blur.The intuition behind it is explained in this link:
   https://setosa.io/ev/image-kernels/
 
### Contour 
  >We use `cv2.findContours()` to find the max contour and draw it on the screen.
  Contour is an outline representing or bounding the shape or form of something ,joining points with similar colors
  `cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)`.
  `cv2.RETR_EXTERNAL` returns the biggest contour ,but we use  `cv2. RETR_TREE` that 
  finds all the promising contour lines and reconstructs a full hierarchy of nested contours.

### Convexhull
 >Hull means the exterior or the shape of the object.
 Therefore, the Convex Hull of a shape or a group of points is a tight fitting convex boundary around the points or the shape.
 We draw convexhull using `cv2.convexHull(cnt)` function. We also record the convexdefectivity using `defects = cv2.convexityDefects(cnt,hull)` 
 ![image](https://user-images.githubusercontent.com/85050265/223634417-10f82aa3-7a09-48dc-a1d3-2a8801dae99d.png)
 

### Defects ( Number of gap between fingers)
  >Deviation of contour from convex hull , or we can explain as the gap between contour and convex hull, basically we are counting them.
  `hull = cv2.convexHull(cnt,returnPoints=False)` 
  false return index of convexhull indx
  true return actual coordinate
  `defects = cv2.convexityDefects(cnt,hull)`
  ![image](https://user-images.githubusercontent.com/85050265/223634862-b5258b6d-9f8f-463d-a1b8-e3534b8f2c03.png)
  More about convexity defect :https://theailearner.com/2020/11/09/convexity-defects-opencv/
  Defects is a (x,y,4) numpy array, we use 3 points in each and calculate the distance between them as a,b,c.

### Calculation of angle using convextiy defect
  >After that, we use Pythagorean theorem and ![cosine rule](https://www.mathsisfun.com/algebra/trig-cosine-law.html) to calculate the angle between b and c , if the     angle <= 90 , number of     fingers +1 , as we know that the angle between fingers won't be >90 (assume you don't have disorder on your hand).
  
  >The angle between fingers is acute.Hence we only consider acute angles as fingers.
  The convexdefect actually is the number of gap betweeen fingers , so at the end we need to increment the nunber of finger by 1 to get the actual number of finger. 

