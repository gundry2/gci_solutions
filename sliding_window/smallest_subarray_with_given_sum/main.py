"""
Problem statement: Given an array of positive numbers and a positive
number ‘S’, find the length of the smallest contiguous subarray whose
sum is greater than or equal to ‘S’. Return 0, if no such subarray
exists.
"""


def smallest_subarray_with_given_sum(s, arr):
    # If the sum of the whole array is less than s we just return.
    # This does necessitate O(n) time being expended here, though...
    if sum(arr) < s:
        #print("array too small")
        return 0

    # I think iterating over successively larger windows gives us
    # O(n^2) time??
    window_size = 0
    smallest_window = 0
    length = len(arr)
    curr = 0

    for i in range(length):
        #print(f"curr is currently {curr}, window_size is {window_size}. ADDING {arr[i]} to curr:")
        curr += arr[i]
        window_size += 1

        while curr >= s:
            if smallest_window == 0:
                smallest_window = window_size
            else:
                smallest_window = min(window_size, smallest_window)
            #print(f"curr is currently {curr}. Current window size is {window_size}. Smallest window so far is {smallest_window}. Subtracting {arr[i-window_size + 1]} from curr.")
            curr -= arr[i - window_size + 1]
            window_size -= 1
            #print(f"curr is now {curr}")

    return smallest_window


if __name__ == "__main__":
    arr1 = [2, 1, 5, 2, 3, 2]
    arr2 = [2, 1, 5, 2, 8]
    arr3 = [3, 4, 1, 1, 6]

    print(smallest_subarray_with_given_sum(7, arr1))
    print(smallest_subarray_with_given_sum(7, arr2))
    print(smallest_subarray_with_given_sum(8, arr3))
