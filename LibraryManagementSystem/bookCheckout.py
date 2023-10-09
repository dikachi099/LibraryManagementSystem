#STUDENT ID:F230776
from  database import *
from datetime import date


def book_checkout(Book_id,Member_id):
    loan()
    for l in loanrecords:
        if Book_id in l[0] and int(Member_id)>=1000 and int(Member_id)<=9999:#checks that the member id and book id inputed is valid 
             if l[4]=="0" and l[2]=="":
                 return 1
             elif l[2]!="" and l[4]=="0":
                print("sorry book is currently reserved")#prints a message to show that the book the person wishes to checkout is reserved by someone and it is currently being loaned
                return 2
             else:
                  print("you have successfully checked book out")#prints a message when the book is avaiable and has been checked out successfully
                  
                  update_checkout(Book_id,Member_id)#the date that the book was checked out is appended to the logfile
                  return 3

    else:
        print("invalid input")#prints an error message if the book id or member id entered isn't valid
        return 4
        
           
def reserve_book(Book_id,Member_id):
    
    for l in loanrecords :
        if l[0] == Book_id:
            today=date.today()
            l[2]=today.strftime("%d/%m/%Y")
            update_reservation(Book_id,Member_id)
            return True
            
        

#testing the functionality of this python module
"""
if __name__=="main":
    print(book_checkout("1",5003))
    print(book_checkout("200",4001))
    print(book_checkout("20",99))
    print(book_checkout("3",5001))
    print(book_checkout("7",5010))
"""



