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
            self.x_board += move
        else:
            self.o_board += move

        self.x_plays = not self.x_plays

    def generate_moves(self):
        combined_board = self.x_board | self.o_board
        move_pointer = 0b100000000
        moves = []

        for i in range(9):
            if (move_pointer >> i) & combined_board != (move_pointer >> i):
                moves.append(move_pointer >> i)

        return moves
    
    def generate_evaluation(self):
        win_states = [
            0b111000000,
            0b000111000,
            0b000000111,
            0b100100100,
            0b010010010,
            0b001001001,
            0b100010001,
            0b001010100
        ]

        for win_state in win_states:
            if self.x_board & win_state == win_state:
                return 1
            if self.o_board & win_state == win_state:
                return -1
            
        if self.x_board | self.o_board ==  0b111111111:
            return 0
        
        return None
    
    def display_board(self):
        if self.x_board & 0b1 == 0b1:
            print("X | ", end="")
        elif self.o_board & 0b1 == 0b1:
            print("O | ", end="")
        else:
            print("1 | ", end="")

        if self.x_board & 0b10 == 0b10:
            print("X | ", end="")
        elif self.o_board & 0b10 == 0b10:
            print("O | ", end="")
        else:
            print("2 | ", end="")

        if self.x_board & 0b100 == 0b100:
            print("X")
        elif self.o_board & 0b100 == 0b100:
            print("O")
        else:
            print("3")

        if self.x_board & 0b1000 == 0b1000:
            print("X | ", end="")
        elif self.o_board & 0b1000 == 0b1000:
            print("O | ", end="")
        else:
            print("4 | ", end="")

        if self.x_board & 0b10000 == 0b10000:
            print("X | ", end="")
        elif self.o_board & 0b10000 == 0b10000:
            print("O | ", end="")
        else:
            print("5 | ", end="")

        if self.x_board & 0b100000 == 0b100000:
            print("X")
        elif self.o_board & 0b100000 == 0b100000:
            print("O")
        else:
            print("6")

        if self.x_board & 0b1000000 == 0b1000000:
            print("X | ", end="")
        elif self.o_board & 0b1000000 == 0b1000000:
            print("O | ", end="")
        else:
            print("7 | ", end="")

        if self.x_board & 0b10000000 == 0b10000000:
            print("X | ", end="")
        elif self.o_board & 0b10000000 == 0b10000000:
            print("O | ", end="")
        else:
            print("8 | ", end="")

        if self.x_board & 0b100000000 == 0b100000000:
            print("X")
        elif self.o_board & 0b100000000 == 0b100000000:
            print("O")
        else:
            print("9")