# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。假设每个输入只对应一种答案，且同样的元素不能被重复利用。

def twoSum_1(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                return (i, j)

def twoSum_2(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return (d[target - num], i)
        d[num] = i

nums = [1, 3, 7, 11, 16]
print(twoSum_1(nums, target=27))
print(twoSum_2(nums, target=27))
