def absoluteValue(input):
	if int(input) >= 0:
		return input
	else:
		return 0 - int(input)

print("Enter your integer: ")
Integer = input()
print(absoluteValue(Integer))