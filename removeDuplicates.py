class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                del nums[i+1]
        length = len(nums)
        return length

sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
test_input = nums
result = sol.removeDuplicates(test_input)
print(f"Input: {test_input} | Result: {result}")