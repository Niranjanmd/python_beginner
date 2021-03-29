def count_char_occur(word: str):
    occurrence = {}
    for c in str.lower(word):
        if c in occurrence.keys():
            occurrence[c] += 1

        else:
            occurrence[c] = 1
    return occurrence


if __name__ == '__main__':
    word = input("Enter Word :")
    print(count_char_occur(word))

