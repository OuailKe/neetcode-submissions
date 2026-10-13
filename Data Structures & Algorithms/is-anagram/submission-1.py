class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!= len(t)):
            return False
        s1 = dict()
        for char in s:
            if char in s1:
                s1[char] += 1
            else:
                s1[char] = 1
        for char in t:
            if char in s1:
                if (s1[char] == 0):
                    return False
                s1[char] -= 1
            else:
                return False
        return True
