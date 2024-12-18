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


window = Tk()

entry = Entry(window, font = ("",20,""))
entry.pack(side = LEFT)
window.mainloop()