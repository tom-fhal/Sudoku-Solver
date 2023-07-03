# Importation des classes Backtracking et BruteForce
from Backtracking import Backtracking
from BruteForce import BruteForce
# Importation de la fonction colored du module termcolor
from termcolor import colored

class Main:

    def __init__(self):
        # Initialisation du solver 
        #self.brute_force_solver = BruteForce()
        #self.backtracking_solver = Backtracking()
        pass

    def read_sudoku(self, filename):
        # Lecture d'un fichier contenant une grille de Sudoku
        with open(filename, 'r') as file:
            lines = file.readlines()
            grid = []
            for line in lines:
                row = []
                for char in line.strip():
                    if char == '_':
                        row.append(0)
                    else:
                        row.append(int(char))
                grid.append(row)
        return grid

    def solve(self, grid, method='backtracking'):
        # Résolution de la grille de Sudoku en utilisant la méthode choisie (backtracking ou brute force)
        if method == 'backtracking':
            solver = Backtracking(grid)
            return solver.solve()
        else:
            solver = BruteForce(grid)
            return solver.solve()


    
    def display(self, grid, method):
        # Affichage de la grille de Sudoku à résoudre
        print("Sudoku à résoudre :")
        self.display_grid(grid)
        # Affichage de la méthode de résolution choisie et de la grille résolue
        if method == 'backtracking':
            print("Résolution par backtracking :")
            self.display_grid(self.solve(grid, 'backtracking'))
        else:
            print("Résolution par force brute :")
            self.display_grid(self.solve(grid, 'brute_force'))

def display_grid(self, grid):
    # Affichage d'une grille de Sudoku
    for i, row in enumerate(grid):
        if i % 3 == 0:
            print('-' * 21)
        row_str = '| '
        for j, cell in enumerate(row):
            if cell == 0:
                row_str += '  '
            else:
                row_str += colored(str(cell), 'blue') + ' '
            if (j + 1) % 3 == 0:
                row_str += '| '
        print(row_str)
    print('-' * 21)
