from tkinter import *
#from PIL import ImageTk,Image #PIL -> Pillow
import mysql.connector
from AddBook import *
from Viewbooks import *
from DeletBooks import *
from IssueBook import *
from ReturnBook import *
con=mysql.connector.connect(host='localhost',port='3306',user='root',password='1234',database='kowshik')
cur=con.cursor()
cur.execute('select * from books')
root=Tk()
root.title('LIBRARY')
root.minsize(width=400,height=400)
root.geometry("600x500")
same = True
n = 0.25

# Adding a background image
background_image = Image.open (r"C:\Users\Kowshik\Desktop\library.webp")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int ( imageSizeWidth )+550
if same:
    newImageSizeHeight = int ( imageSizeHeight)
else:
    newImageSizeHeight = int ( imageSizeHeight/n)

background_image = background_image.resize ( (newImageSizeWidth, newImageSizeHeight))
img = ImageTk.PhotoImage ( background_image )
Canvas1 = Canvas ( root )
Canvas1.create_image ( 300, 340, image=img )
Canvas1.config ( bg="white", width=newImageSizeWidth, height=newImageSizeHeight )
Canvas1.pack ( expand=True, fill=BOTH )
headingFrame1 = Frame(root,bg="#00FFFF",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n My Library", bg='black', fg='white', font=('Times New Roman',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
btn1 = Button ( root, text="Add Book Details", bg='black', fg='white',command=addbook)
btn1.place ( relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1 )
btn2 = Button ( root, text="Delete Book", bg='black', fg='white',command=delete)
btn2.place ( relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1 )

btn3 = Button ( root, text="View Book List", bg='black', fg='white',command=View)
btn3.place ( relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1 )

btn4 = Button ( root, text="Issue Book to Student", bg='black', fg='white',command=issueBook)
btn4.place ( relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1 )

btn5 = Button ( root, text="Return Book", bg='black', fg='white',command=returnBook)
btn5.place ( relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop()



