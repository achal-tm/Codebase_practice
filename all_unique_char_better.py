user_input = raw_input(">Please Enter a String: ")

# comparing the length of the user given string and the length of set of that
# string because set doesn't have duplicate values 
if len(user_input) == len(set(user_input)): 
	print "Unique Characters in the String"
else :
	print "Not Unique Characters in the String"


#Time Complexity = O(1)
#Space Complexity = O(N)