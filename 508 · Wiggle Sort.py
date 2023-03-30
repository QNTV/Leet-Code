# Lintcode

# Description
# Given an unsorted array nums, reorder it in-place such that
# nums[0] <= nums[1] >= nums[2] <= nums[3]....
# There may have multiple answers for a question, you only need to consider one of the possibilities.

# Example 1:
# Input: [3, 5, 2, 1, 6, 4]
# Output: [1, 6, 2, 5, 3, 4]
# Explanation: This question may have multiple answers, and [2, 6, 1, 5, 3, 4] is also ok.

# Example 2:
# Input: [1, 2, 3, 4]
# Output: [1, 4, 2, 3]


from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @return: nothing
    """
    def wiggle_sort(self, nums: List[int]):
        for i in range(1, len(nums)):
            if ((i % 2 == 1 and nums[i] < nums[i - 1]) or 
               (i % 2 == 0 and nums[i] > nums[i -1])):
                nums[i] , nums[i - 1] = nums[i - 1], nums[i]
        return nums        
       
       
sol = Solution()
nums = [3, 5, 2, 1, 6, 4]
print(sol.wiggle_sort(nums)) 