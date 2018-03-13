sentence = 'Use a dictionary comprehension to count the length of each word in a sentence'
results = {word:len(word) for word in sentence.split()}
results

#Method 1:
results = [number for number in range(1,1001) if True in [True for divisor in range(2,10) if number % divisor == 0]]
results
#Method 2:
[num for num in range(1,1001) if [div for div in range(2,10) if num%div == 0]]
results

results = {number:max([divisor for divisor in range(1,10) if number % divisor == 0]) for number in range(1,1001)}
results

