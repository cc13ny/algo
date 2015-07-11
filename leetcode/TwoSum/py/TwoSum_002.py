'''
  Just code simplication from TwoSum_001.py
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]] + 1, i+1]
            dict[nums[i]] = i
