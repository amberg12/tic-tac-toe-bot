import math

class Player:
    def __init__(self):
        pass

    def generate_player_readable_moves(self, computer_readable_moves):
        player_readable_moves = [str(int(math.log2(move)) + 1) for move in computer_readable_moves]
        player_readable_moves.reverse()
        return player_readable_moves
    
    def generate_computer_readable_moves(self,  player_readable_moves):
        return [0b1 << int(player_readable_move) - 1 for player_readable_move in player_readable_moves]
    
    def get_player_response(self, computer_readable_moves):
        player_readable_moves = self.generate_player_readable_moves(computer_readable_moves)
        player_input = ""
        while player_input not in player_readable_moves:
            player_input = input(f"Please enter the move you would like to play in {player_readable_moves}: ")
        return self.generate_computer_readable_moves(player_input)[0]
