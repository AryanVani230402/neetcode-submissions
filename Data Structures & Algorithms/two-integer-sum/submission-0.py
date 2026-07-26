class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        ans = [0]*2
        for i in range(len(nums)):
            if (target - nums[i]) in map:
                ans[0] = map.get(target - nums[i])
                ans[1] = i
                return ans
            
            map[nums[i]] = i
        return ans
