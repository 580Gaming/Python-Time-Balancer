import time
from tkinter import *

WorkTime = int(0)
BreakTime = int(0)
RunCycles = int(0)
IsWork = bool(True)

def StartButton():
    while RunCycles > 0:
        if IsWork == True:
            time.sleep(WorkTime)
            RunCycles -= 1
        else:
            time.sleep(BreakTime)

def WorkTimwSubmit():
    WorkTime = int(WorkTimeEntry.get()*60)
    print(WorkTime)

window = Tk()

window.title("Time Balancer (DEBUG.Linux/Win/Mac)")
window.geometry('550x650')
window.config(background='black')

WorkTimeEntry = Entry(window, font = ("",20,""))
WorkTimeEntry.pack(side = LEFT)



window.mainloop()