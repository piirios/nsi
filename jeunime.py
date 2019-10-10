#!/usr/bin/python
# -*- coding: utf-8 -*-
##################
#paramètres du jeu
##################

nombre_allumette = 16

##################
# jeu POO
# avec bot /!\ uniquement pour nombre_allumette%4 == 0
##################

class jeu:
    def __init__(self, nrb):
        self.board = []
        for i in range(nrb):
            self.board.append('|')
    def printer(self):
        for i in range(len(self.board)):
            print(self.board[i], end='')
        print()
    def player(self):
        n = int(input("choississez un nombre entre 1 et 3:"))
        if 1<=n<=3:
            self.last = n
            for x in range(n):
                self.board.pop()
            self.printer()
        else:
            print('discalifié!')
    def bot(self):
        n = 4-self.last
        print('le bot a pris : ' + str(n))
        for x in range(n):
            self.board.pop()
        self.printer()

games = jeu(nombre_allumette)
games.printer()
while len(games.board) > 0:
    games.player()
    games.bot()
print('le bot a gagnée!')