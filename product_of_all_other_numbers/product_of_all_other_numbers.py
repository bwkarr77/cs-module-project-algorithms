'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    n = len(arr)

    left = [0]*n
    right = [0]*n
    prod = [0]*n

    # first index of left, and last index of right is 1
    left[0] = 1
    right[n-1] = 1

    # example: arr = [10, 2, 3, 4, 5]

    # left is a list that is offset to the right by 1,
    # and multiplies the index of arr[l] by the previous value at left[l]
    # ex: if left[2]=3, then left[3]=arr[l]*3
    for l in range(0, n-1):
        left[l+1] = arr[l] * left[l]
        # example: left = [1, 1*10, 2*(1*10), 3*(2*(1*10)), 4*(3*(2*(1*10)))]

    # similar to left, but starts at the right and works to the left.
    for r in range(n-1, 0, -1):  # start, stop, step
        right[r-1] = arr[r] * right[r]
        # example: right = [2*(3*(4*(5*1))), 3*(4*(5*1)), 4*(5*1), 5*1, 1]

    # print('left: ', left, '\nright:', right)
    for p in range(n):
        prod[p] = left[p] * right[p]
        # example: prod = [1 * 2*(3*(4*(5*1))), 1*10 * 3*(4*(5*1)), 2*(1*10) * 4*(5*1), 3*(2*(1*10)) * 5*1,
        # 4*(3*(2*(1*10))) * 1]

    return prod






if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [10, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
