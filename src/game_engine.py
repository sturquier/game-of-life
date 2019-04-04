#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint
"""
Game Engine class
"""

class GameEngine(object):

    grid = []
    rows = 30
    columns = 30

    def __init__(self, rows, columns):
        self.grid = self.init_grid(rows, columns)

    def init_grid(self, rows, columns):
        """
        Initialize grid

        :param rows - int - number of rows
        :param colums - int - number of colums
        :return grid - int[][] - grid of cells
        """

        grid = []
        for row in range(rows):
            grid_rows = []
            for col in range(columns):
                grid_rows.append(randint(0, 1))
            grid.append(grid_rows)

        return grid

    def display_grid(self):
        return self.grid
