import board
import minimax
import player

if __name__ == "__main__":
    current_board = board.Board()
    player_interaface = player.Player()
    minimax_search = minimax.MiniMax_Search()
    while current_board.generate_evaluation() == None:
        current_board.display_board()
        current_board = board.Board(board=current_board, move=player_interaface.get_player_response(current_board.generate_moves()))

        if current_board.generate_evaluation() == None:
            current_board.display_board()
            current_board = board.Board(board=current_board, move=minimax_search.generate_move(current_board))

    current_board.display_board()
