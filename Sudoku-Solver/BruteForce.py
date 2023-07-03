class BruteForce:
    def __init__(self, grid):
        # Initialisation de l'attribut grid à None
        self.grid = grid

    def solve(self):
        # Appel de la méthode bruteforce
        result = self.bruteforce()
        # Renvoi de la grille résolue
        return result

    def bruteforce(self):
        # Recherche d'une cellule vide
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    # Essai de toutes les valeurs possibles
                    for k in range(1, 10):
                        if self.is_valid(i, j, k):
                            self.grid[i][j] = k
                            if self.solve():
                                return self.grid
                            else:
                                self.grid[i][j] = 0
                    return False
        return self.grid

    def is_valid(self, i, j, k):
        # Vérification de la validité de la valeur k dans la cellule (i,j)
        # Vérification de la ligne
        for col in range(9):
            if self.grid[i][col] == k:
                return False
        # Vérification de la colonne
        for row in range(9):
            if self.grid[row][j] == k:
                return False
        # Vérification de la région
        row_region = (i//3)*3
        col_region = (j//3)*3
        for row in range(row_region,row_region+3):
            for col in range(col_region,col_region+3):
                if self.grid[row][col] == k:
                    return False
        # Si aucune valeur n'a été trouvée, renvoi de True
        return True