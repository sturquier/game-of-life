#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint
"""
Game Engine class

class with all stuf to create the game
"""

class GameEngine(object):

    grid = []

    def __init__(self, rows, columns):
        self.grid = self.init_grid(rows, columns)

    def init_grid(self, rows, columns):
        """
        Initialize grid

        Args
        ----
        rows - int - number of rows
        colums - int - number of colums

        Return
        ------
        grid - int[][] - grid of cells
        """

        grid = []
        for row in range(rows):
            grid_rows = []
            for col in range(columns):
                grid_rows.append(randint(0, 1))
            grid.append(grid_rows)

        return grid
    
    def __str__(self):
        """
        Display grid line by line
        """
        return "\n".join(map(str, self.grid))

    def update_grid(self):
        """
        Update the grid by create a new one with the next value

        Return
        ------
        grid - list
        """
        next_grid = []
        for i,row in enumerate(self.grid):
            next_row = []
            for col in row:
                self.get_neighbourhood(i,row)
                # TODO : update value
                self.grid[i][col] = 0
                next_row.append(self.grid[i][col])
            next_grid.append(next_row)
        print(next_grid)

    def get_neighbourhood(self, row, column):
        """
        Display neighbour cells count of a specific cell

        Args
        ----
        row - int - row of a specific cell
        column - int - column of a specific cell

        Return
        ------
        neighbours - int
        """
        # print(row)
        # print(column)
