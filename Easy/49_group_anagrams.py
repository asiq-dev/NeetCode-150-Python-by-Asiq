# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


from typing import List
class Solution:
    def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            array = [0] * 26
            for letter in word:
                array[ord(letter) - ord('a')]+= 1

            key = tuple(array)
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]

        return print(list(anagrams.values()))

obj = Solution()
obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])