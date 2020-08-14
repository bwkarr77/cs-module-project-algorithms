'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# need to fine tune so it can handle larger inputs
from collections import deque

def sliding_window_max(nums, k):
    # Your code here
    # n = len(nums)-k+1
    # res = [0]*n

    # for i in range(0, n):
    #     m = nums[i]
    #     for j in range(i+1, k+i, 1):
    #         if nums[j] > m:
    #             m = nums[j]
    #     res[i] = m

    # return res

    n = len(nums)
    Qi = deque()
    res = []
    for i in range(k):
        while Qi and nums[i] >= nums[Qi[-1]]:
            Qi.pop()
        Qi.append(i)

    for i in range(k, n):
        # print('for loop: ', i, nums[Qi[0]], nums[Qi[-1]])
        res.append(nums[Qi[0]])
        while Qi and Qi[0] <= i-k:
            Qi.popleft()
        while Qi and nums[i] >= nums[Qi[-1]]:
            Qi.pop()
        Qi.append(i)

    res.append(nums[Qi[0]])
    return res









if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
