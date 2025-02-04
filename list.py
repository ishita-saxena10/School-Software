from tkinter import *
import mysql.connector
import tkinter.ttk as ttk
conn=mysql.connector.connect(user="root",password="",host="localhost",db="school")
cursor=conn.cursor()

def showall():
    global tree
    tree.delete(*tree.get_children())
    tree.heading('NAME',text="NAME",anchor=W)
    tree.heading('CLASS',text="CLASS",anchor=W)
    tree.heading('PHONE_NO',text="PHONE_NO",anchor=W)
    tree.column('#0',stretch=NO,minwidth=0,width=100)
    tree.column('#1',stretch=NO,minwidth=0,width=100)
    tree.column('#2',stretch=NO,minwidth=0,width=200)

    tree.pack()
    cursor.execute("select * from admisssion")
    f=cursor.fetchall()

    for data in f:
        tree.insert('','end',values=(data))

top=Tk()
top.geometry("1600x800+0+0")
top.config(background="PeachPuff")

def ser(x):
    global tree
    tree.delete(*tree.get_children())
   
    tree.heading('NAME', text="NAME",anchor=W)
    tree.heading('CLASS', text="CLASS",anchor=W)
    tree.heading('PHONE_NO', text="PHONE_NO",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=100)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=200)


    tree.pack()
    cursor.execute("select * from admisssion where name like '"+x+"%'")
    f =cursor.fetchall()
    #fetch=[2,3,4,6,7,8,9]
    for data in f:
        tree.insert('', 'end', values=(data))
first=Frame(top, width=2400,height=100,bg="PeachPuff")
first.pack(side="top")
Label(first,text="***ADMISSION***",fg="navyblue",bg="PeachPuff",font=("comic sans MS",50,"bold")).place(x=380,y=5)

second=Frame(top, width=2400,height=100,bg="Bisque")
second.pack(side="top")





Label(top,text="Search",bg="Bisque",fg="navyblue",font=("comic sans MS",30)).place(x=390,y=110)
e1=Entry(top,font=("comic sans MS",15),bd=2,fg="navyblue",bg="PeachPuff")
e1.place(x=550,y=130)
Button(top,text="Search", bd=4, fg= "grey", font= ('comic sans MS',10,'bold'),bg="PeachPuff",command=lambda:ser(e1.get())).place(x=850,y=130)
Button(top,text="ShowAll", bd=4, fg= "grey", font= ('comic sans MS',10,'bold'),bg="PeachPuff",command=showall).place(x=950,y=130)


MidViewForm = Frame(top, width=400)
MidViewForm.pack()
global tree

###SCROLLBAR
scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
tree = ttk.Treeview(MidViewForm, columns=("NAME","CLASS","PHONE_NO"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)    
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
showall()

top.mainloop()    
        
