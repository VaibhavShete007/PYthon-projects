import _json
import json
from difflib import get_close_matches

data = json.load(open("data.json.json"))
def trasnlate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        j=input("Did you mean %s ?,Enter Y if YES and N if NO:" %get_close_matches(w,data.keys())[0])
        if j=="H":
            return data[get_close_matches(w,data.keys())[0]]
        elif j=="N":
            return "The word doesn't exist,please double check it."
        else:
            return "we doesn't understant your entry."
    else:
        return ("sorry this word doesn't exist,please double check. ")
word=input("ENTER:")

OP=(trasnlate(word))
if type(OP)==list:
    for item in OP:
        print(item)
else:
    print(OP)