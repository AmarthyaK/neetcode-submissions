class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict = {}
        t_dict = {}

        for s_str in s:
            try:
                s_dict[s_str] += 1
            except:
                s_dict[s_str] = 1
        for t_str in t:
            try:
                t_dict[t_str] += 1
            except:
                t_dict[t_str] = 1
        ## key length check
        length_of_unique_keys_s = len(list(s_dict.keys()))
        length_of_unique_keys_t = len(list(t_dict.keys()))
        if  length_of_unique_keys_s != length_of_unique_keys_t:
            return False 

        for key,value in s_dict.items():
            try:
                if s_dict[key] != t_dict[key]:
                    return False
            except:
                return False
        return True 

        