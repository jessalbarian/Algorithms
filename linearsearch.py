# Objective: Search through a list. Return the value if found, otherwise, return nil

A = [1,2,3,4,5,6]
v = 7 # this will make the function return none

def linearSearch(A, v):
        position = 0
        while position < len(A):
                if A[position] == v:
                        return v
                position += 1
        return
