# -*- coding: utf-8 -*-
"""
@title: draw_your_name.py
@author: Yiğit GÜMÜŞ
@date: 2024-10-04 23:08:23

@description: Run the script and change window to MS Paint.
And see the magic.
"""


import pyautogui as pg

import subprocess
import threading
import time

def openPaint():
    _openPaint = lambda: subprocess.run(['mspaint'])
    t_OpenPaint = threading.Thread(target=_openPaint)
    t_OpenPaint.start()

pg.FAILSAFE = True
pg.PAUSE = 0.5

screenwidth, screenheight = pg.size()
p,q = int(0.11*screenwidth),int(0.26*screenheight)
print('Letter Width:',p)                            #p = Letter Width
print('Letter Height:',q)                           #q = Letter Height

def drawA(a,b):
    pg.click(a+(p//2),b)
    pg.dragTo(a,b+q,duration = 0.15)
    pg.click(a+(p//2),b)
    pg.dragTo(a+p,b+q,duration = 0.15)
    pg.click(a+(p//4),b+(q//2))
    pg.dragTo(a+((3*p)//4),b+(q//2),duration = 0.15)

def drawB(a,b):
    pg.click(a,b)
    pg.dragTo(a,b+q,duration = 0.15)
    pg.dragTo(a+(4*p)//5,b+q,duration = 0.15)
    pg.dragTo(a+p,b+(9*q)//10,duration = 0.1)
    pg.dragTo(a+p,b+(q//2 + ((9*q)//100)),duration = 0.1)
    pg.dragTo(a+(p//4),b+(q//2),duration = 0.1)
    pg.dragTo(a+p,b+(q//2 - ((9*q)//100)),duration = 0.1)
    pg.dragTo(a+p,b+q//10,duration = 0.1)
    pg.dragTo(a+(4*p)//5,b,duration = 0.1)
    pg.dragTo(a,b,duration = 0.15)

def drawC(a,b):
    pg.click(a+p,b+q//6)
    pg.dragTo(a+(4*p)//5,b,duration = 0.1)
    pg.dragTo(a+p//5,b,duration = 0.15)
    pg.dragTo(a,b+q//6,duration = 0.1)
    pg.dragTo(a,b+(5*q)//6,duration = 0.15)
    pg.dragTo(a+p//5,b+q,duration = 0.1)
    pg.dragTo(a+(4*p)//5,b+q,duration = 0.15)
    pg.dragTo(a+p,b+(5*q)//6,duration = 0.1)

def drawD(a,b):
    pg.click(a,b)
    pg.dragTo(a,b+q,duration = 0.15)
    pg.dragTo(a + (4*p)//5,b+q,duration = 0.15)
    pg.dragTo(a+p,b+(q - ((17*q)//100)),duration = 0.15)
    pg.dragTo(a+p,b+((17*q)//100),duration = 0.15)
    pg.dragTo(a + (4*p)//5,b,duration = 0.15)
    pg.dragTo(a,b,duration = 0.15)

def drawE(a,b):
    pg.click(a,b+q)
    pg.dragTo(a,b,duration = 0.15)
    pg.dragTo(a+p,b,duration = 0.15)
    pg.click(a,b+q//2)
    pg.dragTo(a+p//2,b+q//2,duration = 0.15)
    pg.click(a,b+q)
    pg.dragTo(a+p,b+q,duration = 0.15)

def drawF(a,b):
    pg.click(a,b+q)
    pg.dragTo(a,b,duration = 0.15)
    pg.dragTo(a+p,b,duration = 0.15)
    pg.click(a,b+q//2)
    pg.dragTo(a+p//2,b+q//2,duration = 0.15)

def drawG(a,b):
    pg.click(a+p,b+q//6)
    pg.dragTo(a+(4*p)//5,b,duration = 0.1)
    pg.dragTo(a+p//5,b,duration = 0.15)
    pg.dragTo(a,b+q//6,duration = 0.1)
    pg.dragTo(a,b+(5*q)//6,duration = 0.15)
    pg.dragTo(a+p//5,b+q,duration = 0.1)
    pg.dragTo(a+(4*p)//5,b+q,duration = 0.15)
    pg.dragTo(a+p,b+(5*q)//6,duration = 0.1)
    pg.dragTo(a+p,b+q//2,duration = 0.1)
    pg.dragTo(a+p//2,b+q//2,duration = 0.1)

def drawH(a,b):
    pg.click(a,b)
    pg.dragTo(a,b+(q//2),duration = 0.15)
    pg.dragTo(a+p,b+(q//2),duration = 0.15)
    pg.dragTo(a+p,b,duration = 0.15)
    pg.click(a,b+q)
    pg.dragTo(a,b+(q//2),duration = 0.15)
    pg.click(a+p,b+q)
    pg.dragTo(a+p,b+(q//2),duration = 0.15)

def drawI(a,b):
    pg.click(a,b)
    pg.dragTo(a+p,b,duration = 0.15)
    pg.click(a+(p//2),b)
    pg.dragTo(a+(p//2),b+q,duration = 0.15)
    pg.click(a,b+q)
    pg.dragTo(a+p,b+q,duration = 0.15)

def drawJ(a,b):
    pg.click(a,b)
    pg.dragTo(a+p,b,duration = 0.15)
    pg.click(a+(p//2),b)
    pg.dragTo(a+(p//2),b+(5*q)//6,duration = 0.15)
    pg.dragTo(a+(2*p)//5,b+q,duration = 0.1)
    pg.dragTo(a+p//10,b+q,duration = 0.1)
    pg.dragTo(a,b+(5*q)//6,duration = 0.1)

def drawK(a,b):
    pg.click(a,b)
    pg.dragTo(a,b+q,duration = 0.15)
    pg.click(a+p,b)
    pg.dragTo(a,b+(q//2),duration = 0.15)
    pg.dragTo(a+p,b+q,duration = 0.15)

def drawL(a,b):
    pg.click(a,b)
    pg.dragTo(a,b+q,duration = 0.15)
    pg.dragTo(a+p,b+q,duration = 0.15)

def drawM(a,b):
    pg.click(a,b+q)
    pg.dragTo(a,b,duration = 0.15)
    pg.dragTo(a+p//2,b+q//2,duration = 0.15)
    pg.dragTo(a+p,b,duration = 0.15)
    pg.dragTo(a+p,b+q,duration = 0.15)

def drawN(a,b):
    pg.click(a,b+q)
    pg.dragTo(a,b,duration = 0.15)
    pg.dragTo(a+p,b+q,duration = 0.15)
    pg.dragTo(a+p,b,duration = 0.15)

def drawO(a,b):
    pg.click(a,b+q//6)
    pg.dragTo(a,b+(5*q)//6,duration = 0.15)
    pg.dragTo(a+p//5,b+q,duration = 0.1)
    pg.dragTo(a+(4*p)//5,b+q,duration = 0.15)
    pg.dragTo(a+p,b+(5*q)//6,duration = 0.1)
    pg.dragTo(a+p,b+q//6,duration = 0.15)
    pg.dragTo(a+(4*p)//5,b,duration = 0.1)
    pg.dragTo(a+p//5,b,duration = 0.15)
    pg.dragTo(a,b+q//6,duration = 0.1)

def drawP(a,b):
    pg.click(a,b+q)
    pg.dragTo(a,b,duration = 0.15)
    pg.dragTo(a+(4*p)//5,b,duration = 0.15)
    pg.dragTo(a+p,b+q//10,duration = 0.1)
    pg.dragTo(a+p,b+(2*q)//5,duration = 0.1)
    pg.dragTo(a+(4*p)//5,b+q//2,duration = 0.1)
    pg.dragTo(a,b+q//2,duration = 0.1)

def drawQ(a,b):
    pg.click(a,b+q//6)
    pg.dragTo(a,b+(5*q)//6,duration = 0.15)
    pg.dragTo(a+p//5,b+q,duration = 0.1)
    pg.dragTo(a+(4*p)//5,b+q,duration = 0.15)
    pg.dragTo(a+p,b+(5*q)//6,duration = 0.1)
    pg.dragTo(a+p,b+q//6,duration = 0.15)
    pg.dragTo(a+(4*p)//5,b,duration = 0.1)
    pg.dragTo(a+p//5,b,duration = 0.15)
    pg.dragTo(a,b+q//6,duration = 0.1)
    pg.click(a+(p//2),b+(5*q)//6)
    pg.dragTo(a+p,b+q,duration = 0.1)

def drawR(a,b):
    pg.click(a,b+q)
    pg.dragTo(a,b,duration = 0.15)
    pg.dragTo(a+(4*p)//5,b,duration = 0.15)
    pg.dragTo(a+p,b+q//10,duration = 0.1)
    pg.dragTo(a+p,b+(2*q)//5,duration = 0.1)
    pg.dragTo(a+(4*p)//5,b+q//2,duration = 0.1)
    pg.dragTo(a,b+q//2,duration = 0.1)
    pg.dragTo(a+p,b+q,duration = 0.15)

def drawS(a,b):
    pg.click(a+p,b+q//10)
    pg.dragTo(a+(7*p)//8,b,duration = 0.1)
    pg.dragTo(a+p//8,b,duration = 0.1)
    pg.dragTo(a,b+q//10,duration = 0.1)
    pg.dragTo(a,b+(4*q)//10,duration = 0.1)
    pg.dragTo(a+p//8,b+(q//2),duration = 0.1)
    pg.dragTo(a+(7*p)//8,b+(q//2),duration = 0.1)
    pg.dragTo(a+p,b+(3*q)//5,duration = 0.1)
    pg.dragTo(a+p,b+(9*q)//10,duration = 0.1)
    pg.dragTo(a+(7*p)//8,b+q,duration = 0.1)
    pg.dragTo(a+p//8,b+q,duration = 0.1)
    pg.dragTo(a,b+(9*q)//10,duration = 0.1)

def drawT(a,b):
    pg.click(a,b)
    pg.dragTo(a+p,b,duration = 0.15)
    pg.click(a+(p//2),b)
    pg.dragTo(a+(p//2),b+q,duration = 0.15)

def drawU(a,b):
    pg.click(a,b)
    pg.dragTo(a,b+(q - ((17*q)//100)),duration = 0.15)
    pg.dragTo(a + p//5,b+q,duration = 0.1)
    pg.dragTo(a + (4*p)//5,b+q,duration = 0.15)
    pg.dragTo(a+p,b+(q - ((17*q)//100)),duration = 0.1)
    pg.dragTo(a+p,b,duration = 0.15)

def drawV(a,b):
    pg.click(a,b)
    pg.dragTo(a+(p//2),b+q,duration = 0.15)
    pg.dragTo(a+p,b,duration = 0.15)

def drawW(a,b):
    pg.click(a,b)
    pg.dragTo(a+p//4,b+q,duration = 0.15)
    pg.dragTo(a+p//2,b+q//2,duration = 0.15)
    pg.dragTo(a+(3*p)//4,b+q,duration = 0.15)
    pg.dragTo(a+p,b,duration = 0.15)

def drawX(a,b):
    pg.click(a,b)
    pg.dragTo(a+p,b+q,duration = 0.15)
    pg.click(a+p,b)
    pg.dragTo(a,b+q,duration = 0.15)

def drawY(a,b):
    pg.click(a,b)
    pg.dragTo(a+p//2,b+q//2,duration = 0.15)
    pg.dragTo(a+p//2,b+q,duration = 0.15)
    pg.click(a+p,b)
    pg.dragTo(a+p//2,b+q//2,duration = 0.15)

def drawZ(a,b):
    pg.click(a,b)
    pg.dragTo(a+p,b,duration = 0.15)
    pg.dragTo(a,b+q,duration = 0.15)
    pg.dragTo(a+p,b+q,duration = 0.15)

#-----------------------------------------------------------------------------

drawLetter = {
    "a":drawA, "b":drawB, "c":drawC,
    "d":drawD, "e":drawE, "f":drawF,
    "g":drawG, "h":drawH, "i":drawI,
    "j":drawJ, "k":drawK, "l":drawL,
    "m":drawM, "n":drawN, "o":drawO,
    "p":drawP, "q":drawQ, "r":drawR,
    "s":drawS, "t":drawT, "u":drawU,
    "v":drawV, "w":drawW, "x":drawX,
    "y":drawY, "z":drawZ
}


#---------------------- Function to draw one word ----------------------------

def drawName(name,x,y,spacing): #name: takes one word (str)
                #x,y: coordinates of top left corner of thebounds for a letter
                #spacing: space between each letter
    for i,ch in enumerate(name):
        #print(x+i*(p+spacing),y)
        if x+i*(p+spacing) > screenwidth-p:
            print('"'+name+'"'+' went out of bound in width')
            return
        try:
            drawLetter[ch.lower()](x+i*(p+spacing),y)
        except:
            pass
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
#---------- Function to draw multiple words: one below the other -------------

def drawNames(names,sleeptime,letter_spacing): #names: a list of words
                           #sleeptime: wait time before start drawing words
                           #letter_spacing: space between each letter in words
    screenwidth, screenheight = pg.size()
    #print('Place the mouse pointer at its initial position\nYou have',sleeptime,'seconds') #Method1
    time.sleep(sleeptime)
    x,y = pg.position()
    for i,name in enumerate(names):
        if y+i*((23*q)//20) > screenheight-q:
            print('"'+name+'"'+' went out of bound in height')
            return
        drawName(name,x,y+i*((23*q)//20),letter_spacing)
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
if __name__ == '__main__':
    names = input("Enter names: ")
    openPaint()
    time.sleep(1)
    pg.moveTo(int(0.06*screenwidth),int(0.3*screenheight)) #Method2
    drawNames(names.split(),sleeptime = 1,letter_spacing = 15)
