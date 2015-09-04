# Implementing merge sort

li = [ 11, 4, 1, 2, 10, 6, 8, 3, 5]


#Function break_and_merge
#param lis_b{List Type}
#Function break the list into sublists recursively and then merge them by
#comparing with each other.
def break_and_merge(lis_b):
	newLength = len(lis_b)
	if newLength > 1 :
		mid = newLength / 2
		left = lis_b[0 : mid]
		right = lis_b[mid : ]

		break_and_merge(left)
		break_and_merge(right)

		l, r = 0, 0
		for i in range(0, newLength):
			if l < len(left) :
			 	leftVal = left[l]
			else :
				leftVal = None

			if r < len(right) :
			 	rightVal = right[r]
			else :
				rightVal = None

			if (leftVal and rightVal and leftVal < rightVal) or (rightVal is None):
				lis_b[i] = leftVal
				l += 1

			if (leftVal and rightVal and leftVal >= rightVal) or (leftVal is None):
				lis_b[i] = rightVal
				r += 1

#Function mergeSort
#param lis{List Type}
#function initialize the process for mergesort.
def mergeSort(lis):
	break_and_merge(lis)
	print lis

	
#Calling mergeSort with given list.
mergeSort(li)

