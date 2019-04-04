#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint
"""
Game Engine class

class with all stuf to create the game
"""

class GameEngine(object):

    grid = []
    rows = 0
    columns = 0

    def __init__(self, rows, columns):
        self.grid = self.init_grid(rows, columns)
        self.rows = rows
        self.columns = columns

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

    def display_grid(self):
        """
        Display grid
        """
        for row in self.grid:
            print(row)
        # print(f"prev grid {self.grid}")

    def update_grid(self):
        """
        Update the grid by create a new one with the next value

        Return
        ------
        grid - list
        """
        next_grid = []
        for i, row in enumerate(self.grid):
            next_row = []
            for col in row:
                living_neighbours = self.get_living_neighbourhood(i, col)
                if self.grid[i][col] is 1 and living_neighbours is 2 or living_neighbours is 3:
                    self.grid[i][col] = 1
                elif self.grid[i][col] is 0 and living_neighbours == 3:
                    self.grid[i][col] = 1
                else:
                    self.grid[i][col] = 0
                next_row.append(self.grid[i][col])
            next_grid.append(next_row)
        self.grid = next_grid

    def get_living_neighbourhood(self, row, column):
        """
        Display neighbour living cells count of a specific cell

        Args
        ----
        row - int - row of a specific cell
        column - int - column of a specific cell

        Return
        ------
        neighbours - int
        """
        neighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Check all cells except current cell
                if i is not 0 and j is not 0:
                    neighbours += self.grid[(row + i) % self.rows][(column + j) % self.columns]
        # print(f" N = {neighbours}")
        return neighbours
