class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i,n in enumerate(nums):
            indexes[n] = i
        for i,n in enumerate(nums):
            diff = target - n
            if diff in indexes and indexes[diff] != i:
                return [i,indexes[diff]]
           