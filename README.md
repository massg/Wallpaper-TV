# Wallpaper-TV

This project implements the virtual demonstration of a wallpaper TV using OpenCV. Literally, Wallpaper TV is the thinnest TV which can be peeled onto a wall and held in place with magnets. Thus, the user experiences in such a way that the tv is playing on the wall with a fixed dimension. Similarly, the project shows how a video is played on the wall, which is captured by the web camera, when the dimensions are given as marks or dots in the wall.
When the program is executed, the webcam starts capturing the wall,with dots at certain locations, and takes a snapshot of the camera feed. The image is smoothened, using Gaussian Blur, and thresholded which results in a binary image so that only the points are visible. The image is then contoured and their centre positions are identified which helps in getting the area in which the video can be played. Next, isolate the area of interest from the background, resize the video accordingly, and iterate through every frame so that the video can be played in the area.


