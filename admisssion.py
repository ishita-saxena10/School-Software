from tkinter import *
from tkinter import messagebox
import mysql.connector

top=Tk()
top.config(background="yellow")

def sub():
    a=str(e2.get())
    b=str(e3.get())
    c=str(e4.get())
    d=str(e5.get())
    e=str(e6.get())
    f=str(e7.get())

    
    conn=mysql.connector.connect(user="root",password="",host="localhost",db="school")
    cursor=conn.cursor()
    cursor.execute("insert into admisssion(NAME,CLASS,PHONE_NO,FN,MOTHERS_NAME,EMAIL_ID) values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"')")
   
    conn.commit()
    top.destroy()
    import admisssion

top.geometry("1600x800")
'''def ad():
    top.destroy()
    import adm2pg'''

img=PhotoImage(file="E:/python examples/school tkinter/ap.png")
Label(top,image=img).place(x=1000,y=10)
l1=Label(top,font=("colonna mt",70,"underline"),text="ADMISSION",fg="blue",bg="yellow")
l1.place(x=300,y=50)
l2=Label(top,text="NAME",fg="blue",bg="yellow",font=("arial",30))
l2.place(x=120,y=200)
e2=Entry(top,bd=8,font=("arial",30))
e2.place(x=490,y=200)
l3=Label(top,text="CLASS",fg="blue",bg="yellow",font=("arial",30))
l3.place(x=120,y=300)
e3=Entry(top,bd=8,font=("arial",30))
e3.place(x=490,y=300)
l4=Label(top,text="PHONE NO",fg="blue",bg="yellow",font=("arial",30))
l4.place(x=120,y=400)
e4=Entry(top,bd=8,font=("arial",30))
e4.place(x=490,y=400)
l5=Label(top,text="FATHER'S NAME",fg="blue",bg="yellow",font=("arial",30))
l5.place(x=120,y=500)
e5=Entry(top,bd=8,font=("arial",30))
e5.place(x=490,y=500)
l6=Label(top,text="MOTHER'SNAME",fg="blue",bg="yellow",font=("arial",30))
l6.place(x=120,y=600)
e6=Entry(top,bd=8,font=("arial",30))
e6.place(x=490,y=600)
l7=Label(top,text="EMAILID",fg="blue",bg="yellow",font=("arial",30))
l7.place(x=120,y=700)
e7=Entry(top,bd=8,font=("arial",30))
e7.place(x=490,y=700)
b1=Button(top,text="SUBMIT",bd=8,font=("arial",30),command=sub)
b1.place(x=1200,y=600)

top.mainloop()



