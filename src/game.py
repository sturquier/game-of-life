#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from game_engine import GameEngine
"""
Game class
"""

class Game(object):

    def __init__(self):
        self.init_game()

    def init_game(self):
        print('Welcome to Game of Life !')
        rows_number = int(input('How many rows for your grid ?'))
        columns_number = int(input('How many columns for your grid ?'))

        new_game_engine = GameEngine(rows_number, columns_number)
        print(new_game_engine.display_grid())
