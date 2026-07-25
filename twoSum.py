def twoSum(nums, target):
    for i1 in range(len(nums)):
        if i1 == 0:
            i3 = 0
            if (nums[i1]+nums[i1+1]) == target:
                return [i1, i1+1]
        else:
            i3 += 1            
        temp_value = nums[i1]
        for i2 in range(i1+1, len(nums)):
            if (nums[i2]+temp_value)==target:
                return [i2, i1]
            
nums = [3,2,4]
target = 6
twoSum(nums, target)