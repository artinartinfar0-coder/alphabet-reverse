#how to do Reverse our Alphabet:
ALPHABET = ['A', 'B', 'C', ..., 'Z']
ALPHABET_REVERSE = ALPHABET.copy()
ALPHABET_REVERSE.reverse()

def ramznegari(str):
    result = ""
    for c in str:
        if c == " ":
            result += " "
            continue
        index = ALPHABET.index(c.upper())
        result += ALPHABET_REVERSE[index].upper() if c.isupper() else ALPHABET_REVERSE[index].lower()
    return result

i = input('str :')
print(ramznegari(i))