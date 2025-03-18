# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.



from typing import List

# brute-force approach (O(n²)):
# class Solution:
#     def ProductofArray(self, nums: List[int]) -> List[int]:
#         size = len(nums)
#         print(size)
#         output = []

#         for i in range(0, size):
#             mul = 1
#             for j in range(0, size):
#                 if i != j:
#                     mul *= nums[j]
                
#             output.append(mul)
#         print(output)



#best optimal approach with prefix, postfix
class Solution:
    def ProductofArray(self, nums: List[int]) -> List[int]:
        size_of_nums = len(nums)
        result = [1] * size_of_nums

        prefix = 1
        for i in range(0, size_of_nums):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        # two way for reverser range. (start, stop, step)/ reversed(range(sizeoflen))
        for j in reversed(range(size_of_nums)):
            result[j] *= postfix
            postfix *= nums[j]
        
        return result


obj = Solution()
print(obj.ProductofArray([1,2,3,4]))