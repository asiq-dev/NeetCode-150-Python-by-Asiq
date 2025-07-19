# Encode and Decode Strings

# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(str):
            j=i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            result.appned(str[j + 1: j+ 1 + length])

            i= j + 1 + length

        return result