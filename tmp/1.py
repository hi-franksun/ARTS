
from typing import List

from collections import Counter

"""169. 多数元素

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

1. 使用 hashmap 进行统计
2. 使用众数进行处理（但是不符合当前必有众数的情况就会失效）
3. 摩尔投票法（这种也存在问题，那就是没有众数的时候，也会失效）
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        这里是使用了 dict 这种数据进行了统计
        """
        dic = {}
        length = len(nums) / 2
        for i in nums:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        for k, v in dic.items():
            if v > length:
                return k

    def majorityElementTwo(self, nums: List[int]) -> int:
        """借助统计函数进行的简单化处理，也是 hashmap 的思路
        """
        length = len(nums) / 2
        for k, v in Counter(nums).items():
            if v > length:
                return k

    def majorityElementThree(self, nums: List[int]) -> int:
        """利用众数进行解决，因为题目说了总是有这个众数，所以排序，那么中间的一定是这个数字
        """
        length = len(nums) / 2
        for k, v in Counter(nums).items():
            if v > length:
                return k

    def majorityElementFour(self, nums: List[int]) -> int:
        """摩尔投票法
        """
        count = 0
        m = 0
        for n in nums:
            if count == 0:
                m = n
            if n == m:
                count += 1
            else:
                count -= 1
        return m
    

if __name__ == '__main__':

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            for l in range(i + 1, length]:
                if nums[i] + nums[l] == target:
                    return [i, l]
        return None