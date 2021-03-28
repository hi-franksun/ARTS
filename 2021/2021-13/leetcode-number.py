
from typing import List
import pytest


class Solution:
    """

    """
    def solution(self, nums):
        pass


class TestSolution:
    test_data_one = ()
    test_data_two =  ()

    @pytest.mark.parametrize('input_data, assert_data', [test_data_one, test_data_two])
    def test_solution(self, input_data, assert_data):
        assert Solution().solution(input_data) == assert_data
