import json
from difflib import get_close_matches

"""
r
This is a command line based interactive dictioner.
"""


data=json.load(open("data.json"))



def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter y if yes, or n if no: " % get_close_matches(w, data.keys())[0])
        if yn == "y":
            return data [get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "This word does not exist, please double check it."
        else:
            return "I do not understand your query."
    else:
        return "This word does not exist, please double check it."

while True:
    word = input("Enter word, type quit if you are done: ")
    if word == 'quit': break
    else:
        output = translate(word)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)
        