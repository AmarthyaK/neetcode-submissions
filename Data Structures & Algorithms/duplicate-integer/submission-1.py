class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashmap = {}

        for i in nums:
            try:
                hashmap[i]+=1
                return True
            except:
                hashmap[i] = 1
        return False
        