from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
def bookRegister():
    bid=bookInfo1.get()
    Title=bookInfo2.get()
    Author=bookInfo3.get()
    Status=bookInfo4.get()
    table='books'
    insertBooks = "insert into "+table+" values ('"+bid+"','"+Title+"','"+Author+"','"+Status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
        root.destroy()
    except:
        messagebox.showinfo ( "Error", "Can't add data into Database")
def addbook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur,root
    root=Tk()
    root.title ( "Library" )
    root.minsize ( width=400, height=400 )
    root.geometry ( "600x500" )
    con = mysql.connector.connect ( host='localhost',
                                    port='3306',
                                    user='root',
                                    password='1234',
                                    database='kowshik'
                                    )
    cur = con.cursor ()
    Canvas1 = Canvas ( root )
    Canvas1.config ( bg="#ff6e40" )
    Canvas1.pack ( expand=True, fill=BOTH )
    HeadingFrame1=Frame(root,bd=5,bg="#00FFFF")
    HeadingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    label1=Label(HeadingFrame1,text="Add Books",bg='black',fg='white',font=('Times New Roman',15))
    label1.place ( relx=0, rely=0, relwidth=1, relheight=1 )
    labelFrame = Frame ( root, bg='black' )
    labelFrame.place ( relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4 )
    lb1=Label(labelFrame,text='Book Id:',bg='black',fg='white',font=('Times New Roman',10))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
    bookInfo1=Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
    lb2=Label(labelFrame,text='Title:',fg='white',bg='black',font=('Times New Roman',10))
    lb2.place (relx=0.05,rely=0.35, relheight=0.08)
    bookInfo2=Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
    lb3=Label(labelFrame,text='Author:',bg='black',fg='white',font=('Times New Roman',10))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
    bookInfo3=Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
    lb4=Label(labelFrame,text='Status(Avail/Issued):',fg='white',bg='black',font=('Times New Roman',10))
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
    bookInfo4=Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
    #submit Button
    SubmitBtn = Button ( root, text="SUBMIT", bg='#d1ccc0', fg='black', command=bookRegister)
    SubmitBtn.place ( relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08 )

    quitBtn = Button ( root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy )
    quitBtn.place ( relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08 )
    root.mainloop ()

