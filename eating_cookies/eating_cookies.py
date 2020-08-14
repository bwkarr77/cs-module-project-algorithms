'''
Input: an integer
Returns: an integer
'''
# 0 cookies = 0
# 1 cookie = 1
# 2 cookies = 2
# 3 cookies = 4
# 5 cookies = 13
# 10 cookies = 274

def eating_cookies(n):
    # Your code here
    if n == 0:  # 1 cookie or no cookies
        return 1
    elif n < 0:
        return 0
    else:
        # Fibanaci Equation: Fn = Fn-3 + Fn-2 + Fn-1
        # If he could eat 1, 3, or 5 cookies, the terms would be:
        # ---> (n-1) (n-3) and (n-5)
        return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)

def fib_mem(n, cache = {}):
    # print('recursion', n)
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return 0
    # have we already done this recursion loop/calculation? IF:
    # cache = {2: 2, 3: 4, 4: 7}
    # if n = 4, then we return cache[4]=7
    elif n in cache.keys():
        # print('cache: ', cache)
        return cache[n]
    else:
        value = fib_mem(n-1) + fib_mem(n-2) + fib_mem(n-3)
        # we create a dictionary of returned values (aka, recursion loop is complete). Looks like:
        # {2: 2, 3: 4, 4: 7, 5: 13, 6: 24, 7: 44, ...}
        cache[n] = value
        return value

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
