import cv2
import imutils
import math
import numpy as np
import os
import argparse

# 1. Capture live camera and take a snapshot
image = cv2.imread("dot.jpg")  # snapshot
final = image.copy()
#2. Convert the image into greyscale, smooth it and threshold it to get the dots
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow('thresh', thresh)
cv2.waitKey()
cv2.imwrite('thresh.jpg', thresh)

#3. Get the dot locations using contours
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

#4. For a proper position, we take the center of the contour regions as our 4 pixel locations
point = []
i=0;
for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	i+=1
	point.append((cX,cY))
	print("center",i ,cX,cY)

	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
	cv2.putText(image, "center", (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	# show the image
	cv2.imshow("Image", image)
	cv2.waitKey(0)

for index in range(i):
	print(point[index])

def calcDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  

#calculate the dimensions of the of the area enclosed by the dots
width = calcDistance(point[1][0], point[1][1], point[0][0], point[0][1])
print(math.floor(width))
height = calcDistance(point[2][0], point[2][1], point[1][0], point[1][1])
print(math.floor(height))

new_w = math.floor(width)
new_h = math.floor(height)

#Create a mask so we can play the video, in the enclosed region
#This is done using two ways, one with rectangle, or other my fiilling the polygon area

# cv2.rectangle(final,point[3],point[1],(0,0,0), -1)
# cv2.imshow("rectangle", final)
# cv2.imwrite('bg.jpg', final)
# cv2.waitKey()

contours = np.array([ point[0], point[1], point[2], point[3] ])
cv2.fillPoly(final, pts =[contours], color=(0,0,0))
cv2.imshow(" ", final)
cv2.imwrite('bg.jpg', final)
cv2.waitKey()

#resize the video based on the dimensions we calculated earlier

vid = cv2.VideoCapture("video.mp4")
success=1
count = 0;
s, videoFrame= vid.read()
height , width , layers =  videoFrame.shape
print(height, width)

#resize each frame

images = []    
while (vid.isOpened()):
 
    ret, frame = vid.read()
    if ret == True:
        resize = cv2.resize(frame, (int(new_w), int(new_h))) 
        images.append(resize)
        count += 1
    else:
        break

print(count)

fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
out = cv2.VideoWriter('output.mp4', fourcc, 10.0, (width, height))
dir_path = '.'


ww = image.shape[1]
hh = image.shape[0]
color = (0,0,0)

def paddFrame(frame):
    diff_vert = 720 - new_h
    pad_top = diff_vert//2
    pad_bottom = diff_vert - pad_top
    diff_hori = 1280 - new_w
    pad_left = diff_hori//2
    pad_right = diff_hori - pad_left
    img_padded = cv2.copyMakeBorder(frame, 10, 0, 25, 0, cv2.BORDER_REPLICATE, value=0)
    img_padded = cv2.copyMakeBorder(img_padded, pad_top-10, pad_bottom, pad_left-25, pad_right, cv2.BORDER_CONSTANT, value=0)
    return img_padded



for frame in images:

    frame = paddFrame(frame)
    # cv2.imshow(' ', frame+t)
    # break;
    frame = frame +final
    
    out.write(frame) 

    cv2.imshow('video',frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
		
cv2.waitKey()
out.release()
