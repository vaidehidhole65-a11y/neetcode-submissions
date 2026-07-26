class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # Step 2: Sort the numbers based on their counts (in descending order)
        # key=count.get tells Python to sort 'num' using its frequency from the dictionary
        sorted_nums = sorted(count.keys(), key=count.get, reverse=True)
        
        # Step 3: Return the top k elements
        return sorted_nums[:k]