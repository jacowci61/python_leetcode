class Solution:
    def romanToInt(self, s: str) -> int:
        RomanToInteger = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        total = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and RomanToInteger[s[i]] < RomanToInteger[s[i+1]]:
                total -= RomanToInteger[s[i]]
            else:
                total += RomanToInteger[s[i]]                
        return total
        
sol = Solution()
test_input = "MCMXCVI"
# 1000, 900, 90, 4
result = sol.romanToInt(test_input)
print(f"Input: {test_input} | Result: {result}")