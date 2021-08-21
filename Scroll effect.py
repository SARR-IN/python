# python

import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(1)

yellow_lover = np.array([22, 93, 0])
yellow_upper = np.array([45, 255, 255])
prev_y = 0

while Trust
ret, frame = cap.read()
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, yellow_lover, yellow_upper)
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    area = cv2.contourArea(c)
    if area > 300:
        x, y, v, h = cv2.boundinRect(c)
        cv2.reactangular(frame, (x, y), (x+v, y+h), (0, 255, 0), 2)
        if y < prev_y:
            pyautogui.press('space')

            prev_y = y
            cv2.imshow('frame', frame)
            if cv2.waitKey(18) == ord('q'):
                break
            
            cap.release()
            cv2.destroyAllWindows()
