EMPTY = 0
BLACK = 1
WHITE = 2

from chess_board import ChessBoard

class evaluation(object):

    def __init__(self):
        self.POS = []
        for i in range(19):
            row = [(7-max(abs(i-7),abs(j-7))) for j in range(19)]
            self.POS = tuple(self.POS)

        self.STWO = 1 #冲二
        self.STHREE = 2 #冲三
        self.SFOUR = 3 #冲四
        self.TWO = 4 #活二
        self.THREE = 5 #活三
        self.FOUR = 6 #活四
        self.FIVE = 7 #活五
        self.DFOUR = 8 #双四
        self.FOURT = 9 #四三
        self.DTHREE = 10 #双三
        self.NOTYPE = 11
        self.ANALYSED = 255 # has been analysed
        self.TODO = 0 # haven't been analysed
        self.result = [0 for i in range(30)]
        self.line = [0 for i in range(30)]
        self.record = []
        for i in range(19):
            self.record.append([])
            self.record[i] = []

            for j in range(19):
                self.record[i].append([0,0,0,0])
        sl

