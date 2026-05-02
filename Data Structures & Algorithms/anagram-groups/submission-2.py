class Solution:

    def get_ascii_map(self,string):
        ref_map = [0]*26
        reference_ascii = ord('a')


        for letter in string:
            ref_map[ord(letter)-reference_ascii]+=1

        return tuple(ref_map)

## First I thought of using the reference map as a 26 lettered string and the counter changes the digit
## But what if the counter of the string exceeds 10, then that becomes a problem. 
## So instead of the a string, it was shifted to tuple

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            try:
                hashmap[self.get_ascii_map(string)].append(string)
            except:
                hashmap[self.get_ascii_map(string)] = [string]
        return list(hashmap.values())


        



        