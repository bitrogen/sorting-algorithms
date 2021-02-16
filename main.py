from PIL import Image, ImageDraw,ImageFont,ImageEnhance
import numpy
from random import randrange

import pprint
import time,os


class Main:
    def __init__(self):
        self.__sequence = [1,1,2,2,3,4,4,5,5,6,6,7,8,8,9,9]
        self.swapCount = 0
        self.comparisonCount = 0

        self.callDict = {
            "Quick Sort": self.quickSortMain
        }

    def getShuffledArray(self):
        a = numpy.array([])
        for i in range(120):
            for j in self.__sequence:
                a = numpy.append(a, j+i*9)
        numpy.random.shuffle(a)
        return a

    def createImage(self, array):
        im = Image.new("RGB", (1920, 1080), "black")
        pixels = im.load()
        for index, value in enumerate(array):
            for i in range(int(value)):
                pixels[index, 1079-i]= (255, 255, 255)
                
        font = ImageFont.truetype("arial",size=25)

        text = f"{self.currentSortingAlgorithm} | Comparisons: {self.comparisonCount} | Swaps: {self.swapCount}"
        textSize = font.getsize(text)
        button_size = (textSize[0]+20, textSize[1]+20)
        Box = Image.new("RGB", button_size, "blue")
        boxDraw = ImageDraw.Draw(Box)
        
        boxDraw.text((10,10),text,font=font)
        im.paste(Box, (0, 0))
        im.save(f"{os.getcwd()}/frames/frame-{self.swapCount}.png")
    def quickSortMain(self, array, low, high):
        if len(array) == 1:
            return array
        self.comparisonCount += 1
        if low < high:
            pi = self.quickSortPartition(array, low, high)

            self.quickSortMain(array, low, pi-1)
            self.quickSortMain(array, pi+1, high)

    def quickSortPartition(self, array, low, high):
        pivot = array[high]
        i = (low-1)
        
        for j in range(low, high):
            self.comparisonCount += 1
            if array[j] <= pivot:
                i += 1
                array = self.swap(array, i, j)

        array = self.swap(array, i+1, high)
        return i+1

    def swap(self, array, index1, index2):
        array[index1], array[index2] = array[index2], array[index1]
        self.swapCount += 1
        self.createImage(array)
        return array


    def __call__(self, sort):
        self.currentSortingAlgorithm = sort
        myArray = self.getShuffledArray()
        self.createImage(myArray)
        startTime = time.time()
        self.callDict[sort](myArray,0,len(myArray)-1)
        
        print("time: ", time.time()- startTime)
        self.createImage(myArray)


if __name__ == "__main__":
    program = Main()

    program("Quick Sort")
