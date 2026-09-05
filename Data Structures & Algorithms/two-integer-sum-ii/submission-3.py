class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers)-1

        s = numbers[p1]+numbers[p2]

        while s != target:
            if numbers[p1]+numbers[p2] == target:
                break

            elif numbers[p1]+numbers[p2] > target:
                p2-=1

            elif numbers[p1]+numbers[p2] < target:
                p1+=1

            s = numbers[p1] + numbers[p2]
        
        return [p1+1, p2+1]
        