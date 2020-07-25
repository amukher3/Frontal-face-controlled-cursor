# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 16:24:03 2020

@author: Abhishek Mukherjee
"""

import cv2
import pyautogui
face_cascade = cv2.CascadeClassifier('C:/Users/Abhishek Mukherjee/Downloads/haarcascade_frontalface_default.xml')

# For doing detection:
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        
        #For automated control
        pyautogui.moveTo(x+100, y+100, duration = 0.0000001)
        
        cv2.rectangle(frame, (x, y), (x+10, y+10), (255, 0, 0), 2)
    return frame

# For the webcam:
video_capture = cv2.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()