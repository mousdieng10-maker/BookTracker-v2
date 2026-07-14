#import packages and modules

import readfile
import writefile
import add_book
import get_book
import calibre_book
import menu_select

data = readfile.read("booklib.json")
for book in data:
    print(book.get("title"))
def main():
    # main loop
    #open file at the start
    current_lib = readfile.read("booklib.json")
    while True:
        chosen = menu_select.options()
        if chosen == 1:
            for book in current_lib:
                print(f'{book}\n')
        elif chosen == 2:
            current_lib.append(get_book.add_result())
        elif chosen == 3:
            add_book.random_book(current_lib)
        elif chosen == 4:
            data = calibre_book.get_calibre_books(current_lib)

        elif chosen == 5:
            writefile.rewrite("booklib.json", current_lib)
            quit()


main()
