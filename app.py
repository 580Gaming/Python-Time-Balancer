import time
from tkinter import *
from plyer import notification

WorkTime = int(0)
BreakTime = int(0)
RunCycles = float(0)
TargetCycles = int(10)
IsWork = bool(True)

def StartProgram():
    if WorkTime == 0 or BreakTime == 0 or RunCycles == 0:
        print("invalid times or cycles")

def Waiter():
    if IsWork == True:
        time.sleep(WorkTime)
        print('Work Done')
    else:
        time.sleep(BreakTime)
        print('Break Time')


def WorkTimeSubmit():
    WorkTime = int(WorkTimeEntry.get())
    print(WorkTime)

def BreakTimeSubmit():
    BreakTime = int(BreakTimeEntry.get())
    print(BreakTime)

while RunCycles > 0:
    Waiter()
    IsWork = not IsWork
    RunCycles -= .5

window = Tk()

#Testing if this works.
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

BreakTimeSubmitButton = Button(window, text='Submit break time', fg='black', bg='white', font=('',10,), command=BreakTimeSubmit)
BreakTimeSubmitButton.pack(pady=10)

StartButton = Button(window, text='Start', font=('',10,), bg='white', fg='black', command=StartProgram)
StartButton.pack()
window.mainloop()
