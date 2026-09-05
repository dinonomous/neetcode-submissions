from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_all = defaultdict(int)
        for i in nums:
            hash_all[i] += 1
        
        min_heap = []
        for num, freq in hash_all.items():
            heapq.heappush(min_heap, (freq,num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        result = []
        for freq, num in min_heap:
            result.append(num)
            
        return result
