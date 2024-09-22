import tkinter as tk
from tkinter import filedialog
from ultralytics import YOLO
from ultralytics.utils.benchmarks import benchmark

def openFile():
    global sourcevar
    sourcevar = filedialog.askdirectory(initialdir="D:/Steel_Defect/Extras/exp", title="Select File")
    root.destroy()

def camera_click():
    global sourcevar
    sourcevar = 0
    root.destroy()

root = tk.Tk()
root.title("Simple Tkinter Window")
root.geometry("400x300")

camera_button = tk.Button(root, text="Use Camera", command=camera_click, height=10, width=20)
image_button = tk.Button(root, text="Upload Image", command=openFile, height=10, width=20)
title_label = tk.Label(root, text="STEEL DEFECT DETECTION\n(yolov8n)", font=("Arial", 20))

title_label.pack(pady=20)
camera_button.pack(side=tk.LEFT, padx=20)
image_button.pack(side=tk.RIGHT, padx=20)

root.mainloop()


model = YOLO("../Defect_40.pt")

model.predict(source=sourcevar, show=True, save=True, conf=0.12, save_txt=True, imgsz=512)

root = tk.Tk()
root.title("Simple Tkinter Window")
root.geometry("400x300")

title_label = tk.Label(root, text="Images Have Been Marked With Defects And Saved to ../runs/segment/predict(n) Folder. ", font=("Arial", 18), justify="center", wraplength=400)
title_label2 = tk.Label(root, text="Note: Please delete or relocate the predict folder after viewing to avoid creating multiple instances of predict", font=("Arial", 14), justify="center", wraplength=400)

title_label.pack(pady=20)
title_label2.pack(pady=20)

root.mainloop()
