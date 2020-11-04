class TaTeTi():
    def __init__(self, board=[], valid=[], piece=''):
        self.board = board
        self.valid = valid
        self.piece = piece

    def __str__(self):
        expected = '1.1|1.2|1.3\n---+---+---\n2.1|2.2|2.3\n'
        expected += '---+---+---\n3.1|3.2|3.3'
        return expected

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, positions):
        positions = {'1.1': '1.1', '1.2': '1.2', '1.3': '1.3',
                     '2.1': '2.1', '2.2': '2.2', '2.3': '2.3',
                     '3.1': '3.1', '3.2': '3.2', '3.3': '3.3'}
        self._board = positions

    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, valid):
        valid = ['1.1', '1.2', '1.3',
                 '2.1', '2.2', '2.3',
                 '3.1', '3.2', '3.3']
        self._valid = valid

    @property
    def piece(self):
        return self._piece

    @piece.setter
    def piece(self, valor):
        self._piece = valor

    def input_position(self):
        estate = True
        valor = self.valid
        while estate:
            position = str(input('Valor: '))
            for valor1 in valor:
                if position != valor1:
                    print('Error')
                else:
                    valor.remove(position)
                    estate = False
        return position

    def win(self):
        s = True
        valor = self._board.items()
        valor = list(valor)
        while s:
            for v in self._valid:
                for v1 in valor:
                    print(valor)
                    if v1 != v or v1 != v:
                        return False
                    else:
                        return True
                        s = False

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
    print('Ganó ' + game.game())
