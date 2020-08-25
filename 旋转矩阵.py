class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i].reverse()

s = Solution()
print(s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))