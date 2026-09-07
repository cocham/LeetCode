class Solution:
    def longestPalindrome(self, s: str) -> str:
            n = len(s)
            dp = [[False] * n for _ in range(n)]

            start, max_len = 0, 1

            for i in range(n): #길이가 1
                    for j in range(n):
                        if (i == j):
                            dp[i][j] = True


            for i in range(n - 1): #길이가 2
                if (s[i] == s[i + 1]):
                    dp[i][i + 1] = True
                    start = i
                    max_len = 2



            for length in range(3, n + 1): #길이
                for i in range(n - length + 1): #시작 인덱스
                    j = i + length - 1

                    if (s[i] == s[j] and dp[i + 1][j - 1]):
                        dp[i][j] = True
                        start = i
                        max_len = length
                        

            return s[start : start + max_len]
            
