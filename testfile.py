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
        print("Do You already have a library If you do please Type its Name Else just type n: ")
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
        temp = self.__temp()

        for entry in temp:
            if name == entry['libraryname']:
                books_list = entry['availablebooks']
        return books_list

library1 = Library()

if library1.has_library():
    print(library1.open_library())

else:
    open_library() 