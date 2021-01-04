import time
import os
import json

FILENAME = "./data/library.json"

def choices():
    print("1.To Display the books of library")
    print("2.To Lend books from Library")
    print("3.To add books on Library")
    print("4.To return the books")
    print("5.Exit")   

class Library:

    def __init__(self):
        pass    
        
    def __name(self):
        print("----------Welcome To the Library Manager-------------\n")
        print("Do You already have a library If you do please Type its Name Type The Library: ")
        name = input("")

        return name

    def __temp(self):
        with open(FILENAME,'r') as f:
            temp = json.load(f)
        return temp

    def has_library(self):
        global name

        name = self.__name()
        temp = self.__temp()

        for entry in temp:
            if name == entry['libraryname']:
                return True       

    def open_library(self):
        pass
       


    def display_books(self):
        temp = self.__temp()

        for entry in temp:
            if name == entry['libraryname']:
                books_list = entry['availablebooks']
      
      # TODO: UNIQ: use this books_list and display it in good way ofc
        for book in books_list :
            print(book.rjust(30,' '))
    def lend_books(self):
        pass


    def add_books(self):
        pass


    def return_book(self):
        pass


library1 = Library()

if library1.has_library():
    #choices()
    library1.display_books()

else:
    open_library()




