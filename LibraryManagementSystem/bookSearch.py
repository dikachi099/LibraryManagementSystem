#STUDENT ID:F230776
from database import*

    

def book_search(title):
    """
    title is the input parameter

    the first letter of the title should be a capital letter

    """
    records=[]
    for books in bookrecords:
        if books[2]==title:
            records.append(books)
    return records
 
records()

##print(book_search("Book_2"))


"""
if __name__ == "__main__":
    print(book_search("Book_1"))
    print(book_search("Book_60"))
"""
