from Validate_Sudoku import *

class Solving_sudoku:
    empty_sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def __init__(self, *cord_num):
        self.cord_num = cord_num


    def completing_sudoku(self) -> list:
        ''' function for filling sudoku '''
        for cord in self.cord_num:
            self.empty_sudoku[cord[0]][cord[1]] = cord[2]
        return self.empty_sudoku


    def available_numbers(self, row_index: int, colum_index: int) -> set:
        ''' function for checking columns, rows and individual squares '''
        full_set_numbers = {1,2,3,4,5,6,7,8,9}
        possible_numbers = set()

        for row_num in self.empty_sudoku[row_index]:
            if row_num != 0:
                possible_numbers.add(row_num)

        for colum_num in self.empty_sudoku:
            if colum_num[colum_index] != 0:
                possible_numbers.add(colum_num[colum_index])

        start_colum, end_colum = 0, 0
        start_row, end_row = 0, 0

        if colum_index < 3:
            start_colum, end_colum = 0 , 3
        elif colum_index >= 3 and colum_index < 6:
            start_colum, end_colum = 3 , 6
        elif colum_index >= 6:
            start_colum, end_colum = 6 , 9

        if row_index < 3:
            start_row, end_row = 0 , 3
        elif row_index >= 3 and row_index < 6:
            start_row, end_row = 3 , 6
        elif row_index >= 6:
            start_row, end_row = 6 , 9

        for index in range(start_row, end_row):
            for number in self.empty_sudoku[index][start_colum: end_colum]:
                if number != 0:
                    possible_numbers.add(number)

        return full_set_numbers - possible_numbers


    def count_ava_num_for_row(self, row_index: int) -> dict:
        ''' function to count the available numbers in a row '''
        ava_row_num = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        for ind in range(9):
            if self.empty_sudoku[row_index][ind] == 0:
                for number in self.available_numbers(row_index, ind):
                    ava_row_num[number] += 1
        return ava_row_num


    def count_ava_num_for_colum(self, colum_index: int) -> dict:
        ''' function to count the available numbers in a colum '''
        ava_colum_num = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        for ind in range(9):
            if self.empty_sudoku[ind][colum_index] == 0:
                for number in self.available_numbers(ind, colum_index):
                    ava_colum_num[number] += 1
        return ava_colum_num


    def double_bets_for_row(self, row_index: int) -> set:
        ''' function for finding duplicate pairs in a row '''
        double_num = []
        for ind in range(9):
            if self.empty_sudoku[row_index][ind] == 0:
                ava_num_for_point = self.available_numbers(row_index, ind)
                doub_num_for_squar = self.double_bets_for_squares(row_index, ind)
                ava_num = ava_num_for_point - doub_num_for_squar
                if len(ava_num) == 2:
                    double_num.append(tuple(ava_num))
                elif len(ava_num) == 0:
                    double_num.append(tuple(ava_num_for_point))

        for bets in double_num:
            if double_num.count(bets) == 2:
                return set(bets)
        return set()


    def double_bets_for_colum(self, colum_index: int) -> set:
        ''' function for finding duplicate pairs in a column '''
        double_num = []
        for ind in range(9):
            if self.empty_sudoku[ind][colum_index] == 0:
                ava_num_for_point = self.available_numbers(ind, colum_index)
                doub_num_for_squar = self.double_bets_for_squares(ind, colum_index)
                ava_num = ava_num_for_point - doub_num_for_squar
                if len(ava_num) == 2:
                    double_num.append(tuple(ava_num))
                elif len(ava_num) == 0:
                    double_num.append(tuple(ava_num_for_point))

        for bets in double_num:
            if double_num.count(bets) == 2:
                return set(bets)
        return set()


    def double_bets_for_squares(self, row_index: int, colum_index: int) -> set:
        ''' function for finding duplicate pairs in a square '''
        start_colum, end_colum = 0, 0
        start_row, end_row = 0, 0

        if colum_index < 3:
            start_colum, end_colum = 0 , 3
        elif colum_index >= 3 and colum_index < 6:
            start_colum, end_colum = 3 , 6
        elif colum_index >= 6:
            start_colum, end_colum = 6 , 9

        if row_index < 3:
            start_row, end_row = 0 , 3
        elif row_index >= 3 and row_index < 6:
            start_row, end_row = 3 , 6
        elif row_index >= 6:
            start_row, end_row = 6 , 9

        count_zero = 0
        double_num = []
        for index_row in range(start_row, end_row):
            for index_colum in range(start_colum, end_colum):
                if self.empty_sudoku[index_row][index_colum] == 0:
                    count_zero += 1
                    ava_num = self.available_numbers(index_row, index_colum)
                    if len(ava_num) == 2:
                        double_num.append(tuple(ava_num))

        for bets in double_num:
            if double_num.count(bets) == 2 and count_zero != 2:
                return set(bets)
        return set()


    def sudoku_solution(self) -> list:
        ''' function for solving sudoku (completes the sudoku puzzle only once) '''
        count_zero = 81 - len(self.cord_num)
        stop_iter = 0
        while count_zero > 0 and stop_iter < 20:
            start_row , end_row = 0 , 3

            for step_level_1 in range(3):
                start_colum , end_colum = 0 , 3

                for step_level_2 in range(3):
                    Count_squares = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

                    for step_level_3 in range(2):

                        for index_row in range(start_row, end_row):
                            for index_number in range(start_colum, end_colum):
                                if self.empty_sudoku[index_row][index_number] == 0:
                                    double_bets_for_row: set = self.double_bets_for_row(index_row)
                                    double_bets_for_colum: set = self.double_bets_for_colum(index_number)
                                    double_bets_for_squares: set = self.double_bets_for_squares(index_row, index_number)
                                    ava_num_for_point: set = self.available_numbers(index_row, index_number) - double_bets_for_colum - double_bets_for_row - double_bets_for_squares

                                    if step_level_3 == 0:
                                        stop_checking = False

                                        if len(ava_num_for_point) == 1:
                                            self.empty_sudoku[index_row][index_number] = list(ava_num_for_point)[0]
                                            count_zero -= 1
                                            stop_checking = True

                                        if stop_checking == False:
                                            count_row_num = self.count_ava_num_for_row(index_row)
                                            if len(double_bets_for_row) == 2:
                                                count_row_num.pop(list(double_bets_for_row)[0])
                                                count_row_num.pop(list(double_bets_for_row)[1])
                                            for number_row, count_num_row in count_row_num.items():
                                                if count_num_row == 1 and number_row in ava_num_for_point:
                                                    self.empty_sudoku[index_row][index_number] = number_row
                                                    count_zero -= 1
                                                    stop_checking = True

                                        if stop_checking == False:
                                            count_colum_num: dict = self.count_ava_num_for_colum(index_number)
                                            if len(double_bets_for_colum) == 2:
                                                count_colum_num.pop(list(double_bets_for_colum)[0])
                                                count_colum_num.pop(list(double_bets_for_colum)[1])
                                            for number_colum, count_num_colum in count_colum_num.items():
                                                if count_num_colum == 1 and number_colum in ava_num_for_point:
                                                    self.empty_sudoku[index_row][index_number] = number_colum
                                                    count_zero -= 1
                                                    stop_checking = True

                                        if stop_checking == False:
                                            ava_num: set = self.available_numbers(index_row, index_number) - double_bets_for_squares
                                            for number in ava_num:
                                                Count_squares[number] += 1

                                    elif step_level_3 == 1:
                                        for number in ava_num_for_point:
                                            if Count_squares[number] == 1:
                                                self.empty_sudoku[index_row][index_number] = number
                                                count_zero -= 1

                    start_colum += 3
                    end_colum += 3
                start_row += 3
                end_row += 3
            stop_iter += 1

        return self.empty_sudoku

if __name__ == '__main__':
    # S = Solving_sudoku([0,5,4], [0, 6, 5], [0, 7, 3], [0, 8, 1], [1, 0, 8], [1, 1, 3], [1, 2, 1], [1, 5, 7], [1, 6, 6], [1, 8, 9], [2, 0, 5], [2, 1, 4], [2, 2, 9], [2, 6, 8], [2, 8, 7], [3, 1, 2], [3, 3, 5], [3, 5, 1], [3, 7, 7], [4, 0, 4], [4, 1, 1], [4, 6, 9], [4, 7, 6], [5, 1, 6], [5, 2, 3], [5, 4, 2], [6, 4, 3], [6, 6, 4], [6, 7, 9], [6, 8, 6], [7, 1, 9], [7, 3, 7], [7, 4, 4], [7, 7, 1], [8, 0, 2], [8, 1, 8], [8, 5, 6], [8, 6, 7])
    S= Solving_sudoku([ 0 , 3 , 8 ], [0, 8, 9], [1, 3, 2], [1, 4, 7], [1, 5, 3], [2, 3, 5], [2, 6, 1], [2, 8, 8], [3, 1, 8], [3, 4, 4], [4, 2, 5], [4, 5, 7], [5, 2, 1], [5, 7, 4], [5, 8, 6], [6, 6, 3], [7, 0, 2], [7, 1, 3], [7, 7, 8], [8, 0, 7], [8, 4, 5], [8, 6, 2])
    # S=Solving_sudoku([1,0,3], [1, 1, 5], [1, 2, 1], [1, 3, 6], [1, 6, 9], [0, 8, 3], [2, 0, 4], [2, 2, 9], [2, 8, 7], [3, 1, 7], [3, 6, 1], [3, 7, 9], [4, 0, 9], [4, 1, 4], [4, 2, 6], [4, 4, 5], [4, 6, 8], [5, 0, 1], [5, 3, 3], [5, 8, 5], [6, 3, 4], [6, 4, 1], [6, 5, 5], [7, 2, 5], [7, 5, 3], [8, 5, 8], [8, 7, 6], [8, 8, 1])
    # S=Solving_sudoku([ 0 , 1 , 1 ], [0,2,6], [0,3,7], [0,5,5], [0,6,3], [1,0,4], [1,4,6], [2,0,2], [2,8,1], [3,0,6], [4,5,3], [4,7,8], [5,1,9], [5,2,7], [5,4,5], [5,8,4], [6,1,2], [7,3,9], [7,6,4], [8,1,5], [8,2,1], [8,4,7], [8,8,9])
    # S=Solving_sudoku([0,2,1],[0,4,4], [0,6,6], [1,2,9],[1,7,3],[2,2,7],[2,5,6],[2,6,5],[2,8,9],[3,0,4],[3,4,2],[3,7,5],[3,8,7],[4,0,2],[4,7,9],[5,0,7],[5,1,5],[5,2,3],[5,5,1],[5,7,8],[6,5,3],[6,7,1],[6,8,5],[7,3,2],[7,6,7],[7,8,3],[8,3,6],[8,5,5])
    # S = Solving_sudoku([0,2,3],[0,4,1],[0,5,9],[0,8,7],[1,0,1],[1,1,2],[1,3,7],[1,5,4],[1,8,5],[2,7,3],[3,4,6],[3,5,8],[3,6,7],[3,7,2],[4,1,7],[5,0,2],[5,3,1],[5,4,9],[6,2,4],[6,5,6],[6,6,1],[6,7,7],[7,6,9],[8,0,8],[8,3,4],[8,4,7],[8,5,3],[8,7,5])
    print(*S.completing_sudoku(), sep='\n')
    print('---------------------------')
    print(*S.sudoku_solution(), sep='\n')
    R = Validate_sudoku(S.empty_sudoku)
    print(R.is_valid())
