import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from first import *
from tkinter import *

class AnalysisGraph(Frame):
    
    def __init__(self,master): #Function to initialize the window
        #Initialize the frame
        super(AnalysisGraph,self).__init__(master)
        self.grid()
        self.display_widgets()
        self.dataset=readData()
        #self.dataset=cleanData(self.dataset)
        
    def display_widgets(self):  #Function to create the widgets to take data
        
        Label(self,text="ENTER DATA TO SELECT COLUMNS",width=25).grid(row=0,column=0,sticky=W)
        Label(self,text="   ",width=25).grid(row=0,column=1,sticky=W)
        Label(self,text="   ",width=25).grid(row=0,column=2,sticky=W)
#        self.close=Button(self,text="Quit",command=self.closeWindow)
#        self.close.grid(row=0,column=3,sticky=W)
        
        #Radiobutton for selecting columns
        Label(self,text="Select Columns:* ").grid(row=1,column=0,sticky=W)
        self.col=StringVar()
        Radiobutton(self,text="ABOARD",variable=self.col,value='Aboard').grid(row=1,column=1,sticky=W)
        Radiobutton(self,text="FATALITIES",variable=self.col,value='Fatalities').grid(row=1,column=2,sticky=W)
        Radiobutton(self,text="GROUND",variable=self.col,value='Ground').grid(row=1,column=3,sticky=W)
        
        #Button to submit the data
        self.btn1=Button(self,text="SUBMIT COLUMNS",command=self.displayGraph)
        self.btn1.grid(row=2,column=2,columnspan=2,sticky=W)
        
    def displayGraph(self): #Function to display the graph
        if self.col.get():
            col=self.col.get()
        draw(self.dataset,col)   #Calls the function that creates a window that displays the graph
    
    def closeWindow(self):  #Function to close the window
        self.master.quit()
        self.master.destroy()


def draw(dataset,col):  #Function to display the graph in a separate window
    #initialize the new window
    root = Tk()
    root.wm_title("Embedding in TK")
    
    #initialize the Fugure object
    f = Figure(figsize=(8, 6), dpi=100)
    a = f.add_subplot(111)
    
    #plot the graph
    a.plot(dataset[col])
    a.set_title('Line graph for analysis of number of '+col)
    a.set_xlabel(col)
    a.set_ylabel('Number')
    
    
    #create a DrawingArea
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
    
    def _quit():    #Function to quit the window
        root.quit()     # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate
    
    #button to quit the window
    button = Button(master=root, text='Quit', command=_quit)
    button.pack(side=BOTTOM)
    
    #creating the loop
    root.mainloop()
