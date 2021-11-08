originalList =  ['mix', 'xyz', 'apple', 'xanadu', 'rovio']

wordsWithX = []
wordWithoutX = []
for letter in originalList:
    if 'x' in letter[0]:
        wordsWithX.append(letter)
    else:
        wordWithoutX.append(letter)
wordsWithX.sort()
wordWithoutX.sort()

print(wordsWithX, wordWithoutX)