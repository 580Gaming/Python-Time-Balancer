import time
from tkinter import *

WorkTime = int(0)
BreakTime = int(0)
RunCycles = int(0)
IsWork = bool(True)

def StartProgram():
    global RunCycles
    while RunCycles >= 0:
        if IsWork == True:
            time.sleep(WorkTime)
            RunCycles -= 1
            print("Work Over, congrats")
        else:
            time.sleep(BreakTime)
            print('Break Over, damn')

def WorkTimeSubmit():
    WorkTime = int(WorkTimeEntry.get()) * 60
    print(WorkTime)

def BreakTimeSubmit():
    BreakTime = int(BreakTimeEntry.get())
window = Tk()

#test
window.title("Time Balancer (DEBUG.Linux/Win/Mac)")
window.geometry('450x650')
window.config(background='black')

WorkTimeLabel = Label(window, text='Please enter work time in minutes.',fg='white' , font=('',15,),bg='black')
WorkTimeLabel.pack()

WorkTimeEntry = Entry(window, font = ("",20,""))
WorkTimeEntry.pack()

WorkTimeSubmitButton = Button(window, text='Submit work time', fg='black', bg='white', font=('',10,), command=WorkTimeSubmit)
WorkTimeSubmitButton.pack(pady=10)

BreakTimeEntry = Entry(window, font=("",20,""))
BreakTimeEntry.pack()

StartButton = Button(window, text='Start', font=('',10,), bg='white', fg='black', command=StartProgram)
StartButton.pack()
window.mainloop()
