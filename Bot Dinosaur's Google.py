from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

def printmsg():
    print(" http://www.trex-game.skipser.com/ ")

class Cordinates():
    replayBtn = (340,390)
    dinosaur = (171,440)#437 42

def restartGame():
    pyautogui.click(Cordinates.replayBtn)
    pyautogui.keyDown('down')

def pressSapce():
    pyautogui .keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    time.sleep(0.18)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrab():
    box = (Cordinates.dinosaur[0]+60,Cordinates.dinosaur[1],
           Cordinates.dinosaur[0]+697,Cordinates.dinosaur[1]+5)
    
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum( )) 
    return a.sum()

def main():
    restartGame()
    while True:
        if(imageGrab()!=697):
            pressSapce()
            time.sleep(0.1)


printmsg()
main()
restartGame()
time.sleep(1)
pressSapce()
