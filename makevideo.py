import cv2
import numpy
import glob
import os


images = []
path = os.getcwd()+"\\frames\\"

myVideo = cv2.VideoWriter("quicksort-1.mkv", cv2.VideoWriter_fourcc(*"DIVX"), 60, (1920,1080))

for filename in range(len(os.listdir(path))):
    filename = f"frame-{filename}.png"

    img = cv2.imread(f"{path}{filename}")
    height, width, layers = img.shape
    myVideo.write(img)

   
myVideo.release()
