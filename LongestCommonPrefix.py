class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i in range(len(strs)):
            while i + 1 < len(strs) and strs[i] == strs[i+1]:
                
sol = Solution()
strs = ["flower","flow","flight"]
test_input = strs
result = sol.longestCommonPrefix(test_input)
print(f"Input: {test_input} | Result: {result}")