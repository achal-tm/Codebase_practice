# Flatten a nested list ( input: [1, [2,3,4], [5,6], 7] output: [1, 2, 3, 4, 5, 6, 7])

lis = [1, [2, 3, [4, [10, 'Hello'], 11]], [5, 6], 7]

#declaring global variables
new_li = []
index = 0

#Function flat_list {Recursive function}
#Param li {LIST object}
def flat_list(li):
	for i in range(0,len(li)):
		type_var = type(li[i])
		
		global index

		if type_var != list:
			new_li.insert(index, li[i])
			index += 1

		elif type_var == list:
			flat_list(li[i])

#calling flat_lis() on given list
flat_list(lis)

print "Input : ", lis
print "Output : ", new_li

#Time Complexity = O(n^2)
#Space Complexity = O(n^2)