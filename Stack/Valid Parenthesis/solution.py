class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        m = {
            ")":"(",
            "]":"[",
            "}":"{"
            }

        for char in s:
            if char in m:
                if stack and stack[-1] == m[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

                
        return True if not stack else False


        