from tkinter import *

top=Tk()
top.config(background="black")
top.geometry("1600x800")

def stu():
    top.destroy()
    import loginpg1student
def fac():
    top.destroy()
    import LOGINPG1FACULTY


b1=Button(top,text="STUDENT LOGIN",command=stu,bg="black",fg="white",font=("arial",30))
b1.place(x=500,y=300)

b2=Button(top,text="FACULTY LOGIN",command=fac,bg="black",fg="white",font=("arial",30))
b2.place(x=500,y=400)

top.mainloop()
