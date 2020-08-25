class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        low = 0
        high = len(x) - 1

        while low < high:
            if x[low] != x[high]:
                return False

            else:
                low += 1
                high -= 1

        return True

s = Solution()
s.isPalindrome(10)