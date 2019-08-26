import json
import time

from difflib import get_close_matches

file=json.load(open('data.json'))

def translate(word):
    if word in file:
        return file[word]
    else:
        closematches=get_close_matches(word,file.keys())
        if len(closematches)!=0:
            question=input('did you mean '+closematches[0]+'?\ntype "Y" for Yes , type "N" for No\n').upper()
            if question=='Y':
                return file[closematches[0]]
            elif len(closematches)>=2:
                question=input('did you mean '+closematches[1]+'?\ntype "Y" for Yes , type "N" for No\n').upper()
            if question=='Y':
                return file[closematches[1]]
            elif len(closematches)>=3:
                question=input('did you mean '+closematches[2]+'?\ntype "Y" for Yes , type "N" for No\n').upper()
            if question=='Y':
                    return file[closematches[2]]
            else:
                return "word doesn't figure in dictionary, please check it out"
        else:
            return "word doesn't figure in dictionary, please make sure you are spelling it right"

if __name__=="__main__":
    word=input('Enter a word :\t').lower()
    definition=translate(word)
    if type(definition)==list:
        for i in definition:
            print("#"+i)
    else:
        print(definition)

    time.sleep(30)
