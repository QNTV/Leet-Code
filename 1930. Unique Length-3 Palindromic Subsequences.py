# Given a string s, return the number of unique palindromes 
# of length three that are a subsequence of s.
# Note that even if there are multiple ways 
# to obtain the same subsequence, it is still only counted once.
# A palindrome is a string that reads the same forwards and backwards.
# A subsequence of a string is a new string generated 
# from the original string with some characters (can be none) 
# deleted without changing the relative order of the remaining characters.

#For example, "ace" is a subsequence of "abcde". 

# Example 1:
# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")

# Example 2:
# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".

# Example 3:
# Input: s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba") 

# Constraints:
#     3 <= s.length <= 105
#     s consists of only lowercase English letters.

solution 1:
class Solution(object):
    def countPalindromicSubsequence(self, s):
        d=defaultdict(list)
        for i,c in enumerate(s):
            d[c].append(i)
        ans=0
        for el in d:
            if len(d[el])<2:
                continue
            a=d[el][0]
            b=d[el][-1]
            ans+=len(set(s[a+1:b]))
        return(ans)
solution 2:
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
# Solutions

        # Palindromes will be in the format *_*
        # Hence, we can find the * from both sides when checking all letters a-z

        result = 0
        for char in string.ascii_lowercase:
            i, j = s.find(char), s.rfind(char)
            # All the candidates in the middle are candidates for the middle char _
            if i > -1:
                result += len(set(s[i + 1:j]))
        return result