class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)
        results = []

        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                results.append(num)

                if len(results) == k:
                    return results
