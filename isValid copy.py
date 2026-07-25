class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in mapping.values():
                stack.append(i)
            elif i in mapping:
                if not stack or stack.pop() != mapping[i]:
                  return False
        return not stack

sol = Solution()
test_input = "()[]{}"
result = sol.isValid(test_input)
print(f"Input: {test_input} | Result: {result}")