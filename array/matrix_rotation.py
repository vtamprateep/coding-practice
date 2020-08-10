'''
PROBLEM STATEMENT:

You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise) in-place. Do not
store values in an array.

EXAMPLE:
Given the input matrix = 
[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

The rotated matrix is = 
[
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

INTUITION:
1. We can imagine an n x n matrix made of concentric circles - each circle can be considered a sub-problem
2. There is a certain pattern which numbers get shifted around - this means we can track which set of numbers are swapped
3. I can focus on the top left and bottom right numbers as I traverse the layers. Once I get the corners correct,
   I can focus on traversing each side next.

  ^ 1 ---->
  | * * * * 4
  | * * * * |
  | * * * * |
  2 * * * * |
    <---- 3 V

CRUX OF THE PROBLEM:
- The indexes we traverse on each side is constricted on each side by 1 every layer (i.e. range(0, 4) => range(1, 3))
- For odd sided matrix, the middle is a single number and does not need to be rotated
- Trickiest part of the problem is getting your indexes right and traversing the right side in the right direction
'''

def matrixRotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    ops = n - 1

    # Outer loop traverses the layers of the n x n matrix
    for i in range(n // 2):
        # Innter loop traverses each side of the (sub) matrix layers
        for j in range(i, ops - 1):
            temp = matrix[i][j] # Store first value to prevent losing it
            matrix[i][j] = matrix[ops - j][i] # Replace number on the top
            matrix[ops - j][i] = matrix[ops - i][ops - j] # Replace number on the left
            matrix[ops - i][ops - j] = matrix[j][ops - i] # Replace number on the bottom
            matrix[j][ops - i] = temp # Replace number on the right

    return matrix