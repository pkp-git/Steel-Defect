import cv2
import numpy as np
from random import randint
import os
from tkinter import Tk
from tkinter import filedialog

def get_folder_path():
    root = Tk()
    root.withdraw() 
    folder_path = filedialog.askdirectory(title="Select the folder with images for viewing")  #Opens file explorer
    return folder_path

print("Select the folder containing the image files:")
image_dir = get_folder_path()

image_files = sorted([f for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))])  #Specify if any other format

for image_file in (image_files):

    img_path = os.path.join(image_dir, image_file)
    img = cv2.imread(img_path)
    
    if img is None:
        print(f"Failed to read image {img_path}")
        continue

    img = cv2.resize(img, (480,480)) #resize image as needed
    cv2.imshow('Image with Polygons', img)
    cv2.waitKey(0)  #press any key to move to the next image

cv2.destroyAllWindows()
