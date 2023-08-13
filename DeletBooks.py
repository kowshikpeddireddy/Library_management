from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
def deletBook():
    bookTable = "books"
    issues_book = "books_issued"
    bid=bookInfo.get()
    delete1 = "delete from "+bookTable+" where bid = '"+bid+"'"
    #delete2 = "delete * from " + issues_book + "where bid=" + bid
    try:
        cur.execute(delete1)
        con.commit()
        #cur.execute(delete2)
        #con.commit()
        messagebox.showinfo("sucessfull","Book Deleted")
    except:
        messagebox.showinfo("Failed","To Delete")
    bookInfo.delete(0,END)
    root.destroy ()


def delete():
    global bookInfo,con,cur,root
    con = mysql.connector.connect ( host='localhost',
                                   port='3306',
                                   user='root',
                                   password='1234',
                                   database='kowshik'
                                   )

    cur = con.cursor ( buffered=True )
    # Enter Table Names here

    root = Tk ()
    root.title ( "Library" )
    root.minsize ( width=400, height=400 )
    root.geometry ( "600x500" )

    Canvas1 = Canvas ( root )
    Canvas1.config ( bg="#006B38" )
    Canvas1.pack ( expand=True, fill=BOTH )
    HeadingFrame1 = Frame ( root, bd=5, bg="#00FFFF" )
    HeadingFrame1.place ( relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16 )
    label1 = Label ( HeadingFrame1, text="Delete Book", bg='black', fg='white', font=('Times New Roman', 15) )
    label1.place ( relx=0, rely=0, relwidth=1, relheight=1)
    labelFrame = Frame ( root, bg='black' )
    labelFrame.place ( relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5 )
    label2=Label(labelFrame,text="Book ID :", bg='black', fg='white')
    label2.place ( relx=0.05, rely=0.5 )
    bookInfo=Entry(labelFrame)
    bookInfo.place ( relx=0.3, rely=0.5, relwidth=0.62 )
    # submit Button
    SubmitBtn = Button ( root, text="SUBMIT", bg='#d1ccc0', fg='black', command=deletBook )
    SubmitBtn.place ( relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08 )

    quitBtn = Button ( root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy )
    quitBtn.place ( relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08 )
    root.mainloop()