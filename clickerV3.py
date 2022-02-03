import tkinter

clickcounter = 0
update = ""
gui = tkinter.Tk()
gui. geometry("400x500")
gui.title("Clicker V3")
gui.configure(
    bg="gray"
)
def hover(event):
    gui.configure(bg="yellow")
def hover_leave(e):
    if clickcounter < 0:
        gui.configure(bg="red")
    elif clickcounter > 0:
        gui.configure(bg="#00DC00")
    else:
        gui.configure(bg="gray")
    
def colorchanger():
    if clickcounter < 0:
        gui.configure(bg="red")
    elif clickcounter > 0:
        gui.configure(bg="#00DC00")
    else:
        gui.configure(bg="gray")

def counterchanger(e):
    global update, clickcounter
    if update == 'up':
        clickcounter *= 3
    elif update == 'down':
        clickcounter /=3
    counter.config(text= clickcounter)
        

# de up button

def up():
    global clickcounter,update
    clickcounter += 1
    counter.config(text=clickcounter)
    counter.pack()
    update='up'
    gui.after(10, colorchanger)
    

button1 = tkinter.Button(gui, font=("arial", 20, "bold"), command= up, activebackground="#00DC00")
button1.configure(
    text="Up",
    bg=("#00DC00"),
    padx= 30
)
button1.pack(
    pady= 30
    
)

# de counter in het midden     

counter = tkinter.Label(
    gui,
    text=clickcounter,
    padx=80,
    pady=30,
    font=("arial", 30, "bold"),
    borderwidth=2,
    relief="solid"
)
counter.pack(
    
)

# de Down button
def down():
    global clickcounter,e,update
    clickcounter =clickcounter - 1
    counter.config(text=clickcounter)
    counter.pack()
    update='down'
    gui.after(10, colorchanger)
    

button2 = tkinter.Button(
    gui,
    text="down",
    font=("arial", 30, "bold"),
    command= down,
    bg="red",
    activebackground="red",
    
)
button2.pack(
    pady=30
)
button2.bind("<Enter>",hover)
button2.bind("<Leave>",hover_leave)
button1.bind("<Enter>",hover)
button1.bind("<Leave>",hover_leave)
counter.bind('<Double-Button>', counterchanger)

gui.mainloop()