# Import necessary libraries
import cv2
import numpy as np
import os
import urllib.request

# Function to apply Gaussian blur to an image
def apply_blur(img, k):
    blurred_img = cv2.blur(img, (k, k), 0)
    return blurred_img

# Function to pixelate a specific region in an image
def pixelate_region(image, startX, startY, endX, endY):
    roi = image[startY:endY, startX:endX]
    blurred_roi = apply_blur(roi, 25)
    image[startY:endY, startX:endX] = blurred_roi
    return image

# Function to pixelate the face in an image
def pixelate_face(image, blocks=10):
    h, w = image.shape[:2]
    for i in range(blocks):
        for j in range(blocks):
            dx = int(w//blocks)
            dy = int(h//blocks)
            startX = int(j * dx)
            startY = int(i * dy)
            image = pixelate_region(image, startX, startY, startX+dx, startY+dy)
    return image

# Function to download the Haarcascade file if not exists
def download_haarcascade_file():
    url = 'https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml'
    filename = 'haarcascade_frontalface_default.xml'
    
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"{filename} downloaded successfully.")

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    # Download Haarcascade file if not exists
    download_haarcascade_file()
  

    # Load the Haarcascade classifier for face detection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Capture video stream and apply pixelation to detected faces
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret: break
        if cv2.waitKey(30) >= 0: break

        # Convert image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, 2)

        # Blur the detected faces
        for (x, y, w, h) in faces:
            roi = frame[y:y+h, x:x+w]
            roi = pixelate_face(roi, 8)
            frame[y:y+h, x:x+w] = roi

        # Display the resulting frame
        cv2.imshow('Face Pixelizer', frame)
    # Release the camera and close all windows
    cap.release()
   