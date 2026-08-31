class TimeMap:

    def __init__(self):
        self.m = {}

    def set(self, key, value, timestamp):
        self.m.setdefault(key, []).append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.m:
            return ""

        arr = self.m[key]
        l, r = 0, len(arr) - 1
        ans = ""

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return ans