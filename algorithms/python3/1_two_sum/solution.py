from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        required_dict = dict()

        for idx, num in enumerate(nums):
            required_num = target - num

            if required_num in required_dict:
                return (required_dict[required_num], idx)

            required_dict[num] = idx
