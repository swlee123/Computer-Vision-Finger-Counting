import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret,frame = cam.read()
    
    if not ret:
        print("Frame not read!")
        break
    
    # flip the cam vertical so wont look like mirror
    # 1 = vertical 0 = horizontal
    frame = cv2.flip(frame,1)
    
    # draw bounding rectangle
    cv2.rectangle(frame,(300,50),(600,350),(0,255,0),2)
    crop_img =frame[50:350,300:600]
    
    # convert to grey scale
    grey = cv2.cvtColor(crop_img,cv2.COLOR_BGR2GRAY)
    
    # blur the image to remove noise
    blur = cv2.GaussianBlur(grey,(35,35),0)
    
    # thresholding
    ret,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # contours
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt = max(contours,key =lambda x : cv2.contourArea(x))
    cv2.drawContours(crop_img,[cnt],0,(0,255,0),3)
    
    # convex hull
    hull = cv2.convexHull(cnt)
    # draw the hull
    cv2.drawContours(crop_img,[hull],0,(255,0,0),3)
    
    # convexity defect
    hull = cv2.convexHull(cnt,returnPoints=False) # false return index of convexhull indx
    # true return actual coordinate
    defects = cv2.convexityDefects(cnt,hull)
    
    num_fingers = 0
    if defects is not None :
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i][0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            
            a = np.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2)
            b= np.sqrt((far[0]-start[0])**2 + (far[1]-start[1])**2)
            c = np.sqrt((end[0]-far[0])**2 + (end[1]-far[1])**2)
            angle = np.arccos((b**2+c**2-a**2)/(2*b*c))
            
            if angle <= np.pi/2:
                num_fingers +=1
                cv2.circle(crop_img,far,4,[0,0,225],-1)
            # do calculation on three points and the angle between two fingers\
            # we use the assumtion that angle between 2 fingers wont be >90
            # so if angle <= 90 finger count ++
            # at the end +1 for num of finger as num of finger = num of gap +1 
            # got one more function to show number but not in slide
            # cv2.line(crop_img,start,end,4,[255,0,0],2)
        num_fingers = num_fingers+1
        print(f"Number of finger : {num_fingers}")
        
            
            
            
            
    # cv2.imshow('crop',crop_img) # show frame of cropped image
    cv2.imshow('frame',frame) # show entire rectangle 
    # cv2.imshow('grey',grey)
    cv2.imshow('vid',crop_img)
    
    
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()