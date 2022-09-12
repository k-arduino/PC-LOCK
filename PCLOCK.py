from tkinter import *
import tkinter.font
from PIL import ImageTk, Image
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import date, datetime
import sys
import random

cred = credentials.Certificate('mykey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://jungyo-iot-server-default-rtdb.firebaseio.com/'
})

TD = datetime.now()

DATE = TD.strftime('%Y년 %m월 %d일')
Refresh1 = db.reference('Lenovo Y540/Input/PCLOCK')
Refresh1.update({'DATE' : str(DATE)})

TIME = TD.strftime('%H시 %M분 %S초')
Refresh2 = db.reference('Lenovo Y540/Input/PCLOCK')
Refresh2.update({'TIME' : str(TIME)})

KEY = random.randrange(1000000,9999999)
Refresh3 = db.reference('Lenovo Y540/Input/PCLOCK')
Refresh3.update({'KEY' : KEY})

window=Tk()
window.title("PC LOCK")
window.geometry("3840x1080+-1920+2")
window.resizable(False, False)
window.overrideredirect(True)
img = Image.open('wallpaper.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(window, image=bg)
label.place(x = -2,y = -2)
fontExample = tkinter.font.Font(family="AppleSDGothicNeoEB00", size=20)
window.wm_attributes("-topmost", 1)
label3=tkinter.Label(window, text="엄마한테 풀어달라하던가 아니면 비번을 맞추던가 ㅋㅋㄹㅃㅃ",font=fontExample)
label3.place(x=2545,y=500,width=670,height=40)

def btnpress():
    if ent.get() == str(KEY):
        sys.exit()
    else:
        label3.config(text="응 아니야~")

ent = Entry(window)
ent.config(relief="solid",borderwidth="0",font=fontExample)
ent.place(x=2700, y=600, width=300,height=40)

btn = Button(window, command=btnpress)
btn.config(text= "풀기",relief="solid",borderwidth="0",font=fontExample)
btn.place(x=3010, y=600 , width=50,height=40 )

window.mainloop()