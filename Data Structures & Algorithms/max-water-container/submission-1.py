class Solution:
    def area(self, h:int, w:int) -> int:
        return h * w

    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights)-1
        a_max = 0

        while p1 < p2:
            a_max = max(a_max, self.area(min(heights[p1],heights[p2]),p2-p1))

            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return a_max
            

        