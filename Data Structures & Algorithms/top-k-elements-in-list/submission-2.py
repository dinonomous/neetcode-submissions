from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_all = defaultdict(int)
        for i in nums:
            hash_all[i] += 1
        finalList = sorted(hash_all, key=hash_all.get, reverse=True)
        return finalList[:k]