import requests
import time
import readfile
import writefile
from menu_select import search_result_select as select
from menu_select import choose_book
base_url =  "https://openlibrary.org/search.json?title="
other_base_url = "https://openlibrary.org/"

def add_result():
    def make_url_and_check():
        search_result = 1
        writefile.rewrite("tempsearch.json",[])
        temp_list = readfile.read("tempsearch.json")
        title = input("What is the title of the book you're searching?: ")
        title = title.replace(" ", "+")
        new_url = f"{base_url}{title}"
        print(title)
        while True:
            try:
                response = requests.get(new_url)
                has_response = True
                break
            except TimeoutError:
                print("Connection timed out!")
                time.sleep(1)
            except ConnectionError:
                print("Connection Error!")
        if response.status_code == 200 and has_response:
            print("Connection is successful!")
            search_results = response.json()
            format_result = search_results.get("docs")
            print(format_result)
            for books in format_result:
                link_to = f"{other_base_url}{books.get("key")}"
                temp_dict = {
                    "Result":search_result,
                    "title":books.get("title"),
                    "author":books.get("author_name"),
                    "Link":link_to,
                    "ebook":books.get("ebook_access"),
                    "publish year":books.get("first_publish_year")
                }
                temp_list.append(temp_dict)
                print(f'''
    ------------------------------
    Result: ({search_result})
    Title: {books.get("title")} 
    Author: {books.get("author_name")}
    Link: {link_to}
    ebook?: {books.get("ebook_access")}
    Publish year: {books.get("first_publish_year")}''')
                search_result += 1
            writefile.rewrite("tempsearch.json",temp_list)
        elif response:
            print(f"Connection failed {response.status_code}.")
    while True:
        make_url_and_check()
        chosen = select()
        if chosen == 1:
            return choose_book()
        elif chosen == 2:
            pass
        elif chosen == 3:
            break
