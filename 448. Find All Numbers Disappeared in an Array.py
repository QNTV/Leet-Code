# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]

# Constraints:
#     n == nums.length
#     1 <= n <= 105
#     1 <= nums[i] <= n

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # mark existing numbers
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res
            
        
        
# Define a class named Solution with a method named findDisappearedNumbers
class Solution:
    # The method takes an array of integers as input and returns an array of integers as output
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Loop through each element in the array
        for n in nums:
            # Calculate the index corresponding to the absolute value of current element minus one
            i = abs(n) - 1
            # Mark the element at that index as negative by multiplying it with -1 and taking its absolute value
            nums[i] = -1 * abs(nums[i])

        # Initialize an empty array to store the missing elements
        res = []
        # Loop through each element in the array using its index and value
        for i, n in enumerate(nums):
            # Check if the element is positive, which means it was not marked as negative before
            if n > 0:
                # Add one to the index and append it to res as a missing element
                res.append(i + 1)
        # Return res as output
        return res

# Example: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Explanation:
# After first loop: nums = [-4,-3,-2,-7,8,2,-3,-1]
# After second loop: res = [5,6] (indices of positive elements plus one)       


sol = Solution()

print(sol.findDisappearedNumbers(nums)) 