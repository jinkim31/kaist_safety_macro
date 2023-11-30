import os
import cv2
import time
import pyautogui

def main():
    while True:
        os.system('screencapture screen.png')
        img_screen = cv2.imread('screen.png')
        center_pos = int(img_screen.shape[0] / 2), int(img_screen.shape[1] / 2)
        center_pixel = img_screen[center_pos[0], center_pos[1]]
        if center_pixel[0] == 255 and center_pixel[1] == 255 and center_pixel[2] == 255:
            print('click', center_pos)
            pyautogui.moveTo(center_pos[1]/2, center_pos[0]/2)
            pyautogui.click()
        time.sleep(1)


if __name__ == '__main__':
    main()
