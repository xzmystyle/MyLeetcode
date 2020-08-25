class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        暴力破解版
        """
        if len(intervals) < 2:  # 如果长度小于2，直接输出
            return intervals
        intervals = sorted(intervals, key=lambda x:x[0]) # 按intervals左区间排序
        merged = []  # 设置存放合并后的区间的列表
        merged.append(intervals[0])  # 初始化为intervals区间里的第一个值
        point = 0  # 设置指针始终指向merged中目前要操作的区间

        for i in range(1, len(intervals)):  # 从intervals区间列表中的第二位开始循环与merged中的point所指区间对比
            temp = intervals[i]
            if temp[0] >= merged[point][0] and temp[0] <= merged[point][1]:
                if temp[1] <= merged[point][1]:
                    continue  # 当前intervals区间属于merged当前操作的区间内
                else:
                    merged.append([merged[point][0], temp[1]])  # 区间合并并添加
                    merged.pop(point)  # 将merged当前的区间pop出去

            else:
                merged.append(temp)  # 与当前intervals区间无关联，直接合并
                point += 1  # 将指针移向下一个待操作区间

        return merged



s = Solution()
print(s.merge([[1,4],[0,4]]))