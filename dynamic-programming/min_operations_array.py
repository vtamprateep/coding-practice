import unittest

'''
PROBLEM STATEMENT:

Given an array A[] of size N and two integers (K and D), calculate the minimum possible number of operations required
to obtain at least K equal array elements. Each operation involves replacing an element A[i] by A[i] // D.
This operation can be performed any number of times.

EXAMPLE:
A = [1, 2, 3, 4, 5]
K = 3
D = 2

The minimum number of operations is 2 and there are two solutions.

Solution 1: [1, 2, 3, 4, 5] => [1, 2, 3, 4, 5] => [1, 2, 3, 2, 2]
Performing integer solution on A[3] and A[4] yields 3 instances of two in two operations.

Solution 2: [1, 2, 3, 4, 5] => [1, 1, 3, 4, 5] => [1, 1, 1, 2, 2]
Performing integer solution on A[1] and A[2] yields 3 instances of 1 in two operations.

INTUITION:
1. We need to track the number of operations done on each number
2. Numbers can only go down - smaller number can not be increased
3. Numbers closer in value are more to converge on fewer operations

CRUX OF THE PROBLEM:
- This is a dynamic programming problem
- We want to know which numbers are 'seen' by each item in the array after each integer division
- We also want to track the number of aggregate operations on all numbers to get to that matching number
- We can use a two dimensional array to track which numbers are 'seen' (row index), how many numbers 'see' that
  number (row length) and number of operations for each applicable array item needed to get to that number (row element value)
'''

def minOperations(arr, threshold, n, d):

    # Initialize 2D array with max(arr) + 1 rows
    vector_map = [[] for _ in range(max(arr) + 1)]

    # Loop through each element in arr
    for num in arr:
        count = 0
        
        # Integer divide each element by d and record number of operations at number that is 'seen'
        while num > 0:
            vector_map[num].append(count)
            count += 1
            num //= d

    # Sort each row - prioritizes numbers that 'saw' the number denoted by row index with fewest operations first
    for row in range(len(vector_map)):
        vector_map[row] = sorted(vector_map[row])

    min_ops = -1

    for row in vector_map:
        # If row length is less than threshold, that means not enough numbers passed the number denoted by row index
        if len(row) < threshold:
            continue
        
        # Only need to sum first elements up to threshold
        local_min = sum(row[:threshold])

        # Overwrite min_ops based on number with lower amount of operations performed
        if min_ops < 0 or min_ops > local_min:
            min_ops = local_min

        if min_ops == 0:
            return min_ops
        
    return min_ops