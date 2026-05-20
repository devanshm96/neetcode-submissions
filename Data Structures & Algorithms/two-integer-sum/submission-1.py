class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hmap={}

        # for i, n in enumerate(nums):
        #     diff = target - n

        #     if diff in hmap:
        #         return [hmap[diff], i]
            
        #     hmap[n] = i
        
        ans = [0]*2
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    ans[0] = i
                    ans[1] = j
                    return ans
        return ans