'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    current_index = 0
    stopping_index = len(arr)

    while current_index < stopping_index:
        if arr[current_index] == 0:  # If the current number is zero...
            arr.append(arr.pop(current_index))  # Move to the end of the list
            stopping_index -= 1  # We now stop one index earlier to avoid an infinite loop.
        else:
            current_index += 1  # Move on to the next index.

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")