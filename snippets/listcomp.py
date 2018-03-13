results = [num for num in range(1000) if num % 7 == 0]
results

results = [num for num in range(1000) if '3' in list(str(num))]
results

teststring = 'Find all of the words in a string that are less than 4 letters'
results = [character for character in teststring if character == ' ']
len(results)


teststring = 'Find all of the words in a string that are less than 4 letters'
vowels = ['a','e','i','o','u',' ']
results = [letter for letter in teststring if letter.lower() not in vowels]
results

teststring = 'Find all of the words in a string that are less than 4 letters'
results = [word for word in teststring.split() if len(word) < 4]
results