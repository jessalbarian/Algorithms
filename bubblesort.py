#Bubblesort Algorithm

A = [1,5,3,4,2]

def bubbleSort(A):
	for i in range(0, len(A)-1):
		for j in range(len(A), i+1):
			print("i", i)
			if A[j] < A[j-1]:
				temp = A[j]
				A[j] = A[j-1]
				A[j-1] = temp						
	print(A)

bubbleSort(A)
# Nested loops take n running time each, so the running time of bubblesort is O(n^2).
