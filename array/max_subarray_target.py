'''
PROBLEM STATEMENT:

Given an array nums and an integer target, return the maximum number of non-empty non-overlapping subarrays such that
the sum of values in each subarray is equal to target.

EXAMPLE:
nums = [-1, 3, 5, 1, 4, 2, -9]
target = 6
Output: 2
Explanation: There are 3 subarrays with sum equal to 6.
    1. [5, 1]
    2. [4, 2]
    3. [3, 5, 1, 4, 2, -9]

The first two arrays are the only non-overlapping.

INTUITION:
1. Smaller subarrays are more ideal as it allows for more subarrays with less chance of overlapping
2. We want to be careful of how we design our algorithm - if there is a subarray within a subarray that equals
   the target, we'll want to go for that one.
3. This problem falls under dynamic programming but requires a certain mastery of arrays

CRUX OF THE PROBLEM:
- We can't do a scan then divide an conquer algorithm with varying windows as there may be configurations that are more ideal.
  Take for example: [1, 2, 8, 3, 8] with target of 11
    - If we scan left to right using windows of 1, 2, 3, ... we capture the subarray [8, 3] first
    - If we recursively call the algorithm on the left and right side, this would return max subarray of 1
- Using the prefix sum method, we can get a running total at every index. Note that if there are subarrays that sum
  to the target, the difference of any two index will also equal the target.

Original                  = [-1, 3, 5, 1, 4, 2, -9]
Prefix Sum Transformation = [-1, 2, 7, 8, 12, 14, 5]
Running Sum minus target  = [-7, -4, -1, 2, 6, 8, -1]

- As we calculate our prefix sum transformation, store it in a hashtable. As you compute your running sum minus target
  value, check if you find the complement in the hashtable.
- Reset the hashtable everytime you find a match.
'''
from collections import defaultdict

def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
    prefix_sum = 0
    seen_num = defaultdict(int)
    seen_num[0] = 0 # Initializing your dictionary ensures we capture the first count
    count = 0
    
    for i in nums:
        prefix_sum += i
        
        if prefix_sum - target in seen_num:
            count += 1
            seen_num = defaultdict(int) # When you refresh your dictionary, don't initialize at zero to avoid overcounting
        
        seen_num[prefix_sum] += 1
        
    return count