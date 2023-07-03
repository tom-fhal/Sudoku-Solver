class Backtracking:
    def __init__(self,grid):
        # Initialisation de l'attribut grid à None
        self.grid = grid

    def solve(self):
        # Appel de la méthode backtrack
        self.backtrack()
        # Renvoi de la grille résolue
        return self.grid

    
    def backtrack(self):
        # Parcours des lignes et des colonnes de la grille
        for i in range(9):
            for j in range(9):
                # Si la cellule est vide (représentée par 0)
                if self.grid[i][j] == 0:
                    # Essai de toutes les valeurs possibles de 1 à 9
                    for k in range(1,10):
                        # Si la valeur est valide (vérifiée par la méthode is_valid, non montrée dans ce code)
                        if self.is_valid(i,j,k):
                            # Assignation de la valeur à la cellule
                            self.grid[i][j] = k
                            # Appel récursif de la méthode backtrack pour continuer à résoudre le problème
                            if self.backtrack():
                                # Si l'appel récursif renvoie True, c'est-à-dire qu'une solution a été trouvée, renvoi de True
                                return True
                            # Sinon, retour en arrière en réinitialisant la cellule à 0 et essai d'autres valeurs
                            self.grid[i][j] = 0
                    # Si aucune valeur valide n'a été trouvée pour une cellule vide, renvoi de False pour indiquer qu'aucune solution n'est possible
                    return False
        # Si toutes les cellules ont été remplies, renvoi de True pour indiquer qu'une solution a été trouvée
        return True

    def is_valid(self,i,j,k):
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
    

    

    