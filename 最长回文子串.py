class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = ""
        tag = 0
        for _s in s:
            if stack == "":
                stack += _s
                tag += 1

            else:
                for j in range(len(stack)):
                    if _s == stack[j]:
                        stack = stack[j+1:]
                        break

                stack += _s

                if len(stack) < tag:
                    pass
                else:
                    tag = len(stack)


        return tag

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))