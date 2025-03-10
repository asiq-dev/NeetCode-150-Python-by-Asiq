# 347 Top K frequent elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. k means how much char returned form the nums, and most frequent elements means is return top appear char from the list
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# solution method: solved using hashmap and heapq

from typing import List
import heapq
class Solution:
    def topKfrequent(self, nums: List[int], k: int)->List[int]:
        if k > len(set(nums)):
            return "K value is not greter than nums range"
        count = {}
        heap = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        print(count)
        
        for num in count:
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]
        

obj = Solution()
print(obj.topKfrequent([1,1,1,2,6,2,1], 2))