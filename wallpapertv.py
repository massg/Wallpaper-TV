import numpy as np
import cv2
import time

# 1. Capture live camera
img = cv2.imread("dot.jpg")  # snapshot


# 2. Find the four points

# 2.1 Convert to grey-scale
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Grey",img_g)
# cv2.waitKey(100)

# 2.2 thresholding
ret1,th1 = cv2.threshold(img_g,127,255,cv2.THRESH_BINARY_INV) # black--255 and white--0
cv2.imshow("Threshold",th1)
cv2.waitKey(0)

#2.3 get the points

mask = np.zeros(img_g.shape,np.uint8)
pixelpoints = cv2.findNonZero(mask)
print(pixelpoints)
cv2.destroyAllWindows()


# 3. Play the vedio
