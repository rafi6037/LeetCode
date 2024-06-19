from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] == target:
            return [i, j]
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return []

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))
