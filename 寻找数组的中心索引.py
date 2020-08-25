class Solution(object):
    def pivotIndex(self, nums):
        s = sum(nums)
        left = 0
        for i, x in enumerate(nums):
            if left == s - left - x:
                return i
            left += nums[i]

        return -1

s = Solution()
print(s.pivotIndex([-1,-1,-1,-1,-1,0]))