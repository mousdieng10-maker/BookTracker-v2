import subprocess
import json

def get_calibre_books(lib):
    choosing = [1,2]
    while True:
        try:
            choose = int(input("Are you sure? this is a beta feature and could create duplicates in the library? yes(1) no(2): "))
            if choose in choosing:
                break
            else:
                print("please type something valid")
        except ValueError:
            print("Please type something valid.")
    if choose == 1:
        result = subprocess.run(
            ["calibredb", "list", "--for-machine", "--fields", "title,authors,tags"],
            capture_output=True,
            text=True
        ).stdout
        result = json.loads(result)
        for book in result:
            lib.append(book)
        return result

