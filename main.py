import time
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
        name = input("").lower()

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
        item_data['lentbooks'] = {}
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
        temp = self.__temp()
        new_temp = []

        for entry in temp:
            if name == entry['libraryname']:
                lentbooks = entry['lentbooks']
                availablebooks = entry['availablebooks']
                book = input("Which Book Do you want to lend: ").title()
                if book in lentbooks:
                    print(f"{book} has already been lent by {lentbooks[book]}")
                    new_temp.append(entry)
                elif book in availablebooks:
                    availablebooks.remove(book)
                    lentbooks[book] = input("Please Enter Your name to lend this book: ")
                    new_temp.append(entry)
                else:
                    print("Sorry This Book isnt available")
                    new_temp.append(entry)
            else:
                new_temp.append(entry)
        with open(FILENAME,'w') as f:
            json.dump(new_temp,f,indent=4)




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
                entry['availablebooks'] = books_list
                new_temp.append(entry)
            else:
                new_temp.append(entry)
        with open(FILENAME,'w') as f:
            json.dump(new_temp,f,indent=4)


    def return_book(self):
        temp = self.__temp()
        new_temp = []

        for entry in temp:
            if name == entry['libraryname']:
                lentbooks = entry['lentbooks']
                books_list = entry['availablebooks']
                book = input("Which book do u wish to return: ").title()
                if book in lentbooks:
                    print(f"Thanks for returning the book {lentbooks[book]}")
                    del lentbooks[book]
                    books_list.append(book)
                    new_temp.append(entry)
                else:
                    print("Sorry you havent lent the book to return")
                    new_temp.append(entry)

            else:
                new_temp.append(entry)

        with open(FILENAME,'w') as f:
            json.dump(new_temp,f,indent=4)
                


if __name__ == "__main__":
    library1 = Library()
    while True:
        if library1.has_library():
            while True:
                choices()
                choice = input("")
                if choice == "1":
                    library1.display_books()
                elif choice == "2":
                    library1.lend_books()
                elif choice == "3":
                    library1.add_books()
                elif choice == "4":
                    library1.return_book()
                elif choice == "5":
                    break
                else:
                    print("Wrong input please check the numbers agaain")

        else:
            print("You dont have a library Opening New library...")
            time.sleep(2.5)
            library1.open_library()






