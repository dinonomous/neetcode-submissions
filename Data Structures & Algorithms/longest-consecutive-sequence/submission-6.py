class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        max_streek = 0

        for i in hash_set:
            if i-1 not in hash_set:
                curr_num = i
                streek = 1

                while curr_num+1 in hash_set:
                    curr_num = curr_num+1
                    streek+=1
                max_streek = max(max_streek, streek)
        return max_streek