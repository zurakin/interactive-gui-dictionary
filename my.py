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
            out='word is not in dictionary, mabye try {}'.format(closematches[0])
            if len(closematches)>=2:
                out+=', {}'.format(closematches[1])
                if len(closematches)>=3:
                    out+=' or {}'.format(closematches[2])

        else:
            out= "word doesn't figure in dictionary, please double check it"
        return [out]

if __name__=="__main__":
    word=input('Enter a word :\t').lower()
    definition=translate(word)
    if type(definition)==list:
        for i in definition:
            print("#"+i)
    else:
        print(definition)

    time.sleep(30)
