class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers = sorted(numbers)
        solution = []
        l,r=0,len(numbers)-1
        value = numbers[l]+numbers[r]
        while value != target:
            value = numbers[l]+numbers[r]
            if value > target:
                r -=1
            if value < target:
                l+=1
        solution.append(l+1)
        solution.append(r+1)
        return solution