# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

 # Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.

# Constraints:
#     1 <= nums.length <= 105
#     -231 <= nums[i] <= 231 - 1

class Solution:
    def firstMissingPositive(self, A) -> int:
        for i in range(len(A)):
            if A[i] < 0:
                A[i] = 0
                
        for i in range(len(A)):
            val = abs(A[i])
            if 1 <= val <= len(A):
                if A[val -1] > 0:
                    A[val -1] *= -1
                elif A[val - 1] == 0:
                    A[val - 1] = -1 * (len(A) + 1)
                    
        for i in range(1, len(A) +1):
            if A[i - 1] == 0:
                return i
        return len(A) + 1


class Sol:
  def firstMissingPositive(self, nums) -> int:
        n = len(nums)
		
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        for i in range(n):
            if abs(nums[i]) > n:
                continue
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1



Sol = Sol()
Solution = Solution()
A = [7,8,9,11,12]

print(Sol.firstMissingPositive(A))