from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
def issue():
    bid=info1.get()
    name=info2.get()
    bookTable = "books"
    issueTable = "books_issued"
    allbid=[]
    query1='select bid from '+bookTable
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
            if check=='avail':
                status=True
            else:
                status=False
        else:
            messagebox.showinfo('No','Bid Present')
    except:
        messagebox.showinfo('Failed','To Fetch')
    query3="insert into "+issueTable+" values ('"+bid+"','"+name+"')"
    query4="update "+bookTable+" set status = 'issued' where bid = '"+bid+"'"
    try:
        if bid in allbid and status==True:
            cur.execute(query3)
            con.commit()
            cur.execute(query4)
            con.commit()
            messagebox.showinfo("successful",'issued')
            root.destroy()
        else:
            allbid.clear()
            messagebox.showinfo("Already","Issued")
            root.destroy()
    except:
        messagebox.showinfo("Failed")
    allbid.clear()



def issueBook():
    global root,cur,con,info1,info2,status,check
    root = Tk ()
    root.title ( "Library" )
    root.minsize ( width=400, height=400 )
    root.geometry ( "600x500" )
    con = mysql.connector.connect ( host='localhost',
                                    port='3306',
                                    user='root',
                                    password='1234',
                                    database='kowshik'
                                    )
    cur = con.cursor ( buffered=True )
    Canvas1 = Canvas ( root )
    Canvas1.config ( bg="#FFB6C1" )
    Canvas1.pack ( expand=True, fill=BOTH )
    headingFrame1 = Frame ( root, bg="#00FFFF", bd=5 )
    headingFrame1.place ( relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13 )

    headingLabel = Label ( headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15) )

    headingLabel.place ( relx=0, rely=0, relwidth=1, relheight=1 )
    labelFrame = Frame ( root, bg='black' )
    labelFrame.place ( relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5 )
    lb1=Label(labelFrame,text='Book Id :',bg="black",fg='white',font=('Courier', 10))
    lb1.place(relx=0.05,rely=0.2)
    info1=Entry(labelFrame)
    info1.place(relx=0.3,rely=0.2, relwidth=0.62)
    lb2=Label(labelFrame,text="Issued To :",fg='white',bg='black',font=('Courier', 10))
    lb2.place(relx=0.05,rely=0.4)
    info2=Entry(labelFrame)
    info2.place(relx=0.3,rely=0.4, relwidth=0.62)
    # submit Button
    SubmitBtn = Button ( root, text="SUBMIT", bg='#d1ccc0', fg='black', command=issue)
    SubmitBtn.place ( relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08 )

    quitBtn = Button ( root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy )
    quitBtn.place ( relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08 )
    root.mainloop()
