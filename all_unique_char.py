
# Function removes the white spaces from user given string.
def remove_spaces(withSpaceString):
	withoutSpaceString = withSpaceString.replace(" ","")
	return withoutSpaceString

# Function check the uniqueness of characters in the without whitespaced string.
def check_uniqueness(unique_string, unique_string_length):
	for i in range(0,unique_string_length):
		for j in range(0,unique_string_length):
			if i != j:
				if unique_string[i] == unique_string[j]:
					unique = False
					return unique
				else:
					unique = True
	return unique


Test_Str = raw_input("Enter a String : ")
new_str = remove_spaces(test_str)
length = len(new_str)
check = check_uniqueness(new_str, length)

if(check):
	print "Unique Characters in the String"
else:
	print "Not Unique Characters in the String"


#Time Complexity = O(N^2)
#Space Complexity = O(N)