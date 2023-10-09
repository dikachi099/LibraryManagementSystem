#STUDENT ID:F230776#STUDENT ID:F230776
from database import *
records()
loan()


def most_poplular_book():
    popular_id="no books"
    popularcount=0
    checked=[]

    for r in bookrecords:

        if r[2] not in checked:

##            print(r[2],"    ID:", r[0])
            currentcount=0
            currentbook=r[2]
            for y in loanrecords:
##                print(y[0])
                samebook = False
                for x in bookrecords:
                    if (x[2]==r[2]) and (y[0] == x[0]):
                        samebook=True
                        break
                    
##                print(samebook)
                if r[0]==y[0] or samebook == True:
                    currentcount=currentcount+1
##                print("count = ",currentcount)
            checked.append(r[2])
            if currentcount>popularcount:
                popular_id=r[2]
                popularcount=currentcount
    return popular_id
    
    
            
##print(most_poplular_book())




