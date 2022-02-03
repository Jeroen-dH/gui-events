from cgitb import text
import tkinter
import time
import random
from tkinter import messagebox
from tkinter.messagebox import *

timer=20
points = 0
a =False
list1 = ["druk op de w","druk op de a","druk op de s","druk op de d","druk op de spatiebalk","enkele klik","dubbele klik","driedubbele klik."]
list2 = ["<w>","<a>","<s>","<d>","<space>","<Button>","<Double-Button>","<Triple-Button>"]
var1 = random.randint(0,7)

gui = tkinter.Tk()
gui.geometry("550x550")
gui.title("FPSTrainer")
gui.configure(bg="gray")

def countdown():
    global timer, a
    if a == False:
        a = True
        destroyStartButton()
    elif timer == -1:
        popup()      
    elif timer > -1:
        timer = timer
        timerlabel.config(text=timer)
        timer = timer - 1
        gui.after(1000, countdown)
      

def destroyStartButton():
    startButton.destroy()
    countdown()

def popup():
    info = showinfo(title= "Time's up", message="Je tijd is om en je hebt "+str(points)+ " punten gehaald")

def addpoints(e):
    global points
    var1 = random.randint(0,7)
    points += 1
    pointslabel.config(text="Points: "+str(points))
    gui.bind(list2[var1],addpoints)
    Clickbutton.configure(
        text=(list1[var1]) 
    )       
    Clickbutton.pack()



def bindfunction():
    gui.bind(list2[var1],addpoints)
def unbind():
    gui.unbind(list2[var1],addpoints)

Clickbutton = tkinter.Label(
    gui,
    text=(list1[var1]),
    padx= 20,
    pady= 20
)

def randombutton():
    Clickbutton.configure(
        text=(list1[var1])
    )       
    Clickbutton.pack()    

timerlabel = tkinter.Label(
    gui,
    text="(Timer)",
    relief="solid",
    padx="125",
    bg="black",
    fg="White"

)
timerlabel.place(anchor="nw")

pointslabel = tkinter.Label(
    gui,
    text="Points: "+ str(points),
    relief="solid",
    padx="125",
    bg="black",
    fg="white",
)
pointslabel.place(x=260)
    
startButton = tkinter.Button(
    gui,
    text="Click to start",
    command=lambda:[randombutton(), countdown(),bindfunction()]
)
startButton.place(relx=.5, rely=.5, anchor="center")

gui.mainloop()