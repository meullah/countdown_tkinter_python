import tkinter as tk
import pickle
from tkinter import simpledialog
is_s_pressed = False
COUNTDOWN_VALUE = 45
FILE_NAME = 'countdown_value'

def check_key_Stroke(event):
    # print(event.keysym)
    global is_s_pressed
    global COUNTDOWN_VALUE
    if is_s_pressed:
        if str(event.keysym) == 'p' or str(event.keysym) == 'P':
            COUNTDOWN_VALUE = 0
        else:
            is_s_pressed = False

    if str(event.keysym) == 's' or str(event.keysym) == 'S':
        is_s_pressed = True

def update_countdown_value(event):
    global COUNTDOWN_VALUE
    COUNTDOWN_VALUE = simpledialog.askinteger("Input a number","Enter a new countdown value")
    outfile = open(FILE_NAME,'wb')
    # print(countdown_value)
    pickle.dump(COUNTDOWN_VALUE,outfile)
    outfile.close()

def update(label):
    global COUNTDOWN_VALUE
    def decrement():
        global COUNTDOWN_VALUE
        COUNTDOWN_VALUE -=1 if COUNTDOWN_VALUE != 0 else  0
        if COUNTDOWN_VALUE > 10 :
            label.config(text=str(" time left : " + str(COUNTDOWN_VALUE)+ " sec"),font=("Courier", 40),fg='Black')
        else:
            if COUNTDOWN_VALUE != 0 :
                label.config(text=str(" time left : " + str(COUNTDOWN_VALUE)+ " sec"),font=("Courier", 40),fg='Orange')
            else:
                label.config(text=str(" time left : " + str(COUNTDOWN_VALUE)+ " sec"),font=("Courier", 40),fg='Red')

        label.after(1000,decrement)
    decrement()


infile = open(FILE_NAME,'rb')
COUNTDOWN_VALUE = pickle.load(infile)
infile.close()

windows = tk.Tk()
windows.title("Count Down")
windows.geometry('700x200')

windows.bind("<Key>",check_key_Stroke)
windows.bind("<Button-3>",update_countdown_value)

label = tk.Label(windows)
label.pack()
update(label)

windows.mainloop()
