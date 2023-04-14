import cv2
import streamlit as st

def detectAndDisplay(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)

    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)   
    FRAME_WINDOW.image(frame)

st.title("Webcam Live Feed")
FRAME_WINDOW = st.image([])
face_cascade = cv2.CascadeClassifier()
face_cascade.load('haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        detectAndDisplay(frame)
    else:
        break
cap.release()
