# -*- coding: utf-8 -*-
"""
@Time: 2021/4/23 14:34
@Author: puffy
@FileName: 旋转数组.py
"""

# aa = [[1]]

aa = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 0, 1, 2],
      [9, 0, 1, 2]]

# aa = [[1, 2, 3, 4],
#       [5, 6, 7, 8],
#       [9, 0, 1, 2]]

# aa = [[1, 2, 3],
#       [5, 6, 7],
#       [9, 0, 1],
#       [9, 0, 1]]


def ORZ(matrix):
    n_row = len(matrix)
    n_line = len(matrix[0])

    if n_line == 1 and n_row == 1:
        res = [matrix[0][0]]

    else:
        res = []
        for n in range((min(n_line, n_row) + 1) // 2):
            [res.append(matrix[n][i]) for i in range(n, n_line - n) if len(res) != n_line * n_row]
            [res.append(matrix[i][n_line - n - 1]) for i in range(n + 1, n_row - n - 1) if len(res) != n_line * n_row]
            [res.append(matrix[n_row - 1][-i]) for i in range(n + 1, n_line - n + 1) if len(res) != n_line * n_row]
            [res.append(matrix[i][n]) for i in range(n_row - n - 2, n, -1) if len(res) != n_line * n_row]

    return res


print(ORZ(aa))
