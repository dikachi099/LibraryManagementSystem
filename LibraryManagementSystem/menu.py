#STUDENT ID:F230776
from tkinter import *
from database import *
from bookSearch import *
from bookReturn import *
from bookCheckout import *
from bookSelect import*
import time



def say_welcome():
    print("Welcome")

def say_Bye():
    print("Close")
    


def getBook():
    lstSearch.delete(0,END)
    title=txtsearch.get()
    record=book_search(title)
    for i in range (0,len(record)):
        lstSearch.insert(i,record[i])


    
def returns():
    lstSearch.delete(0,END)
    Book_id=txtreturn.get()
    record=book_return(Book_id)
    if record==True:
        lstSearch.insert(0,"you have returned book")
    else:
        lstSearch.insert(0,"input not valid")



def check_out():
    lstSearch.delete(0,END)
    Book_id=txtcheckout_bookid.get()
    Member_id=txtcheckout_memberid.get()
    record=book_checkout(Book_id,Member_id)
    if record==1:
        lstSearch.insert(0,"book is loan out. type Y in reservation text field to reserve")
        btnreserve.wait_variable(reserveButtonClicked)
        
        option=txtreserve.get()
        if option == "Y" or option == "Yes":
            reserve_book(Book_id,Member_id)
            lstSearch.insert(0,"Book has been reserved")
    elif record==2:
        lstSearch.insert(0,"sorry book is currently reserved")
    elif record==3:
        lstSearch.insert(0,"you have successfully checked book out")
    else:
      lstSearch.insert(0,"input not valid")
      

    
    


window=Tk()
window.title("Library Main Menu")
window.geometry("800x300")

reserveButtonClicked = StringVar()

# Create GUI components
btnWelcome=Button(window,text="Welcome",command=say_welcome)
btnBye=Button(window,text="Close",command=say_Bye)

btnsearch=Button(window,text="Search Book",command=getBook)
txtsearch=Entry(window,width=10)
txtcheckout_bookid=Entry(window,width=5)
txtcheckout_memberid=Entry(window,width=5)


lstSearch=Listbox(window, width='30')
btncheckout=Button(window,text="Checkout Book",command=check_out)
btnreturn=Button(window,text="Return Book",command=returns)
txtreturn=Entry(window,width=5)
lblTitle=Label(window,text="Title")
lblcheckout_1=Label(window,text="Book ID")
lblcheckout_2=Label(window,text="Member ID")
lblreturn=Label(window,text="Book ID")
lblreserve=Label(window,text="Type Y to reserve book,N for otherwise")
txtreserve=Entry(window,width=5)
btnreserve=Button(window,text="Reserve Book", command=lambda: reserveButtonClicked.set("button pressed"))
btnselect=Button(window,text="Select Book")



# Defining location of the component
btnWelcome.grid(column=0,row=0)

btnsearch.grid(column=0,row=3)
txtsearch.grid(column=1,row=3)
lblTitle.grid(column=1,row=2)

btncheckout.grid(column=0,row=5)
lblcheckout_1.grid(column=1,row=4)
lblcheckout_2.grid(column=2,row=4)
txtcheckout_bookid.grid(column=1,row=5)
txtcheckout_memberid.grid(column=2,row=5)

btnreturn.grid(column=0,row=14)
txtreturn.grid(column=1,row=14)
lblreturn.grid(column=1,row=12)
lblreserve.grid(column=0,row=11)
txtreserve.grid(column=1,row=11)
btnreserve.grid(column=2,row=11)
btnselect.grid(column=0,row=13)
btnBye.grid(column=0,row=15)
lstSearch.grid(column=50,row=0,rowspan=200)



window.mainloop()



    
