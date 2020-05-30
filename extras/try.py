import cv2
import os
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=False, default='output.mov', help="output video file")
args = vars(ap.parse_args())
output = args['output']

vid = cv2.VideoCapture("video.mp4")
success=1
count = 0;
s, image= vid.read()
height , width , layers =  image.shape
print(height, width)

t = cv2.imread('bg.jpg')
th, tw, z= t.shape
print(tw, th)
# image = cv2.resize(image, (int(tw), int(th)))
# image = image+t;
# cv2.imshow('check',image)
# cv2.waitKey()


new_h=459 # give the height and width from the contour points from the other file
new_w=777
print("I am in success")    
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

# for a in os.listdir('.'):
#     if a.endswith('jpg'):
#         images.append(a)

# image_path = os.path.join('.', images[0])
# frame = cv2.imread(image_path)
# cv2.imshow('video',frame)
# height, width, channels = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
out = cv2.VideoWriter(output, fourcc, 10.0, (width, height))
dir_path = '.'

#adding padding to the image
ww = 1280
hh = 720
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

    # image_path = os.path.join(dir_path, image)
    # frame = cv2.imread(image_path)
    # frame = cv2.resize(frame, (int(th), int(tw)))
    # frame = frame+t;
    frame = paddFrame(frame)
    # cv2.imshow(' ', frame+t)
    # break;
    frame = frame +t
    
    out.write(frame) 

    cv2.imshow('video',frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
		
cv2.waitKey()
out.release()




cv2.destroyAllWindows()


