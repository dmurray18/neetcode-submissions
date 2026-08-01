class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        longest = 1
        solution = [0]
        nums.sort()
        for i in range(len(nums)-1):
            
            if nums[i] + 1 == nums[i+1]:
                longest += 1
                print(longest)
            elif nums [i] + 1 != nums[i+1] and nums[i] != nums [i+1]:
                solution.append(longest)
                longest = 1
            solution.append(longest)
        return max(solution)


        