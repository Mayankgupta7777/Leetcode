class Solution(object):
    def twoSum(self, nums, target):
        s = {}
        for i, v in enumerate(nums):
            r = target - v
            if r in s:
                return [s[r], i]
            s[v] = i
        return []
      
      #RESULT: 42ms
