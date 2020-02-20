class Solution:

    def isValidSudoku(self, board):

        # To map the row and col index to an index from 0 to 8 for the 3x3 quadratic cells.
        def rowColToThreeCell(row, col):
            return (row // 3) + 3 * (col // 3)

        # Lists of sets to ensure that a sudoku element
        # can just be once in a row, column, or 3x3 cell
        columns = [set() for i in range(9)]
        rows = [set() for i in range(9)]
        threeCells = [set() for i in range(9)]

        # Go through every single number of the sudoku board
        for row_idx in range(9):
            for col_idx in range(9):

                # Get the board element at row_idx and col_idx
                board_element = board[row_idx][col_idx]

                # Only if the current element is number a check has to be performed
                if board_element != ".":

                    # Run three checks if the element is already contained in its
                    # column, row or 3x3 cell. Return False if that is the case otherwise add it.
                    if board_element in columns[col_idx]:
                        return False
                    else:
                        columns[col_idx].add(board_element)

                    if board_element in rows[row_idx]:
                        return False
                    else:
                        rows[row_idx].add(board_element)

                    threeCellIdx = rowColToThreeCell(row_idx, col_idx)

                    if board_element in threeCells[threeCellIdx]:
                        return False
                    else:
                        threeCells[threeCellIdx].add(board_element)

        # If no duplicate element has been found the board configuration is valid and true can be returned
        return True
