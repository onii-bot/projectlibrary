import time
import os
userlist=[]

print("----------Welcome To the Library Manager-------------\n")
print("1.If you already have library")
print("2.If you want to create a new library")
answr = input()

if answr == '1':
    name = input("Type the name of library: ")
    try:
        fhand = open(name+'.txt','r')
        for nameofbook in fhand:
            striipe_name = nameofbook.strip()
            if striipe_name == "": continue
            userlist.append(striipe_name)
        print("Opened Sucessfully")

    except:
        print("No such library is found")
        print("qutting now..")
        time.sleep(2)
        quit()


elif answr == '2':
    print("What would you like to Name your library: ")
    name = input()

    print(f"Your {name} Library is created successfully..\n")

    print("Now we need to add books")
    print("1.If you have the text file with name of books")
    print("2.If you wish to add list here")

    answer = input()

    if answer == '1':
        filename = input("Enter the name of txt file inculding full path: ")
        try:
            fhand = open(filename, 'r')
            for bookname in fhand:
                stripped_line = bookname.strip()
                if stripped_line == "":continue
                userlist.append(stripped_line)
            fhand.close()
        except:
            print("No such text file is found")
            print("Exiting now....")
            time.sleep(2)
            quit()
    elif answer == '2':
        fhand = open(name + ".txt", 'w')
        print("Keep typing name of book and type stop to quit adding books")
        while True:
            bookname = input("Name of Book: ")
            if bookname == "stop":
                fhand.close()
                break
            userlist.append(bookname)
            fhand.write('\n'+str(bookname)+'\n')
else:
    print('No such number is listed')
    print("Exiting..")
    time.sleep(1.5)
    quit()
try:
    dictionary_of_lent_books = {}
    fhand = open(name+'dict'+'.txt','r')
    for lineg in fhand:
        strippee = lineg.rstrip()
        if strippee == "" : continue
        listline = strippee.split(':')
        dictionary_of_lent_books[listline[0]] = listline[1]
    fhand.close()

except Exception as e:
    dictionary_of_lent_books = {}


class Library:
    def __init__(self, listofbooks):
        self.listofbooks = listofbooks

    def display_books(self):
        for booke in self.listofbooks:
            print(booke)
        print("These are the books available in the library")
        time.sleep(15)

    def lend_books(self):
        while True:
            namej = input("Please enter your name: ")
            book = input("Please enter the name of book you want to lend: ")
            if book not in self.listofbooks:
                print("The book is not on Library")
                print("Please check the books first before acquiring it")
                time.sleep(10)
                quit()


            if book in dictionary_of_lent_books:
                print(f"You cant take the book beacuse it is currently with {dictionary_of_lent_books[book]}")
            elif book not in dictionary_of_lent_books:
                dictionary_of_lent_books[book] = name
                fhand2 = open(name+'dict'+'.txt','a')
                fhand2.write('\n'+book+":"+namej+"\n")
                print("Book successfully acquired!! ")

            quitornot2 = input("Press y if you wish to lend book again: ")
            if quitornot2 == 'y':
                continue
            else:
                break


    def add_books(self):
        print("Opening Book adding..")
        time.sleep(1.5)
        print("Type here to add Book")
        print("Type stop when you want to close Book adder")
        fhand3 = open(name+'.txt','a')
        while True:
            booknametoadd = input("Bookname: ")
            if booknametoadd == "stop":
                fhand3.close()
                break
            userlist.append(booknametoadd)
            fhand3.write(str('\n'+ booknametoadd) + '\n')



    def return_book(self):
        os.remove(name+'dict'+'.txt')
        namep = input("Please enter your name: ")
        book2 = input("Please enter the name of book you want to return: ")

        if dictionary_of_lent_books[book2] == namep:
            del dictionary_of_lent_books[book2]

            fhanddd = open(name + 'dict' + '.txt', 'a')

            for value in dictionary_of_lent_books:
                fhanddd.write(str(value)+':'+str(dictionary_of_lent_books[value]))


print("1.To Display the books of library")
print("2.To Lend books from Library")
print("3.To add books on Library")
print("4.To return the books")
print("Type anything else to quit")
library1 = Library(userlist)
answa = input()

if answa == '1':
    library1.display_books()

elif answa == '2':
    library1.lend_books()

elif answa == '3':
    library1.add_books()

elif answa == '4':
    library1.return_book()

else:
    quit()



