import cv2 as cv
import numpy as np
import os
import time
from windowcapture import WindowCapture
from vision import Vision

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture()
vision_symbol = []
names =[ 'w_gray.jpg','a_gray.jpg','s_gray.jpg','d_gray.jpg']
# initialize the Vision class

for name in names:
    vision = Vision(name)
    temp = vision.needle_img
    vision_symbol.append(temp)


wincap = WindowCapture()

loop_time = time.time()
while(True):

    # get an updated image of the game
    screenshot = wincap.screenme()

    result = vision.findUnique(screenshot[0] ,screenshot[1], vision_symbol, 0.5)

    # debug the loop rate
    print('FPS {}'.format(1 / (time.time() - loop_time)))
    loop_time = time.time()

    cv.imshow("Image", screenshot[0])

    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
