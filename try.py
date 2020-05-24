import cv2
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=False, default='output.mp4', help="output video file")
args = vars(ap.parse_args())
output = args['output']

vid = cv2.VideoCapture("video.mp4")
success=1
count = 0;
s, image= vid.read()
height , width , layers =  image.shape
new_h=200
new_w=200
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

for frame in images:

    # image_path = os.path.join(dir_path, image)
    # frame = cv2.imread(image_path)

    out.write(frame) # Write out frame to video

    cv2.imshow('video',frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
        break
		
out.release()
cv2.destroyAllWindows()


