# There are n dominoes in a line, and we place each domino vertically upright. 
# In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

# After each second, each domino that is falling to the left pushes the adjacent domino on the left. 
# Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

# When a vertical domino has dominoes falling on it from both sides, 
# it stays still due to the balance of the forces.

# For the purposes of this question, we will consider that a falling domino 
# expends no additional force to a falling or already fallen domino.

# You are given a string dominoes representing the initial state where:

#     dominoes[i] = 'L', if the ith domino has been pushed to the left,
#     dominoes[i] = 'R', if the ith domino has been pushed to the right, and
#     dominoes[i] = '.', if the ith domino has not been pushed.
# Return a string representing the final state. 

# Example 1:
# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.

# Example 2:
# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."

# Constraints:
#     n == dominoes.length
#     1 <= n <= 105
#     dominoes[i] is either 'L', 'R', or '.'.

from typing import List
from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        q = deque()
        
        for i, d in enumerate(dom):
            if d != ".": q.append((i, d))
            
        while q:
            i, d = q.popleft()
            
            if d == "L" and i > 0 and dom[i - 1] == ".":
                q.append((i - 1, "L"))
                dom[i -1] = "L"
            elif d == "R":
                if i + 1 < len(dom) and dom[i + 1] == ".":
                    if i + 2 < len(dom) and dom[i + 2] == "L":
                        q.popleft()
                    else:
                        q.append((i + 1, "R"))
                        dom[i + 1] = "R"
        return "".join(dom)
                        
Solution = Solution()
dominoes = ".L.R...LR..L.."

print(Solution.pushDominoes(dominoes))


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Two pointer
        # d[i] == L and d[j] == R : no push
        # d[i] == d[j] : push all
        # d[i] == R and d[j] == L : push i->mid to R + [ . if mid is odd] + push j <- mid to L
        
        res = ""
        prev = 'L'
        dots = 0
        dominoes += 'R'
        for c in dominoes:
            if c == '.':
                dots += 1
                continue
            
            if prev == c:
                res += c * dots
            elif prev == 'L' and c == 'R':
                res += '.' * dots
            else:
                half = dots // 2
                mid = '.' if dots % 2 else ""
                res += 'R' * half + mid + 'L' * half
            
            res += c
            dots = 0
            prev = c

        return res[:-1]


sol = Solution()
dominoes = ".L.R...LR..L.."
print(sol.pushDominoes(dominoes))