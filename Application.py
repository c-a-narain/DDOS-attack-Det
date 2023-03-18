import numpy as np


import pandas as pd
import pickle

import click

#RSA

from tkinter import *
from tkinter import ttk  
from tkinter import Menu  
from tkinter import messagebox as mbox  
# import filedialog module
from tkinter import filedialog
flg=0
import tkinter as tk

# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a CSV File",
                                          filetypes = (("CSV files",
                                                        "*.csv*"),
                                                       ("all files",
                                                        "*.*")))
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
    global f
    f = filename


def start():

    print("Process Started")
    dataset = pd.read_csv(f)
    dataset=dataset.dropna(how="any")
    print(dataset)

    print(dataset.info())

    X = dataset.iloc[:,6:16].values

    # load the model from disk
    model = pickle.load(open('knnpickle_file', 'rb'))
    ypred = model.predict(X)
    ypred = ypred.round()
    print(ypred)
    app = tk.Tk()
    if(ypred[0]==0):
        print("Normal")
        label_file_explorer.configure(text="Result for the request: The Input Request is Normal")
        app.title("DDOS Attack Detection")
        ttk.Label(app, text="Result for the request: The Input Request is Normal").grid(column=0,row=0,padx=20,pady=30)  
        menuBar = Menu(app)
        app.config(menu=menuBar)
    else:
        print("DDOS Attack Detected")
        label_file_explorer.configure(text="Result for the request: The Input Request is Malicious and Blocked")
        app.title("DDOS Attack Detection")
        ttk.Label(app, text="Result for the request: The Input Request is a DDOS Attack and Blocked").grid(column=0,row=0,padx=20,pady=30)
        menuBar = Menu(app)
        app.config(menu=menuBar)
    
        
if __name__ == '__main__':
    window = Tk()
  
    # Set window title
    window.title('DDOS Attack Detection')
      
    # Set window size
    window.geometry("700x400")
      
    #Set window background color
    window.config(background = "white")
      
    # Create a File Explorer label
    label_file_explorer = Label(window,
                                text = "Please give Input Request",
                                width = 100, height = 4,
                                fg = "blue")
         
    button_explore = Button(window,
                            text = "Browse Request Files",
                            command = browseFiles)
    button_exit = Button(window,
                         text = "exit",
                         command = exit)  
    button_start = Button(window,
                         text = "Start Analyzing Request",
                         command = start)

       
    # Grid method is chosen for placing
    # the widgets at respective positions
    # in a table like structure by
    # specifying rows and columns
    label_file_explorer.grid(column = 1, row = 1, padx=5, pady=5)
    button_explore.grid(column = 1, row = 3, padx=5, pady=5)
    button_exit.grid(column = 1,row = 9, padx=5, pady=5)
    button_start.grid(column = 1,row = 12, padx=5, pady=5)
      
    # Let the window wait for any events
    
    
    window.mainloop()


    
