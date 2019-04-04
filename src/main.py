#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from game_engine import GameEngine

"""
John Conway Game of Life
"""

def play_game():
    print('Welcome to Game of Life !')

    rows_number = int(input('How many rows for your grid ?'))
    columns_number = int(input('How many columns for your grid ?'))

    new_game = GameEngine(rows_number, columns_number)
    print(new_game.display_grid())

def main():
    play_game()

if __name__ == '__main__':
    main()
