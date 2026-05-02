class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            try:
                hashmap[nums[i]].append(i)
            except:
                hashmap[nums[i]] = [i]
        
        for num in nums:
            try:
                if num == target - num:
                    return sorted([hashmap[target-num][0],hashmap[num][1]])
                return sorted([hashmap[target-num][0],hashmap[num][0]])
            except:
                continue
        
        