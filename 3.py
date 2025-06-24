# Step 1: Import Required Libraries
import cv2  # OpenCV for image processing
import numpy as np  # Array operations
import string
import os
import matplotlib.pyplot as plt

# Step 2: ASCII Conversion Dictionary
d = {chr(i): i for i in range(255)}       # character to ASCII
c = {i: chr(i) for i in range(255)}       # ASCII to character

# Load the image
image_path = r"C:\Users\LENOVO\Documents\Cyber security\fruite.jpg"
img = cv2.imread(image_path)

xrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(xrgb)
plt.axis('off')
plt.show()
x.shape
(1500,1000,3)
key="123"
text="secret"
key
'123'

