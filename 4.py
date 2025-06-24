# Import Required Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ASCII CONVERSION
d = {chr(i): i for i in range(255)}  # character to ASCII
c = {i: chr(i) for i in range(255)}  # ASCII to character

# Load the image
image_path = r"C:\Users\LENOVO\Documents\Cyber security\fruite.jpg"  # update with your actual path
img = cv2.imread(image_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.axis('off')
plt.show()
