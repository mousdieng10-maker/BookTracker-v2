import readfile
import random


def random_book(lib):
    options = [1,2]
    data = readfile.read("randomlib.json")
    book = random.choice(data)
    for details in book:
        print(book[details])
    while True:
        try:
            add = int(input("add to library(1) or no(2)?: "))
            if add in options:
                break
            else:
                print("Select a valid option")
        except ValueError:
            print("Select a valid option")
    if add == 1:
        lib.append(book)
    else:
        pass
