def consonant(word):
	vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']
	temp = ""
	while True:
		if word[0] in vowels:
			break

		else:
			temp += word[0]
			word = word[1:]
		word = word + temp
		word = word + 'ay'
		print(word,end=' ')

x = input("Enter an input: ")
x = x.split(' ')
vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']
for index in x:
	if index[0] not in vowels:
		consonant(index)
	else:
		temp = index + 'yay'
		print(temp,end=' ')