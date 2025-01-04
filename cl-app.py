import time
from plyer import notification


WaitTime = int(0)
TimeOne = int(input("Enter worktime: "))
TimeTwo = int(input('Enter breaktime: '))
Runs = float(input('Enter cycles: '))
BreakFirstChecker = str(input('Would you like your break first? Y/n: '))
EndMessage = str(input('End Message: '))
StageOne = bool(True)
BreakFirst = bool(False)

if BreakFirstChecker == 'y' or BreakFirstChecker == 'Y':
    StageOne = False
    Runs += .5
    print('break first')

def Setter():
    if StageOne == True:
        NotifyUserWork()
        time.sleep(TimeOne * 60)

    else:
        NotifyUser()
        time.sleep(TimeTwo * 60)

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

while Runs > 0:
    Setter()
    StageOne = not StageOne
    Runs -= .5


if Runs == 0:
    NotifyUserWorkEnd()

    if EndMessage:
        print(EndMessage)
    else: 
        print('Shift Complete')
