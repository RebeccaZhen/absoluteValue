def absoluteValue(input):
	if input >= 0:
		return input
	else:
		return 0 - input

print("Enter your integer: ")
Integer = input()
print(absoluteValue(Integer))