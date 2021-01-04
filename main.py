import time
import os

def choices():
    print("1.To Display the books of library")
    print("2.To Lend books from Library")
    print("3.To add books on Library")
    print("4.To return the books")
    print("Type anything else to quit")
   


class Library:

    def __init__(self, listofbooks):
        self.listofbooks = listofbooks

    def has_library():
        print("----------Welcome To the Library Manager-------------\n")
        print("Do You already have a library If you do please Type its Name Else just type n: ")

    def open_library():
        


    def display_books(self):
        pass

    def lend_books(self):
        pass


    def add_books(self):
        pass


    def return_book(self):
        pass



library1 = Library(userlist)

choices()

choice = input()

if choice == '1':
    library1.display_books()

elif choice == '2':
    library1.lend_books()

elif choice == '3':
    library1.add_books()

elif choice == '4':
    library1.return_book()

else:
    quit()



