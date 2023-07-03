# Importation des classes Main, Backtracking et BruteForce
from main import Main
from Backtracking import Backtracking
from BruteForce import BruteForce

# Création d'une instance de la classe Main
main = Main()

# Initialisation de la variable continuer à 'o' pour entrer dans la boucle while
continuer = 'o'

# Boucle while pour permettre à l'utilisateur de résoudre plusieurs grilles de Sudoku
while continuer == 'o':
    # Demande à l'utilisateur de choisir un niveau de difficulté
    level = input("Choisissez un niveau (1 à 5) : ")
    # Construction du nom du fichier contenant la grille de Sudoku en fonction du niveau choisi
    filename = f'level/level{level}.txt'
    # Lecture de la grille de Sudoku à partir du fichier
    grid = main.read_sudoku(filename)
    # Affichage du niveau choisi et de la grille de Sudoku
    print(f'Résolution du niveau {level}:')
    main.display_grid(grid)
    # Demande à l'utilisateur de choisir une méthode de résolution (backtracking ou brute force)
    method = input("Choisissez une méthode de résolution (backtracking ou brute_force) : ")
    # Résolution de la grille de Sudoku en utilisant la méthode choisie
    solution = main.solve(grid, method)
    # Affichage de la solution et de la méthode utilisée
    main.display(solution, method)
    # Demande à l'utilisateur s'il souhaite continuer à résoudre des grilles de Sudoku
    continuer = input("Voulez-vous continuer (o/n) ? ")
