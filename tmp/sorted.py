# Bubble Sort

from typing import List
import pytest


class Solution():
    def bubbleSortOne(self, nums: List) -> List:
        length = len(nums)
        count = 0
        for i in range(length):
            for l in range(0, length-1):
                count += 1
                if nums[l] > nums[l+1]:
                    nums[l], nums[l+1] = nums[l+1], nums[l]
        print(count)
        return nums

    def bubbleSortTwo(self, nums: List) -> List:
        length = len(nums)
        count = 0
        for i in range(length):
            flag = False
            for l in range(0, length-1-i):
                count += 1
                if nums[l] > nums[l+1]:
                    nums[l], nums[l+1] = nums[l+1], nums[l]
        print(count)
        return nums

    def bubbleSortThree(self, nums: List) -> List:
        length = len(nums)
        count = 0
        for i in range(length):
            flag = False
            for l in range(0, length-1-i):
                count += 1
                if nums[l] > nums[l+1]:
                    nums[l], nums[l+1] = nums[l+1], nums[l]
                    flag = True
            if flag is False:
                break
        print(count)
        return nums

    def insertSord(self, nums: List) -> List:
        length = len(nums)
        count = 0
        for i in range(1, length):
            key = nums[i] # 要排序的牌
            j = i - 1 # 已排序好的最大元素的索引（剩下没有对比的最大索引值）
            while j >= 0 and nums[j] > nums[i]:
                count += 1
                # nums[i], nums[j] = nums[j], nums[i]
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        print(count)
        return nums


class TestBubbleSort():

    test_data_one = ([4, 5, 6, 3, 2, 1], [1, 2, 3, 4, 5, 6])

    @pytest.mark.parametrize('input_data, assert_data', [test_data_one])
    def test_bubble_sort(self, input_data, assert_data):
        assert Solution().bubbleSortThree(input_data) == assert_data

    @pytest.mark.parametrize('input_data, assert_data', [test_data_one])
    def test_insert_sort(self, input_data, assert_data):
        assert Solution().insertSord(input_data) == assert_data


if __name__ == '__main__':
    import random
    import time
    data = [random.randint(0, 1000) for _ in range(10000)]
    
    # start = time.time()
    # result = Solution().bubbleSortOne(data)
    # print(result)
    # end = time.time()
    # print(f'spend time is {end-start}' )

    # result = Solution().bubbleSortTwo(data)
    # print(result)

    # start = time.time()
    # result = Solution().bubbleSortThree(data)
    # end = time.time()
    # print(f'spend time is {end-start}')

    start = time.time()
    result = Solution().insertSord(data)
    end = time.time()
    print(f'spend time is {end-start}')