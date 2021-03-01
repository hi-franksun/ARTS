
from typing import List


class Solution:

    def insertSord(self, nums: List) -> List:
        length = len(nums)
        for i in range(1, length):
            key = nums[i] # 要排序的牌
            j = i - 1 # 已排序好的最大元素的索引（剩下没有对比的最大索引值）
            while j >= 0 and nums[j] > nums[i]:
                # nums[i], nums[j] = nums[j], nums[i]
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums

        