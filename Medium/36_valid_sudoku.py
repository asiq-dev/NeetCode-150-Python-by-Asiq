
# 36. Valid Sudoku
    # Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    # Each row must contain the digits 1-9 without repetition.
    # Each column must contain the digits 1-9 without repetition.
    # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

import collections
from typing import List

# brute force solution:
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         for row in range(9):
#             seen = set()
#             for i in range(9):
#                 if board[row][i] == ".": 
#                     continue
#                 if board[row][i] in seen:
#                     return False
#                 seen.add(board[row][i])
        
#         for col in range(9):
#             seen = set()
#             for i in range(9):
#                 if board[i][col] == ".":
#                     continue
#                 if board[i][col] in seen:
#                     return False
#                 seen.add(board[i][col])
            
#         for square in range(9):
#             seen = set()
#             for i in range(3):
#                 for j in range(3):
#                     row = (square//3) * 3 + i
#                     col = (square % 3) * 3 + j
#                     if board[row][col] == ".":
#                         continue
#                     if board[row][col] in seen:
#                         return False
#                     seen.add(board[row][col])
#         return True

# hash map/ set
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        boxs = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in boxs[(r // 3, c // 3)]):
                    return False
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxs[(r // 3, c // 3)].add(board[r][c])
        return True



# testing
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

solution = Solution()
obj = solution.isValidSudoku(board)
print(obj)