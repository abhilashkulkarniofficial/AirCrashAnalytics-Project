#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:06:11 2017

@author: abhilashsk
"""

from tkinter import *
from projectgui import *
from projectgui2 import *

class StartPage(Frame):
    
    def __init__(self, master): #Function to initialize the frame
        self.master = master
        self.frame = Frame(self.master)
        
        #Creating the buttons
        self.button1 = Button(self.frame, text = 'ANALYSIS BY NUMBERS', width = 50, command = self.new_window1)
        self.button1.pack()
        self.button2 = Button(self.frame, text = 'ANALYSIS BY GRAPH', width = 50, command = self.new_window2)
        self.button2.pack()
        self.button3 = Button(self.frame, text = 'CLOSE', width = 50, command = self.closeWindow)
        self.button3.pack()
        self.frame.pack()

    def new_window1(self):  #Function to create an Analysis by numbers window
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("Analysis by Numbers")
        self.newWindow.geometry("2000x1000")
        self.app = AnalysisNumber(self.newWindow)
        
    def new_window2(self):  #Function to create an Analysis by graph window
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("Analysis by Graph")
        self.newWindow.geometry("1000x1000")
        self.app=AnalysisGraph(self.newWindow)
    
    def closeWindow(self):  #Function to close the window
        self.master.quit()
        self.master.destroy()


def main(): #Main Function
    root = Tk()
    root.geometry("500x500")
    root.title("Data Analysis of Aircrash Dataset")
    app = StartPage(root)
    root.mainloop()

if __name__ == '__main__':
    main()