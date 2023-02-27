# You are given a 0-indexed string s of even length n. 
# The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

# A string is called balanced if and only if:
#     It is the empty string, or
#     It can be written as AB, where both A and B are balanced strings, or
#     It can be written as [C], where C is a balanced string.

# You may swap the brackets at any two indices any number of times.
<<<<<<< HEAD
# Return the minimum number of swaps to make s balanced. 
=======
# Return the minimum number of swaps to make s balanced.
>>>>>>> 97cbca2ef620242e312f08078915fa28441dc88a

# Example 1:
# Input: s = "][]["
# Output: 1
# Explanation: You can make the string balanced by swapping index 0 with index 3.
# The resulting string is "[[]]".

# Example 2:
# Input: s = "]]][[["
# Output: 2
# Explanation: You can do the following to make the string balanced:
# - Swap index 0 with index 4. s = "[]][][".
# - Swap index 1 with index 5. s = "[[][]]".
# The resulting string is "[[][]]".

# Example 3:
# Input: s = "[]"
# Output: 0
# Explanation: The string is already balanced. 

# Constraints:
#     n == s.length
#     2 <= n <= 106
#     n is even.
#     s[i] is either '[' or ']'.
#     The number of opening brackets '[' equals n / 2, and the number of closing brackets ']' equals n / 2.

class Solution:
   def minSwaps(self, s):
      close, maxClose = 0, 0
        
     for c in s:
            if c == "[":
                close -= 1            
          else:
                close += 1
            maxClose = max(close, maxClose)
        return (maxClose + 1) // 2
    
class Solution:
    def minSwaps(self, s: str) -> int:
        # it is number of mismatches/2 approx
        # as every swap its easy to handle both open and close

        stack_size = 0
    
        for c in s:
            if c is '[':
                stack_size += 1
            else:
                if stack_size:
                    stack_size -= 1
                else:
                    stack_size += 1
        return (stack_size+1)//2