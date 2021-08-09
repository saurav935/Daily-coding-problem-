

'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''


#Also named as Product of Array except self (238) on leetcode


# Takes O(n) time and O(1) space
def product(nums):
    left = 1
    right = [1]

    for j in nums[:0:-1]:
        right.append(right[-1] * j)

    right = right[::-1]

    for i in range(0, len(nums)):
        right[i] = right[i] * left
        left = left * nums[i]

    return right



# Takes O(n) time and O(n) space
def product(nums):    
    left = [1]
    right = [1]
    
    for i in nums[:-1]:
        left.append(left[-1] * i)
    
    for j in nums[:0:-1]:
        right.append(right[-1] * j)
    
    right = right[::-1]
    
    for k in range(0, len(nums)):
        nums[k] = left[k] * right[k]
    
    return nums


nums = [1,2,3,4,5]
print(product(nums))

