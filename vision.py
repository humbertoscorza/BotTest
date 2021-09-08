import cv2 as cv
import numpy as np
from time import sleep
import pyautogui


class Vision:

    # properties
    needle_img = None
    needle_w = 0
    needle_h = 0
    method = None

    # constructor
    def __init__(self, needle_img_path, method=cv.TM_CCOEFF_NORMED):
        self.needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)
        # Save the dimensions of the needle image
        self.needle_w = self.needle_img.shape[1]
        self.needle_h = self.needle_img.shape[0]

        self.method = method

    def pressKey(self, index):
        if index == 0:
            sleep(0.5)
            pyautogui.press('w')
        elif index == 1:
            sleep(0.5)
            pyautogui.press('a')
        elif index == 2:
            sleep(0.5)
            pyautogui.press('s')
        elif index == 3:
            sleep(0.5)
            pyautogui.press('d')

    def findUnique(self, origin,  haystack_img, needle_img, threshold=0.5):
        # run the OpenCV algorithm
        for img in needle_img:
            result = self.fastMatch(haystack_img,img)

            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

            if max_val >= threshold:
     
                index = needle_img.index(img)
                print(int(index))

                self.pressKey(int(index))

                needle_w = img.shape[1]
                needle_h = img.shape[0]

                # Calculate the bottom right corner of the rectangle to draw
                top_left = max_loc
                bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

                # Draw a rectangle on our screenshot to highlight where we found the needle.
                # The line color can be set as an RGB tuple
                cv.rectangle(origin, top_left, bottom_right, 
                                color=(0, 255, 0), thickness=2)

    def fastMatch(self, haystack_img, needle_img):
        return cv.matchTemplate(haystack_img, needle_img, self.method)

    
    
          
