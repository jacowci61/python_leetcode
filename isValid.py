class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        temp_string = ""
        round_Parentheses = "()"
        square_Parentheses = "[]"
        spiky_Parentheses = "{}"
        for i1 in range(len(s)):
            stack.append(s[i1])
        i = 0
        for i2 in range(len(stack)):
            if i == 2:
                i = 0
                if temp_string == round_Parentheses or temp_string == square_Parentheses or temp_string == spiky_Parentheses:
                    return True
                temp_string = ""
            else:
                i += 1
                temp_string += stack.pop(0)
            # return True
        return False

sol = Solution()

test_input = "()"
result = sol.isValid(test_input)

print(f"Input: {test_input} | Result: {result}")