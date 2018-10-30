import json
from difflib import get_close_matches

"""
r
This is a command line based interactive dictioner.
"""
x = ''
while x == "y":
    x = input("Do you want me to define a word? Enter y if yes, or n if no: ")
    if x == "y":
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

        word = input("Enter word: ")

        output = translate(word)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)
    else:
        print("please come back again")