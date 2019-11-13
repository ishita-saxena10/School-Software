from tkinter import *
import mysql.connector
from tkinter import messagebox

top=Tk()
top.geometry("1600x800")
'''def lgn():
    top.destroy()
    import wlcm'''
def sub():
    conn=mysql.connector.connect(host="localhost",user="root",password="",db="school")
    cursor=conn.cursor()
    cursor.execute("select * from facrec where N='"+e2.get()+"' and EI='"+e3.get()+"'")
    if(cursor.fetchone()):
                   top.destroy()
                   import wlcm
    elif(e2.get()=="" or e3.get()==""):
                   messagebox.showinfo("empty")
    else:
                   messagebox.showinfo("please sign in")


l1=Label(top,text="FACULTY LOGIN",fg="blue",bg="white",font=("arial",30))
l1.place(x=500,y=100)

l2=Label(top,text="NAME",fg="blue",bg="white",font=("arial",30))
l2.place(x=150,y=300)
e2=Entry(top,fg="blue",bg="white",font=("arial",30))
e2.place(x=350,y=300)
l3=Label(top,text="EMAIL ID",bg="white",fg="blue",font=("arial",30))
l3.place(x=150,y=350)
e3=Entry(top,fg="blue",bg="white",font=("arial",30))
e3.place(x=350,y=350)

b1=Button(top,text="LOGIN",command=sub,fg="blue",bg="white",font=("arial",30))
b1.place(x=400,y=450)

top.mainloop()

