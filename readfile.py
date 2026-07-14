import json
from json import JSONDecodeError


def read(file):
    to_add = []
    while True:
        try:
            with open(file, "r") as f:
                 data = json.load(f)
            break
        except JSONDecodeError:
            with open(file, "w") as f:
                json.dump(to_add,f, indent=4)
        except FileNotFoundError:
            open(file,"x")
    return data

