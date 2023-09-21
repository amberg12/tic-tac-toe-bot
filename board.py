class Board:
    def __init__(self, board=False, move=None):
        if board == False:
            self.x_board = 0b000000000
            self.o_board = 0b000000000
            self.x_plays = True
        else:
            self.x_board = board.x_board
            self.o_board = board.o_board
            self.x_plays = board.x_plays
            self.process_move(move)

    def process_move(self, move):
        if self.x_plays:
            self.x_board = self.x_board | move
        else:
            self.o_board = self.o_board | move

        self.x_plays = not self.x_plays

    def generate_moves(self):
        combined_board = self.x_board | self.o_board
        move_pointer = 0b100000000
        moves = []

        for i in range(9):
            if (move_pointer >> i) & combined_board != (move_pointer >> i):
                moves.append(move_pointer)

        return moves