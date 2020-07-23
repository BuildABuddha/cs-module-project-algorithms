'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    """
    The array [1, 2, 3] turns into...
    [
        ()      *   (2 * 3), 
        (1)     *   (3), 
        (1 * 2) *   ()
    ]

    So we need to make a way to build two arrays of length n, one that looks like [1, 1, 1*2] and [2*3, 3, 1].
    """
    n = len(arr)
    arr_1 = [1] * n
    arr_2 = [1] * n

    # Construct first list:
    index = 1
    while index < n:
        arr_1[index] = arr_1[index-1] * arr[index-1]
        index += 1

    # Construct second list:
    index = n - 2
    while index > -1:
        arr_2[index] = arr_2[index+1] * arr[index+1]
        index -= 1

    # Find product of both lists:
    index = 0
    return_arr = [0] * n
    while index < n:
        return_arr[index] = arr_1[index] * arr_2[index]
        index += 1

    return return_arr

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
