import time
from plyer import notification


WaitTime = int(0)
WorkTime = int(input("Enter worktime: "))
BreakTime = int(input('Enter breaktime: '))
Cycles = float(input('Enter cycles: '))
BreakFirstChecker = str(input('Would you like your break first? Y/n: '))
EndMessage = str(input('End Message: '))
IsWork = bool(True)
BreakFirst = bool(False)

if BreakFirstChecker == 'y' or BreakFirstChecker == 'Y':
    IsWork = False
    Cycles += .5
    print('break first')

def Setter():
    if IsWork == True:
        NotifyUserWork()
        time.sleep(WorkTime * 60)

    else:
        NotifyUser()
        time.sleep(BreakTime * 60)

def NotifyUserWork():
    notification.notify(title='TimeKeeper',message='Time to start work, sorry.', timeout=5)

def NotifyUserWorkEnd():
    if EndMessage:
        notification.notify(title='TimeKeeper',message=EndMessage, timeout=5)
    else:
         notification.notify(title='TimeKeeper',message='Work has ended, YAY', timeout=5)


def NotifyUser():
    notification.notify(title='TimeKeeper',message="It's time to start your break. :)", timeout=5)

def NotifyUserEnd():
    notification.notify(title='TimeKeeper',message="Goodbye break, hello work. :(", timeout=5)

while Cycles > 0:
    Setter()
    IsWork = not IsWork
    Cycles -= .5


if Cycles == 0:
    NotifyUserWorkEnd()

    if EndMessage:
        print(EndMessage)
    else: 
        print('Shift Complete')
