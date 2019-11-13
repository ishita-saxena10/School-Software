from tkinter import *
import mysql.connector

top=Tk()
top.geometry("1600x800")
'''def f():
    top.destroy()
    import fee2pg'''
def sub():
    a=str(e2.get())
    b=str(e3.get())
    c=str(e4.get())

    
    conn=mysql.connector.connect(user="root",password="",host="localhost",db="school")
    cursor=conn.cursor()
    cursor.execute("insert into fee(N,C,EA) values('"+a+"','"+b+"','"+c+"')")
   
    conn.commit()
    top.destroy()
    import fees

l1=Label(top,text="PAY FEES",font=("arial",70,"bold","underline"),fg="blue",bg="white")
l1.place(x=220,y=100)
l2=Label(top,text="NAME",font=("arial",20),fg="blue",bg="white")
l2.place(x=100,y=250)
e2=Entry(top,bd=8,font=("arial",20))
e2.place(x=330,y=250)
l3=Label(top,text="CLASS",font=("arial",20),fg="blue",bg="white")
l3.place(x=100,y=300)
e3=Entry(top,bd=8,font=("arial",20))
e3.place(x=330,y=300)
l4=Label(top,text="ENTER AMOUNT",font=("arial",20),fg="blue",bg="white")
l4.place(x=100,y=400)
e4=Entry(top,bd=8,font=("arial",20))
e4.place(x=330,y=400)
b1=Button(top,text="PROCEED",command=sub,font=("arial",20),fg="blue",bg="white")
b1.place(x=150,y=470)
top.mainloop()
