import board
import time

class MiniMax_Search:
    def __init__(self):
        pass
        
    def generate_children(self, root_board):
        moves = root_board.generate_moves()
        children = []
        for move in moves:
            children.append(board.Board(board=root_board, move=move))
        return children
    
    def generate_move(self, root_board):
        initial_time = time.process_time()
        moves = root_board.generate_moves()
        children = []
        for move in moves:
            children.append(board.Board(board=root_board, move=move))

        children_scores = []
        for child in children:
            children_scores.append(self.minimax(child, not root_board.x_plays))

        best_move = -1
        
        if root_board.x_plays:
            value = -9999
            for i, child_score in enumerate(children_scores):
                if value < child_score:
                    best_move = moves[i]
                    value = child_score
        else:
            value = 9999
            for i, child_score in enumerate(children_scores):
                if value > child_score:
                    best_move = moves[i]
                    value = child_score
        print(f"{1000*(time.process_time() - initial_time)}ms to calculate.")
        return best_move

    def minimax(self, node, is_maxxing, depth=10, alpha=-9999, beta=9999, cache={}):

        if cache.get(node.x_board << 9 + node.o_board, None) != None:
            return cache.get(node.x_board << 9 + node.o_board, None)

        if node.generate_evaluation() != None:
            cache[node.x_board << 9 + node.o_board] = node.generate_evaluation()
            return node.generate_evaluation()
        
        if depth == 0:
            raise RecursionError("Expected depth exceeded")

        self.children = self.generate_children(node)

        if is_maxxing == True:
            value = -9999
            for child in self.children:
                child_value = self.minimax(child, False, depth=depth-1, alpha=alpha, beta=beta)
                cache[child.x_board << 9 + child.o_board] = child_value
                value = max(value, child_value)
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return value
        else:
            value = 9999
            for child in self.children:
                child_value = self.minimax(child, True, depth=depth-1, alpha=alpha, beta=beta)
                cache[child.x_board << 9 + child.o_board] = child_value
                value = min(value, child_value)
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value

