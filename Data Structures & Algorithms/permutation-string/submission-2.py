class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
            
        s1_sorted = sorted(s1)
        
        for i in range(len2 - len1 + 1):
            if sorted(s2[i : i + len1]) == s1_sorted:
                return True
                
        return False