import cv2
import imutils
import math
import numpy as np


image = cv2.imread('IMG_20200529_182340.jpg')
final = image.copy()
print(image.shape)



gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow('thresh', thresh)

cv2.imwrite('thresh.jpg', thresh)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
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


print(point[1], point[0])
print(point[3], point[2])
width = calcDistance(point[1][0], point[1][1], point[0][0], point[0][1])
print(math.floor(width))
height = calcDistance(point[2][0], point[2][1], point[1][0], point[1][1])
print(math.floor(height))


cv2.rectangle(final,point[3],point[1],(0,0,0), -1)
cv2.imshow("rectangle", final)
cv2.imwrite('bg.jpg', final)
cv2.waitKey()

# contours = np.array([ point[0], point[1], point[2], point[3] ])
# cv2.fillPoly(final, pts =[contours], color=(0,0,0))
# cv2.imshow(" ", final)
# cv2.imwrite('bg.jpg', final)
# cv2.waitKey()