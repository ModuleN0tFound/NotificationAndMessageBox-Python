from ctypes import windll
from win10toast import ToastNotifier
from win32con import MB_OKCANCEL

def MessageBox(title, text, style):
    #  0 : OK
    #  1 : OK | Cancel
    #  2 : Abort | Retry | Ignore
    #  3 : Yes | No | Cancel
    #  4 : Yes | No
    #  5 : Retry | Cancel
    #  6 : Cancel | Try Again | Continue

    return windll.user32.MessageBoxW(0, text, title, style)

def Notifications(title, text, duration):
    toaster = ToastNotifier()

    toaster.show_toast(title, text, duration=duration)

if MessageBox('Title', "Hello", 1) == MB_OKCANCEL:
    print('You Clicked `OK` Button')

Notifications('Title', 'Hello', 3)