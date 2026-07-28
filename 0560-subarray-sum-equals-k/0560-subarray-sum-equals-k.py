class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={}
        freq[0]=1
        prefix=0
        count=0
        for x in nums:
            prefix += x
            target =prefix-k
            if target in freq:
                count += freq[target]
            if prefix in freq:
                freq[prefix] += 1
            else:
                freq[prefix]=1
        return count