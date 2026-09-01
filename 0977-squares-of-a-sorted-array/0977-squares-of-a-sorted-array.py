class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [x * x for x in nums]
        ans.sort()
        return ans