import board

class MiniMax_Search:
    def __init__(self, root):
        self.root = root
        moves = root.generate_moves()
        self.children = self.generate_children(self.root)
        
    def generate_children(self, root_board):
        moves = root_board.generate_moves()
        children = []
        for move in moves:
            children.append(board.Board(board=root_board, move=move))
        return children
    
    def minimax(self, node, is_maxxing, depth=10):

        if node.generate_evaluation() != None:
            return node.generate_evaluation()
        
        if depth == 0:
            raise RecursionError("Expected depth exceeded")

        self.children = self.generate_children(node)

        if is_maxxing == True:
            value = -9999
            for child in self.children:
                value = max(value, self.minimax(child, False, depth=depth-1))
            return value
        else:
            value = 9999
            for child in self.children:
                value = min(value, self.minimax(child, True, depth=depth-1))
            return value

