class Solution:
    def largestRectangleArea(self, heights):
        stack = [-1]
        ans = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                area = h * w

                if area > ans:
                    ans = area

            stack.append(i)

        n = len(heights)

        while stack[-1] != -1:
            h = heights[stack.pop()]
            w = n - stack[-1] - 1
            area = h * w

            if area > ans:
                ans = area

        return ans