## tic-tac-toe-bot
 tic-tac-toe game with a minimax algorithm bot
# simple minimax:
 |move|time|
 |--|--|
 |1|1188ms|
 |2|1281ms|
 |5|1563ms|

# alpha/beta pruning:
 |move|time|
 |--|--|
 |1|141ms|
 |2|266ms|
 |5|156ms|
 
# cache:
|move|time|
 |--|--|
 |1|47ms|
 |2|47ms|
 |5|36ms|

Further improvements could be reached by using transpositions when using the cache (most boards in tic tac toe are rotations of other boards), but most people wont be able to tell the difference at that point, and it would be more focussed on tic-tac-toe rather then the intent of this project - to experiment with minimax in a simpler environment before having to handle a more complex game such as chess.
