#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from game_engine import GameEngine
"""
Game class

class in order to show and play the game
"""

class Game(object):

    rounds_number = 0

    def __init__(self):
        self.play_game()

    def play_game(self):
        print('Welcome to Game of Life !')
        try:
            rows_input = int(input('How many rows for your grid ? '))
            columns_input = int(input('How many columns for your grid ? '))
            rounds_input = int(input('How many rounds for your game ?'))
        except Exception as e:
            print(e)
        else:
            game_engine = GameEngine(rows_input, columns_input)

        while self.rounds_number <= rounds_input:
            game_engine.display_grid()
            print('\n\n')
            self.rounds_number += 1
