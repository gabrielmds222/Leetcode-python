class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max = 0

        for i in range(len(nums)):
            if(nums[i] + i > max):
                max = nums[i] + i
            if(max == i):
                break

        return max >= len(nums) - 1