import os
from BoardGUI.GoAI import searcher
from BoardGUI.chess_board import ChessBoard

EMPTY = 0
BLACK = 1
WHITE = 2

# ai_1 = searcher()
# print(ai_1)

class Game(object):

### alpha-beta vs alpha-beta

    def ab_vs_ab(self):
        step = 0
        board = ChessBoard()
        ab_ab_end = False
        ## BLACK goes first
        ini_x = 9
        ini_y = 9
        board.draw_xy(ini_x,ini_y,BLACK)
        print("BLACK Places at position :",ini_x,ini_y)
        step = step + 1
        ai_1 = searcher()
        ai_2 = searcher()

        while ab_ab_end == False:

            # ai 2 place chess
            ai_2.board = board.board()
            score_2,x_2,y_2 = ai_2.search(WHITE,2)
            print("WHITE Places at position :", x_2, y_2,"Score:",score_2)
            board.draw_xy(x_2,y_2,WHITE)
            step = step + 1
            winner = board.anyone_win(x_2,y_2)
            if winner != EMPTY:
                if winner == BLACK:
                    print("Winner is Black")
                else:
                    print("Winner is WHITE")
                ab_ab_end = True
                break

            # ai 1 place chess
            ai_1.board = board.board()
            score_1,x_1,y_1 = ai_1.search(BLACK,2)
            print("BLACK Places at position :", x_1, y_1, "Score:", score_1)
            board.draw_xy(x_1,y_1,BLACK)
            step = step + 1
            winner = board.anyone_win(x_1, y_1)
            if winner != EMPTY:
                if winner == BLACK:
                    print("Winner is Black")
                else:
                    print("Winner is WHITE")
                ab_ab_end = True
                break

    def mc_vs_mc(self):
        print("Monte Carlo AI vs. Monte Carlo AI")





# Black vs White


### MCTS vs MCTS


### Competition

if __name__ == "__main__":
    Game = Game()
    Game.ab_vs_ab()