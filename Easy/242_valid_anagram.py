# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Time Complexity: O(n)
# Space Complexity: O(n)    

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        t = t.lower()

        if len(s) != len(t):
                return False
        
        s_count = {}
        t_count = {}
        
        for letter in s:
            s_count[letter] = s_count.get(letter, 0) + 1
        
        for letter in t:
            t_count[letter] = t_count.get(letter, 0) + 1

        return s_count == t_count

obj = Solution()
print(obj.isAnagram("anagram", "NagAram"))
print(obj.isAnagram("rat", "car"))
