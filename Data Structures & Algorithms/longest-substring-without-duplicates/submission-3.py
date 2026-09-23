class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        total = 0
        left = 0

        for right, v in enumerate(s):
            if v in hash_map and hash_map[v] >= left:
                left = hash_map[v] + 1

            hash_map[v] = right
            total = max(total, right - left +1)
        
        return total

