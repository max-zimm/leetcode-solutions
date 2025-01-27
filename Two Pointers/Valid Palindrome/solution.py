class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(" ", "")
        s = s.lower()
     

        for c in s:
            if not c.isalnum():
                s=s.replace(c, "")
        print(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True
            
        