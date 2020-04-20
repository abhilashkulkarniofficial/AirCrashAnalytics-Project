#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:14:31 2017

@author: abhilashsk
"""

from tkinter import *
from first import *
import datetime


class AnalysisNumber(Frame):
    

    def __init__(self, master): #Function to initialize the window
        #Initialize the frame
        super(AnalysisNumber,self).__init__(master)
        self.grid()
        self.display_widgets()
        self.dataset=readData()
        self.dataset=cleanData(self.dataset)
        
    def display_widgets(self):   #Function to create Widgets to take data
        """
        This section is for selecting columns to view the dataset
        """
        #Labels for setting the width of the columns
        Label(self,text="ENTER DATA TO SELECT COLUMNS",width=25).grid(row=0,column=0,sticky=W)
        Label(self,text="   ",width=25).grid(row=0,column=1,sticky=W)
        Label(self,text="   ",width=25).grid(row=0,column=2,sticky=W)
        Label(self,text="   ",width=25).grid(row=0,column=3,sticky=W)
        Label(self,text="   ",width=25).grid(row=0,column=4,sticky=W)
        Label(self,text="   ",width=25).grid(row=0,column=5,sticky=W)
#        self.close=Button(self,text="Quit",command=self.closeWindow)
#        self.close.grid(row=0,column=6,sticky=W)
        
        #Text boxes for take From and To date
        Label(self,text="From (YYYY-MM-DD) :*").grid(row=1,column=0,sticky=W)
        self.frm=Entry(self)
        self.frm.grid(row=1,column=1,sticky=W)
        
        Label(self,text="To (YYYY-MM-DD) :*").grid(row=2,column=0,sticky=W)
        self.to=Entry(self)
        self.to.grid(row=2,column=1,sticky=W)
        
        #Checkboxes for selecting columns from the dataset
        Label(self,text="Select Columns: *").grid(row=3,column=0,sticky=W)
        self.operator=BooleanVar()
        Checkbutton(self,text="OPERATOR",variable=self.operator).grid(row=3,column=1,sticky=W)
        self.route=BooleanVar()
        Checkbutton(self,text="ROUTE",variable=self.route).grid(row=3,column=3,sticky=W)
        self.flight=BooleanVar()
        Checkbutton(self,text="FLIGHT",variable=self.flight).grid(row=3,column=2,sticky=W)
        self.regis=BooleanVar()
        Checkbutton(self,text="REGISTRATION",variable=self.regis).grid(row=4,column=1,sticky=W)
        self.aboard=BooleanVar()
        Checkbutton(self,text="ABOARD",variable=self.aboard).grid(row=4,column=2,sticky=W)
        self.fatal=BooleanVar()
        Checkbutton(self,text="FATALITIES",variable=self.fatal).grid(row=4,column=3,sticky=W)
        
        #Text boxes to take Start and End indices of rows
        Label(self,text="Start Index:*").grid(row=5,column=0,sticky=W)
        self.rowStart=Entry(self)
        self.rowStart.grid(row=5,column=1,sticky=W)
        Label(self,text="End Index:*").grid(row=5,column=2,sticky=W)
        self.rowEnd=Entry(self)
        self.rowEnd.grid(row=5,column=3,sticky=W)
        
        #Button to submit the data
        self.btn1=Button(self,text="SUBMIT COLUMNS",command=self.displayCols)
        self.btn1.grid(row=6,column=2,columnspan=2,sticky=W)
        
        
        """
        This section is for displaying Descriptive Statistics
        """
        #Label for Descriptive Statistics section
        Label(self,text="DESCRIPTIVE STATISTICS",width=25).grid(row=7,column=0,sticky=W)
        
        #Radiobutton for selecting columns
        Label(self,text="Select Columns:* ").grid(row=8,column=0,sticky=W)
        self.col=StringVar()
        Radiobutton(self,text="ABOARD",variable=self.col,value='Aboard').grid(row=8,column=1,sticky=W)
        Radiobutton(self,text="FATALITIES",variable=self.col,value='Fatalities').grid(row=8,column=2,sticky=W)
        Radiobutton(self,text="GROUND",variable=self.col,value='Ground').grid(row=8,column=3,sticky=W)
        
        #Radiobutton to select particular statistic
        Label(self,text="Select Result:* ").grid(row=9,column=0,sticky=W)
        self.stat=StringVar()
        Radiobutton(self,text="COUNT",variable=self.stat,value='count').grid(row=9,column=1,sticky=W)
        Radiobutton(self,text="MEAN",variable=self.stat,value='mean').grid(row=9,column=2,sticky=W)
        Radiobutton(self,text="STANDARD DEVIATION",variable=self.stat,value='std').grid(row=9,column=3,sticky=W)
        Radiobutton(self,text="MINIMUM",variable=self.stat,value='min').grid(row=9,column=4,sticky=W)
        Radiobutton(self,text="MAXIMUM",variable=self.stat,value='max').grid(row=9,column=5,sticky=W)
        Radiobutton(self,text="ALL",variable=self.stat,value='all').grid(row=9,column=6,sticky=W)
        
        
        #Entries for displaying stats
        Label(self,text="COUNT",width=25).grid(row=10,column=0,sticky=W)
        self.count=Entry(self)
        self.count.grid(row=11,column=0,sticky=W)
        Label(self,text="MEAN",width=25).grid(row=10,column=1,sticky=W)
        self.mean=Entry(self)
        self.mean.grid(row=11,column=1,sticky=W)
        Label(self,text="STANDARD DEVIATION",width=25).grid(row=10,column=2,sticky=W)
        self.std=Entry(self)
        self.std.grid(row=11,column=2,sticky=W)
        Label(self,text="MINIMUM",width=25).grid(row=10,column=3,sticky=W)
        self.min=Entry(self)
        self.min.grid(row=11,column=3,sticky=W)
        Label(self,text="MAXIMUM",width=25).grid(row=10,column=4,sticky=W)
        self.max=Entry(self)
        self.max.grid(row=11,column=4,sticky=W)

        #Button to submit data
        self.btn2=Button(self,text="SUBMIT STATISTICS",command=self.descStat)
        self.btn2.grid(row=12,column=2,columnspan=2,sticky=W)
        
    def displayCols(self):  #Function to display the columns
        #initialize variables
        msg={}
        col=0
        r=20
        
        #Taking data from the entries
        if self.frm.get() and self.to.get():
            frm=datetime.datetime.strptime(self.frm.get(), "%Y-%m-%d").date()
            to=datetime.datetime.strptime(self.to.get(), "%Y-%m-%d").date()
        else:
            frm=datetime.datetime.strptime("1910-01-01", "%Y-%m-%d").date()
            to=datetime.datetime.strptime("1990-01-01", "%Y-%m-%d").date()
            
        if  self.rowStart.get() and self.rowEnd.get():
            rowStart=int(self.rowStart.get())
            rowEnd=int(self.rowEnd.get())
        else:
            rowStart=1
            rowEnd=desDataset(self.dataset,"shape")[0]

        
        #filtering the dataset by dates
        newds=self.dataset
        newds=filterDs(newds,frm,to)
        
        
        #Checking for selected checkboxes
        if self.operator.get():
            msg['OPERATOR']=getColumns(newds,'Operator',rowStart,rowEnd)
        if self.route.get():
            msg['ROUTE']=getColumns(newds,'Route',rowStart,rowEnd)
        if self.flight.get():
            msg['FLIGHT NUMBER']=getColumns(newds,'Flight #',rowStart,rowEnd)
        if self.regis.get():
            msg['REGISTRATION']=getColumns(newds,'Registration',rowStart,rowEnd)
        if self.aboard.get():
            msg['ABOARD']=getColumns(newds,'Aboard',rowStart,rowEnd)
        if self.fatal.get():
            msg['FATALITIES']=getColumns(newds,'Fatalities',rowStart,rowEnd)
        
        #Displaying the columns in textareas
        for x in msg.keys():
            Label(self,text=x).grid(row=r,column=col,sticky=W)
            self.t=Text(self,width=25,height=rowEnd-rowStart,wrap=WORD)
            self.t.grid(row=r+2,column=col,rowspan=2,sticky=W)
            self.t.config(state=NORMAL)
            self.t.delete(0.0,END)
            self.t.insert(0.0,msg[x])
            self.t.config(state=DISABLED)
            col+=1
        
    def descStat(self): #Function to get descriptive statistics of a particular column
        #initializing dictionary to store the entry objects
        x={'count':self.count,'mean':self.mean,'std':self.std,'min':self.min,'max':self.max}
        
        #reading data from the radiobuttons
        if self.col.get() and self.stat.get():
            col=self.col.get()
            stat=self.stat.get()
        
        #fetching the statistics
        desc=desColumns(self.dataset,col)
        
        #displaying the result in the text boxes
        if self.stat.get()=='all':
            for i in x.keys():
                x[i].config(state=NORMAL)
                x[i].delete(0,END)
                x[i].insert(0,desc[i])
                x[i].config(state=DISABLED)
        else:
            x[self.stat.get()].config(state=NORMAL)
            x[self.stat.get()].delete(0,END)
            x[self.stat.get()].insert(0,desc[stat])
            x[self.stat.get()].config(state=DISABLED)
        
    def closeWindow(self):  #Function to close the window
        self.master.quit()
        self.master.destroy()

#root=Tk()
#root.title("Data analysis of Aircrash Dataset")
#root.geometry("2000x2000")
#app=Application(root)
#root.mainloop()