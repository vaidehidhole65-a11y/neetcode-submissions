class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # stores indices
        l = r = 0

        while r < len(nums):
            # Remove smaller numbers from the back of deque as they are useless
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            # Remove index from front if it's out of the current sliding window
            if l > q[0]:
                q.popleft()

            # Append the max element (front of deque) once window size reaches k
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1

        return output
