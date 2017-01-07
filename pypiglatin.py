from re import split, IGNORECASE
from string import punctuation


def word_to_pig_latin(word):
    if word[0] in "aeiouyAEIOUY":
        return word + "way"
    else:
        sep = split(r"(^[^[aeiou]*]*)", word, flags=IGNORECASE)[1:]
        if sep[0][0].isupper():
            return (sep[1] + sep[0] + "ay").lower().capitalize()
        else:
            return sep[1] + sep[0] + "ay"


def text_to_pig_latin(text):
    pig_latin = {}
    words = text.translate(None, punctuation).split()

    for word in words:
        if word not in pig_latin:
            pig_latin[word] = word_to_pig_latin(word)

    for word in pig_latin:
        text = text.replace(word, pig_latin[word])

    return text

ttpl = text_to_pig_latin
