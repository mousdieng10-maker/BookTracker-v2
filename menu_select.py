import time
import readfile
correct_options = [1, 2, 3, 4, 5]


def options():
    while True:
        while True:
            try:
                choice = int(input('''
    Welcome to the Book tracker
    ----------------------------\n
    [1] See library
    [2] Search for books online
    [3] Get Random book Recommendation
    [4] import calibre library 
    [5] quit app
    > '''))
                break
            except ValueError:
                print("Please type a valid option.")
                time.sleep(1)
        if choice in correct_options:
            return choice
        else:
            print("Please type a valid option")
            time.sleep(1)


def search_result_select():
    options_available = [1,2,3]
    while True:
        try:
            choice = int(input('''
[1] Get book option
[2] Search again
[3] quit'''))
            if choice in options_available:
                return choice
            else:
                print("please type a valid option!")
        except ValueError:
            print("please type a valid option!")
            time.sleep(1)


def choose_book():
    books = readfile.read("tempsearch.json")
    result_list = []
    for book in books:
        result_list.append(book.get("Result"))
    while True:
        try:
            choose = int(input(f"Type the result number of the book you want to add to your library ({min(result_list)}-{max(result_list)}): "))
            if choose in result_list:
                for book in books:
                    if choose == book.get("Result"):
                        return book
        except ValueError:
            print("type a valid number")
