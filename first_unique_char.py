
def check_non_rep_char(u_list, length):
	for i in range(0, length):
		count = u_list.count(u_list[i])
		if count == 1 : return u_list[i]
	
	return "None"


user_input_string = raw_input("Please Enter a string: ")
if(user_input_string):
	user_input_string = user_input_string.replace(" ", "")
	input_list = list(user_input_string)
	print input_list
	list_length = len(input_list)
	result = check_non_rep_char(input_list, list_length)
	print "First non repeated character is : " + result

else:
	print "Please Enter a valid string !"


#Time Complexity = O(N)
#Space Complexity = O(N)