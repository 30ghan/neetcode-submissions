class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        oldMap = {}

        for i, n in enumerate (nums):
            diff = target - n
            if diff in oldMap:
                return [oldMap[diff], i]

            oldMap[n] = i    

        