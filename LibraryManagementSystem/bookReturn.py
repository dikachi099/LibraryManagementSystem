#STUDENT ID:F230776#STUDENT ID:F230776
from database import *

import datetime 

def book_return(Book_id):
##    loan()
    for r in loanrecords:
        
        if r[0]==Book_id and r[4]=="0" and r[2]=="":
            
            print("you have successfully returned this book")#print this message if the book was previously loaned
            today=date.today()
            r[4]=today.strftime("%d/%m/%Y")
##            print(loanrecords)
            updatelogfile() # the log file is updated and today's date appended.
            
            return True
            break
          
        elif r[2]!="" and r[4]=="0" and r[0]==Book_id:
            """

            This is a case where the book has been reserved before it was returned
            in this case it prints out a message when the book is returned to inform the
            librarian that someone is going to check the book out soon
            """
            print("you have successfully returned this book,book has been reserved by a member")#prints this message to inform the librarian
            today=date.today()
            r[4]=today.strftime("%d/%m/%Y")
            updatelogfile() #The log file is updated and today's date is appended 
            return True
            break


    else:
        return False
            
    
  
    
loan()        



##book_return("1")


#testing the functionality of this python module
if __name__=="__main__":
    print(book_return("3"))#this is when the book is being returned and hasn't been reserved
    print(book_return("12"))#this is when the book is being returned and has been reserved



