class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        indexOfZero = []
        for i in range(len(nums)):
            if nums[i] == 0:
                indexOfZero.append(i)
        for i in range(len(nums) -1, -1, -1):
            if nums[i] == 0:
                del nums[i]
        for i in range(len(indexOfZero)):
            nums.append(0)

sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
test_input = nums
result = sol.moveZeroes(test_input)
print(f"Input: {test_input} | Result: {result}")