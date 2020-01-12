import Board
import numpy as np
from datetime import datetime as dtt


class Solver:

    def __init__(self):

        board_1 = Board.Board()
        self.board = board_1.GetBoard()

        print(self.board)

        self.filled_list = []
        self.filled_already(self.board)
        start_time = dtt.now()
        print('solution :')
        self.backtracking(0, 0)
        end_time = dtt.now()
        print('\n')
        print('Start time:', start_time)
        print('End time: ', end_time)
        print('Difference: ', (end_time - start_time).total_seconds())

    def filled_already(self, arr):

        for x in range(0, arr.shape[0]):
            for y in range(0, arr.shape[1]):
                if arr[x][y] == 0:
                    continue
                else:
                    self.filled_list.append([x, y])

        # print(self.filled_list)

    def isValid(self, x, y, value):
        temp_lst = self.board[x, :]
        if value in temp_lst:
            return False
        temp_lst = self.board[:, y]
        if value in temp_lst:
            return False
        temp_lst = self.board[x - x % 3:x - x % 3 + 3, y - y % 3:y - y % 3 + 3]
        if value in temp_lst:
            return False
        return True

    def next_cell(self, x, y):
        if x < 8:
            return [x + 1, y]
        else:
            return [0, y + 1]

    def backtracking(self, x, y):

        if y > 8:
            print(self.board)
            return True

        if [x, y] not in self.filled_list:
            for i in range(1, 11):
                if i == 10:
                    self.board[x,y] = 0
                    return False
                if self.isValid(x, y, i):
                    self.board[x][y] = i
                    newcell = self.next_cell(x, y)
                    if self.backtracking(newcell[0], newcell[1]):
                        return True

        newcell = self.next_cell(x, y)
        if self.backtracking(newcell[0], newcell[1]):
            return True


solver_1 = Solver()
