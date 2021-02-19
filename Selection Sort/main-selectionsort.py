from PIL import Image, ImageDraw,ImageFont,ImageEnhance
import numpy
import time,os
import threading

numberOfWorkers = 8

class Main:
    def __init__(self):
        self.__sequence = [1,1,2,2,3,4,4,5,5,6,6,7,8,8,9,9]
        self.swapCount = 0
        self.comparisonCount = 0
        self.currentSortingAlgorithm = "Selection Sort"
        


    def getShuffledArray(self):
        a = numpy.array([])
        for i in range(120):
            for j in self.__sequence:
                a = numpy.append(a, j+i*9)
        numpy.random.shuffle(a)
        return list(a)

    def createImage(self, array, swapCount, comparisonCount):
        im = Image.new("RGB", (1920, 1080), "black")
        pixels = im.load()
        for index, value in enumerate(array):
            for i in range(int(value)):
                pixels[index, 1079-i]= (255, 255, 255)
                
        font = ImageFont.truetype("arial",size=25)

        text = f"{self.currentSortingAlgorithm} | Comparisons: {comparisonCount} | Swaps: {swapCount}"
        textSize = font.getsize(text)
        button_size = (textSize[0]+20, textSize[1]+20)
        Box = Image.new("RGB", button_size, "blue")
        boxDraw = ImageDraw.Draw(Box)
        
        boxDraw.text((10,10),text,font=font)
        im.paste(Box, (0, 0))
        im.save(f"{os.getcwd()}/frames/frame-{swapCount}.png")
        print(f"Created image [{swapCount}]")


    def selectionSortMain(self, array):
        length = len(array)
        
        for i in range(length):
            minimumElement = i
            for j in range(i+1, length):
                self.comparisonCount += 1
                if array[minimumElement] > array[j]:
                    minimumElement = j

            self.swap(array, i, minimumElement)
                    


    def swap(self, array, index1, index2):
        array[index1], array[index2] = array[index2], array[index1]
        self.swapCount += 1
        
        thread = threading.Thread(target=self.createImage, args=(list(array), self.swapCount, self.comparisonCount))
        thread.start()

        while threading.active_count() > numberOfWorkers: 
            time.sleep(0.01)
      
        
        return array


    def __call__(self):
        
        myArray = self.getShuffledArray()
        self.createImage(myArray,self.swapCount, self.comparisonCount)
        startTime = time.time()
        self.selectionSortMain(myArray)
        
        print("time: ", time.time()- startTime)
        self.createImage(myArray,self.swapCount, self.comparisonCount)



if __name__ == "__main__":
    program = Main()

    program()
