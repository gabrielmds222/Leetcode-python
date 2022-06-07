class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return [[]]
        res = [[]]

        for i in nums:
            n = len(res)
            for j in range(n):
                r = res[j] + [i]
                res.append(r)
        return res