

'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

* Also named as First Missing Positive (41) at LeetCode
'''


#  Solution taking linear time and constant space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        #  Clean up
        for i in range(0, len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = len(nums) + 1

        #  Placing our marker
        for num in nums:
            num = abs(num)
            if num <= len(nums) and nums[num - 1] > 0:
                nums[num - 1] = -nums[num - 1]

        #  Final step
        for k in range(0, len(nums)):
            if nums[k] > 0:
                return k + 1

        return len(nums) + 1


#  Solution taking linear time and linear space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(1, max(nums) + 2):
            if i not in nums:
                return i

        return 1
