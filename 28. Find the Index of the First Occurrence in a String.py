# Given two strings needle and haystack, 
# return the index of the first occurrence 
# of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# Constraints:
#     1 <= haystack.length, needle.length <= 104
#     haystack and needle consist of only lowercase English characters.

class Solution:
    def strStr(self, haystack, needle):
        if needle == "": return 0
        lps = [0] * len(needle)
        
        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS +1 
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS -1]
                
        i = 0 # ptr for haystack
        j = 0 # ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)
        return -1
        
        
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


# Boyer-Moore algorithm 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        
        n = len(haystack)
        m = len(needle)
        
        # create bad match table
        bm_table = {}
        for i in range(m-1):
            bm_table[needle[i]] = m-1-i
        
        # search for the needle in the haystack
        i = m-1
        while i < n:
            k = i
            j = m-1
            while j >= 0 and haystack[k] == needle[j]:
                k -= 1
                j -= 1
            if j == -1:
                return k+1
            if haystack[i] in bm_table:
                i += bm_table[haystack[i]]
            else:
                i += m
        
        return -1



# Rabin-Karp algorithm


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        
        n = len(haystack)
        m = len(needle)
        p = 31
        p_pow = [1]
        for i in range(m-1):
            p_pow.append(p_pow[-1] * p)
        
        # compute hashes for needle and first m characters of haystack
        needle_hash = 0
        for i in range(m):
            needle_hash += ord(needle[i]) * p_pow[m-1-i]
        haystack_hash = 0
        for i in range(m):
            haystack_hash += ord(haystack[i]) * p_pow[m-1-i]
        if needle_hash == haystack_hash and haystack[:m] == needle:
            return 0
        
        # compute rolling hash for haystack and check for needle match
        for i in range(m, n):
            haystack_hash -= ord(haystack[i-m]) * p_pow[m-1]
            haystack_hash = haystack_hash * p + ord(haystack[i])
            if haystack_hash == needle_hash and haystack[i-m+1:i+1] == needle:
                return i-m+1
        
        return -1
