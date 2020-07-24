'''
Input: an integer
Returns: an integer
'''
    
def eating_cookies(n, cache=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        if cache is None:
            cache = [0] * (n + 1)

        if cache[n] != 0:
            return cache[n]
        else:
            cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache) 
            # print(f"{n}: {cache[n]}")
            return cache[n]



if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 500

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
