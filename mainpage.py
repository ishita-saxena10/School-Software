from tkinter import *

top=Tk()
top.config(background="chocolate1")
top.geometry("1600x800")

def admm():
    top.destroy()
    import admisssion
def far():
    top.destroy()
    import facr
def fee():
    top.destroy()
    import fees
def login():
    top.destroy
    import  LOGINPG1
def adst():
    top.destroy
    import list
    
l1=Label(top,font=("arial",70,"bold","underline"),text="ST.PAUL'S SCHOOL",fg="black",bg="chocolate1")
l1.place(x=220,y=100)

b1=Button(top,text="ADMISSION",command=admm,fg="black",bd=8,bg="white",font=("arial",30)).place(x=500,y=300)
b2=Button(top,text="FACULTY RECRUITMENT",command=far,bd=8,fg="black",bg="white",font=("arial",30)).place(x=500,y=400)
b3=Button(top,text="PAY FEES",command=fee,fg="black",bd=8,bg="white",font=("arial",30)).place(x=500,y=500)
b4=Button(top,text="LOGIN",command=login,fg="black",bd=8,bg="white",font=("arial",30)).place(x=500,y=600)
b5=Button(top,text="ADMITTED STUDENTS",command=adst,fg="black",bd=8,bg="white",font=("arial",30)).place(x=500,y=700)
top.mainloop()
