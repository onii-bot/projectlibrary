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
        print("Type the name of the library If the name is already registered it will open else new will be created ")
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
        item_data = {}
        temp = self.__temp()
        item_data['libraryname'] = name.lower()
        item_data['ownername'] = input("Name of the owner: ").lower()
        books_list = []
        while True:
            book = input("Keep adding books you have and type done to stop: ").title()
            if book == "Done":
                break
            else:
                books_list.append(book)
        item_data['availablebooks'] = books_list
        temp.append(item_data)
        with open(FILENAME,'w') as f:
            json.dump(temp,f,indent=4)

       


    def display_books(self):
        temp = self.__temp()

        for entry in temp:
            if name == entry['libraryname']:
                books_list = entry['availablebooks']
      
        for book in books_list :
            print(book)


    def lend_books(self):
        pass


    def add_books(self):
        temp = self.__temp()
        new_temp = []

        for entry in temp:
            if name == entry['libraryname']:
                books_list = entry['availablebooks']
                new_books = []
                while True:
                    book = input("Keep adding books you have and type done to stop: ").title()
                    if book == "Done":
                        break
                    else:
                        new_books.append(book)
                books_list = books_list + new_books
                with open()
            else:
                new_temp.append(entry)




    def return_book(self):
        pass


library1 = Library()

if library1.has_library():
    #choices()
    pass

else:
    library1.open_library()




