class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        answer = []
        for start in range(len(nums)):
            for i in range(len(nums)):
                if start != i and (nums[start] + nums[i] == target):
                    answer.append(start)
                    answer.append(i)
                    return answer
            start +=1
        

        