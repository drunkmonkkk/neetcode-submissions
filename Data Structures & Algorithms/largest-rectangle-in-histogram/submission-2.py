from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (start index, height)
        maxArea = 0

        for i, height in enumerate(heights + [0]):
            start = i

            while stack and stack[-1][1] > height:
                left, h = stack.pop()
                maxArea = max(maxArea, h * (i - left))
                start = left

            stack.append((start, height))

        return maxArea