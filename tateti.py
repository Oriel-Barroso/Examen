class TaTeTi():
    def __init__(self, board={}, valid=[], piece=''):
        self.board = {'1.1':'1.1','1.2':'1.2','1.3':'1.3',
                      '2.1':'2.1','2.2':'2.2','2.3':'2.3',
                      '3.1':'3.1','3.2':'3.2','3.3':'3.3'}
        self.valid = list(self.board.values())
        self.piece = piece
    def __str__(self):
        return '1.1|1.2|1.3\n---+---+---\n2.1|2.2|2.3\n---+---+---\n3.1|3.2|3.3'
    
    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, valor):
        self._board = valor
    
    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, valor):
        self._valid = valor
    
    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, valor):
        self._piece = valor

    def input_position(self):
        while True:
            a = str(input('posicion a eliminar: '))
            if a not in self.board.values():
                print('posicion incorrecta')
            else:
                self.valid.remove(a)
                return a
                break

    def win(self):
        board = list(self.board.values())
        print(board)
        row = board[0] == board[1] == board[2]
        if row is True:
            return True
        row = board[3] == board[4] == board[5]
        if row is True:
            return row
        row = board[6] == board[7] == board[8]
        if row is True:
            return row
        row = board[0] == board[3] == board[6]
        if row is True:
            return row
        row = board[1] == board[4] == board[7]
        if row is True:
            return row
        row = board[2] == board[5] == board[8]
        if row is True:
            return row
        row = board[0] == board[4] == board[8]
        print(f'Este es el row {row}, posicion 0 {board[0]}, posicion 4 {board[4]}, posicion 8 {board[8]}')
        if row is True:
            return row
        row = board[2] == board[4] == board[6]
        if row is True:
            return row
        return False

    def game(self):
        print(self)
        while not self.win() and len(self.valid) > 0:
            self.board[self.input_position()] = ' ' + self.piece + ' '
            print(self)
            winner = self.piece
            self.piece = 'o' if self.piece == 'x' else 'x'
            if len(self.valid) == 0:
                winner = 'Ninguno'
            return winner




if __name__ == '__main__':
    game = TaTeTi()
    game.input_position()
