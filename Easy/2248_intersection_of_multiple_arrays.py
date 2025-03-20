# 2248. Intersection of Multiple Arrays 
# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
 

# Example 1:

# Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# Output: [3,4]
# Explanation: 
# The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].

from typing import List

# approach -1(time-2ms)
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        make_set = [set(sublist) for sublist in nums]
        result = make_set[0]

        for subset in make_set[1:]:
            result = result.intersection(subset)
        
        print(sorted(result))

obj = Solution()
obj.intersection([[1,2,2,1,4,3,5],[1,2,4,3],[4,1,3,6]])


# approach -2(mannual, time-3ms)
# class Solution:
#     def myintersection(self, nums: List[List[int]]) -> List[int]:
#         count = {}
#         for subset in nums:
#             seen = set()
#             for number in subset:
#                 if number not in seen:
#                     count[number] = count.get(number, 0) + 1
#                     seen.add(number)
#         result = []
#         for i in count:
#             if count[i] == len(nums):
#                 result.append(i)
#         return sorted(result)


# obj = Solution()
# print(obj.myintersection([[1,2,2,1,4,3,5],[1,2,4,3],[4,1,3,6]]))