from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        listToSet = set(nums)
        newlist = list(listToSet)
        return len(newlist)

# Create an instance of the Solution class
solution = Solution()

# Test the removeDuplicates method
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(solution.removeDuplicates(nums))
