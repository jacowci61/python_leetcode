class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_str = ""
        if x < 0:
            return False
        else:
            input_str = str(x)
            for i in range(len(input_str)-1,-1,-1):
                reversed_str += input_str[i]
            if input_str == reversed_str:
                return True
            else:
                return False

sol = Solution()
test_input = 121
result = sol.isPalindrome(test_input)
print(f"Input: {test_input} | Result: {result}")