# 暴力解
def twoSum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
                
    return []


# 效率解
def twoSum_efficient(nums, target):
    seen_map = {} 
    
    for i, num in enumerate(nums):
        complement = target - num 
        
        if complement in seen_map:
            return [seen_map[complement], i]
            
        seen_map[num] = i
        
    return []




nums = [2, 7, 11, 15]
target = 9

print("暴力解結果:", twoSum_brute(nums, target))
print("效率解結果:", twoSum_efficient(nums, target))