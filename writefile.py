import json
import readfile
def rewrite(file, data):
    while True:
        try:
            with open(file, "w") as f:
                json.dump(data, f, indent=4)
            break
        except FileNotFoundError:
            open(file, "x")

