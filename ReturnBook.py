from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
def Return():
    bid=bookInfo.get()
    bookTable = "books"
    issueTable = "books_issued"
    allbid=[]
    query1='select bid from '+issueTable
    try:
        cur.execute(query1)
        con.commit()
        for i in cur:
            allbid.append(i[0])
        if bid in allbid:
            query2='select status from '+bookTable+' where bid='+bid
            cur.execute(query2)
            con.commit()
            for i in cur:
                check=i[0]
            if check=='issued':
                status=True
            else:
                status=False
        else:
            messagebox.showinfo("No Bid",'Present')
    except:
        messagebox.showinfo("Failed")
    query3='delete from '+issueTable+' where bid='+bid
    query4="update "+bookTable+" set status = 'avail' where bid = '"+bid+"'"
    try:
        if bid in allbid and status==True:
            cur.execute(query3)
            con.commit()
            cur.execute(query4)
            con.commit()
            messagebox.showinfo("Returned",'succesfully')
            root.destroy()
        else:
            allbid.clear()
            messagebox.showinfo("Already","Available")
    except:
        messagebox.showinfo("Error")
    allbid.clear()
def returnBook():
    global con,cur,bookInfo,root,status
    con = mysql.connector.connect ( host='localhost',
                                    port='3306',
                                    user='root',
                                    password='1234',
                                    database='kowshik'
                                    )

    cur = con.cursor ( buffered=True )
    root = Tk ()
    root.title ( "Library" )
    root.minsize ( width=400, height=400 )
    root.geometry ( "600x500" )

    Canvas1 = Canvas ( root )
    Canvas1.config ( bg="#006B38" )
    Canvas1.pack ( expand=True, fill=BOTH )

    headingFrame1 = Frame ( root, bg="#00FFFF", bd=5 )
    headingFrame1.place ( relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13 )

    headingLabel = Label ( headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier', 15) )

    headingLabel.place ( relx=0, rely=0, relwidth=1, relheight=1 )
    labelFrame = Frame ( root, bg='black' )
    labelFrame.place ( relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5 )
    label2 = Label ( labelFrame, text="Book ID :", bg='black', fg='white' )
    label2.place ( relx=0.05, rely=0.5 )
    bookInfo = Entry ( labelFrame )
    bookInfo.place ( relx=0.3, rely=0.5, relwidth=0.62 )
    # submit Button
    SubmitBtn = Button ( root, text="RETURN", bg='#d1ccc0', fg='black',command=Return )
    SubmitBtn.place ( relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08 )

    quitBtn = Button ( root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy )
    quitBtn.place ( relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    root.mainloop()
