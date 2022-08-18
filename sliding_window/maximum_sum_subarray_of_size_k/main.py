"""
Problem Statement: Given an array of positive numbers and a positive
number ‘k’, find the maximum sum of any contiguous subarray of length
‘k’.
"""

def max_sub_array_of_size_k(k, arr):
    if len(arr) < k:
        return -1

    curr = sum(arr[0:k])
    largest = float('-inf')
    end_index = 0

    for i in range(k, len(arr)):
        curr -= arr[0+i-k]
        curr += arr[i]
        if largest < curr:
            largest = curr
            end_index = i

    return arr[end_index - k + 1:end_index + 1]

