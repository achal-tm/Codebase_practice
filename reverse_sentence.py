#Asking User for an input string
user_input_string = raw_input("Please Enter a String: ")
input_list = user_input_string.split()

#Traversing the list in reverse order
reverse_input_list = input_list[::-1]

#Joining the elements of list with Join
print " ".join(reverse_input_list)


#Time Complexity = O(n)
#Space Complexity = O(n)