'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    res = arr[0]
    for i in range(1, len(arr)):
        # XOR operator (sets each bit to 1 if only one of two bits is 1; more below)
        res = res ^ arr[i]
        print(res)
    return res


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")



# XOR EXPLAINED:
# compares 2 numbers/variables (a and b)
# if a = b (a = b = 0 OR a = b = sum_number), then output is 0
# if a = sum_number, and b = 0 (or vice versa), then output is 1
# (still need more help understanding)

