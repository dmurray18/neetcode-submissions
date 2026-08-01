class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solution = []
        
        for i in range(len(nums)):
            answer = 1
            for x in  range(len(nums)):
                if x != i:
                    answer = answer * nums[x]
            solution.append(answer)
        return solution


        