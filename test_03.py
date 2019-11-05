array = [-2, -1, 4, 3, 8]
print('The question number 3.\n')
print('array: ', array, '\n')
#print(len(array))
for i in range(1, len(array)+2):
	if i not in array:
		print(i)
		break
print("\n")



