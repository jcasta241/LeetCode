from typing import List

from solution import Solution


class TestSolution:
    solution = Solution()

    def _run_solution(self, nums: List[int], target: int, expected_output: List[int]):
        actual_output = self.solution.twoSum(nums, target)

        assert actual_output[0] == expected_output[0]
        assert actual_output[1] == expected_output[1]

    def test_case_1(self):
        self._run_solution(
            nums=[2, 7, 11, 15],
            target=9,
            expected_output=[0, 1]
        )

    def test_case_2(self):
        self._run_solution(
            nums=[3, 2, 4],
            target=6,
            expected_output=[1, 2]
        )

    def test_case_3(self):
        self._run_solution(
            nums=[3, 3],
            target=6,
            expected_output=[0, 1]
        )
