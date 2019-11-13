from tkinter import *
import mysql.connector

top=Tk()
top.config(background="white")
top.geometry("1600x800")
def db():
    a=str(e2.get())
    b=str(e3.get())
    c=str(e4.get())
    d=str(e5.get())
    e=str(e6.get())
    f=str(e7.get())
    g=str(e8.get())
    h=str(e9.get())

    
    conn=mysql.connector.connect(user="root",password="",host="localhost",db="school")
    cursor=conn.cursor()
    cursor.execute("insert into facrec(N,Age,AFS,Q,EI,PN,A,E) values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"','"+h+"')")
   
    conn.commit()
    top.destroy()
    import wlcm
    
'''def fac():
    top.destroy()
    import fac2pg'''

l1=Label(top,font=("arial",70,"bold","underline"),text="FACULTY RECRUITMENT",fg="black",bg="white")
l1.place(x=300,y=180)
l2=Label(top,text="NAME",fg="black",bg="white",font=("arial",20))
l2.place(x=120,y=380)
e2=Entry(top,bd=8,font=("arial",20))
e2.place(x=500,y=380)
l3=Label(top,text="AGE",fg="black",bg="white",font=("arial",20))
l3.place(x=120,y=430)
e3=Entry(top,bd=8,font=("arial",20))
e3.place(x=500,y=430)
l4=Label(top,text="APPLYING FOR SUBJECT:",fg="black",bg="white",font=("arial",20))
l4.place(x=120,y=480)
e4=Entry(top,bd=8,font=("arial",20))
e4.place(x=500,y=480)
l5=Label(top,text="QUALIFICATION",fg="black",bg="white",font=("arial",20))
l5.place(x=120,y=530)
e5=Entry(top,bd=8,font=("arial",20))
e5.place(x=500,y=530)
l6=Label(top,text="EMAIL ID",fg="black",bg="white",font=("arial",20))
l6.place(x=120,y=580)
e6=Entry(top,bd=8,font=("arial",20))
e6.place(x=500,y=580)
l7=Label(top,text="PHONE NO.",fg="black",bg="white",font=("arial",20))
l7.place(x=120,y=630)
e7= Entry(top,bd=8,font=("arial",20))
e7.place(x=500,y=630)         
l8=Label(top,text="ADDRESS",fg="black",bg="white",font=("arial",20))
l8.place(x=120,y=680)
e8=Entry(top,bd=8,font=("arial",20))
e8.place(x=500,y=680)
l9=Label(top,text="EXPERIENCE",fg="black",bg="white",font=("arial",20))
l9.place(x=120,y=730)
e9=Entry(top,bd=8,font=("arial",20))
e9.place(x=500,y=730)
b1=Button(top,text="SUBMIT",command=db,bd=8,fg="black",bg="white",font=("arial",20))
b1.place(x=1200,y=520)

