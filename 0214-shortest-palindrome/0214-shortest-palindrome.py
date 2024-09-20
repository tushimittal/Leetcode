class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or s == s[::-1]:
            return s
     
        s_new = s + "#" + s[::-1]
        
        lps = [0] * len(s_new)
        length = 0 
        for i in range(1, len(s_new)):
            while length > 0 and s_new[i] != s_new[length]:
                length = lps[length - 1]
            if s_new[i] == s_new[length]:
                length += 1
                lps[i] = length
        
        longest_palindromic_prefix_length = lps[-1]
        
        
        remaining = s[longest_palindromic_prefix_length:]
        return remaining[::-1] + s
