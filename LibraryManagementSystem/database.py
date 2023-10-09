#STUDENT ID:F230776
from datetime import date

def borrow():
    
    f=open("logfile.txt","r")#opens the logfile for reading 
    for line in f:
        print(line)

    f.close()
    



bookrecords=[]
def records():
    bookrecords.clear()
    f=open("Book_info.txt","r")#opens the logfile for reading 
    for line in f:
        s=line.strip()
        records=s.split(":")
        bookrecords.append(records)
    f.close()

loanrecords=[]
def loan():
    loanrecords.clear()
    f=open("logfile.txt","r")
    for index in f:
        x=index.strip()
        loan=x.split(",")
        loanrecords.append(loan)
    f.close()



def updatelogfile():
    f=open("logfile.txt","w") 
    
    for record in loanrecords:
           newrecords=record[0]+","+record[1]+","+str(record[2])+","+record[3]+","+str(record[4])+"\n"
           f.write(newrecords)
    f.close()
           
           


def update_book_log(Book_id):
    for g in loanrecords:
        if g[0]==Book_id:
            today=date.today()
            g[4]==today
    updatelogfile()#updates the date in the logfile to today's date 


 
def update_checkout(Book_id,Member_id):
    
    f=open("logfile.txt","a")#opens the logfile for appending 
    currentDate = date.today();
    today=currentDate.strftime("%d/%m/%Y")
    f.write(str(Book_id)+","+str(Member_id)+","+""+ "," + str(today)+ ",0"+"\n")
    f.close()

def update_reservation(Book_id,Member_id):
    for g in loanrecords:
        
        if g[0]==Book_id and g[1]== Member_id:
            today=date.today()
            g[2]==today
    
    updatelogfile()#updates the date in the logfile to today's date 
