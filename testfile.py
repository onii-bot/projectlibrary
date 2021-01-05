import json
FILENAME = "./data/library.json"

def __temp():
    with open(FILENAME,'r') as f:
        temp = json.load(f)
    return temp

def __name():
    print("----------Welcome To the Library Manager-------------\n")
    print("Type the name of the library If the name is already registered it will open else new will be created ")
    name = input("")

    return name

def has_library():
    global name

    name = __name()
    temp = __temp()

    for entry in temp:
        if name == entry['libraryname']:
            return True

def add_books():
    temp = __temp()
    has_library()
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

add_books()