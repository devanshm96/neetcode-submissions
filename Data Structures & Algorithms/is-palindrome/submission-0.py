class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return True
        
        # Tc and SC : O(n) 
        # cleaned = []
        # for ch in s:
        #     if not ch.isalnum():
        #         continue
        #     cleaned.append(ch.lower())
        
        # return cleaned == cleaned[::-1]

        #  TC: O(n), SC: O(1)
        # i,j = 0, len(s)-1
        # while i<j:
        #     while i<j and not s[i].isalnum():
        #         i+=1
        #     while i<j and not s[j].isalnum():
        #         j-=1
            
        #     if s[i].lower() != s[j].lower():
        #         return False
        #     i+=1
        #     j-=1
        # return True
        
        # Build a cleaned string (lowercased, alphanumeric only)
        cleaned = [c.lower() for c in s if c.isalnum()]
        n = len(cleaned)
        # Palindrome check
        for i in range(n // 2):
            # print("n-i-1 ", n-i-1)
            if cleaned[i] != cleaned[n-i-1]:
                return False
        return True