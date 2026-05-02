class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## In my previous solution, I have initilized the hashmap already and then began my search lookups.
        ## Instead the trick is to search and fill the hashmap simultaneosuly for a simpler code archictecture.

        hashmap = {}

        for i in range(len(nums)):
            try:
                return sorted([hashmap[target - nums[i]],i])
            except:
                hashmap[nums[i]] = i