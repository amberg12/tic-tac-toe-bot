import board

class MiniMax_Search:
    def __init__(self, root):
        self.root = root
        moves = root.generate_moves()
        self.children = self.generate_children(self.root)
        print(self.children)
        
    def generate_children(self, root_board):
        moves = root_board.generate_moves()
        print(moves)
        children = []
        for move in moves:
            children.append(board.Board(board=root_board, move=move))
        return children

