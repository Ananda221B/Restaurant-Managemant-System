from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime

def main():
    root = Tk()
    app = Window1(root)

class Window1:
    def __init__(self,master):
        self.master= master
        self.master.title("Restaurent Login System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame=Frame(self.master,bg='powder blue')
        self.frame.pack()

        self.btnLogin=Button(self.frame,text='login',command=self.new_window)
        self.btnLogin.grid(row=3,colomn=0)
        self.btnReset = Button(self.frame, text='login')
        self.btnReset.grid(row=3, colomn=1)
        self.btnExit = Button(self.frame, text='login')
        self.btnExit.grid(row=3, colomn=2)

    def new_Window(self):
        self.newWindow= Toplevel(self.master)
        self.app=Window2(self.newWindow)
class Window2:
    def __init__(self,master):
        self.master=master
        self.master.title("Resturent Management System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame=Frame(self.master,bg='powder blue')
        self.frame.pack()




if main=="main__":
    main()

