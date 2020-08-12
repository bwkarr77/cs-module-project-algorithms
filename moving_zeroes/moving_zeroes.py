'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    res = [0]*len(arr)
    count = 0
    for i in range(0, len(arr)):
        if arr[i] != 0:
            res[count] = arr[i]
            count += 1
    return res


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")