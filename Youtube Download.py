from pytube import YouTube
from tkinter import *

root=Tk()

root.geometry("500x400")
root.title("Youtube video download")

def youtube():
    a=var.get() #https://www.youtube.com/watch?v=aEDu2oKOWzE&feature=emb_imp_woyt
    ytvideo = YouTube(a).streams.filter(progressive=True,file_extension="mp4").order_by('resolution').desc().first()
    
    ytvideo.download(r"C:\Users\Amartya\Downloads")
    print("Entry box",a)

l1=Label(root,text="YouTube video link",fg="Red",font="Bold")
l1.place(x=30,y=20)

var=StringVar()
e1=Entry(root,textvariable=var,width=60)
e1.place(x=40,y=80)

b1=Button(root,text="Download",command=youtube,bg="green",width=20,fg="white")
b1.place(x=80,y=120)
root.mainloop()