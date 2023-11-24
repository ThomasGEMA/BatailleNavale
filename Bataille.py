from Bateau import Bateau


class Bataille:
    def __init__(self):
        self.grille1 = [[0 for _ in range(10)] for _ in range(10)]
        self.grille2 = [[0 for _ in range(10)] for _ in range(10)]
        self.bateaux1 = [
            Bateau(taille=2),
            Bateau(taille=3),
            Bateau(taille=4),
            Bateau(taille=5),
        ]
        self.bateaux2 = [
            Bateau(taille=2),
            Bateau(taille=3),
            Bateau(taille=4),
            Bateau(taille=5),
        ]

    def afficher_grille1(self):
   # Créer des étiquettes pour les colonnes et les lignes
       colonnes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
       lignes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

   # Afficher les étiquettes des colonnes
       print(' ', end='')
       for c in colonnes:
           print(' ' + str(c), end='')
       print()

   # Afficher la grille1 avec les étiquettes des lignes
       for i,e in enumerate(self.grille1) : # toutes les lignes
           print(lignes[i], end='')
           for elt in e: # toutes les cases de la ligne courante
               if elt == 1:
                   print(' ' + 'X', end='')
               else:
                   print(' ' + str(elt), end='')
           print()

    def afficher_grille2(self):
   # Créer des étiquettes pour les colonnes et les lignes
       colonnes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
       lignes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

   # Afficher les étiquettes des colonnes
       print(' ', end='')
       for c in colonnes:
           print(' ' + str(c), end='')
       print()

   # Afficher la grille2 avec les étiquettes des lignes
       for i,e in enumerate(self.grille2) : # toutes les lignes
           print(lignes[i], end='')
           for elt in e: # toutes les cases de la ligne courante
               if elt == 1:
                   print(' ' + 'X', end='')
               else:
                   print(' ' + str(elt), end='')
           print()


    def placer_bateaux(self):
        for bateau in self.bateaux1:
            while True:
                try:
                    x = int(input(f"Entrez la coordonnée X du {bateau.get_taille()}-bateau : "))
                    y = int(input(f"Entrez la coordonnée Y du {bateau.get_taille()}-bateau : "))
                    horizontal = input("Le bateau est-il horizontal ? (o/n) ").lower() == 'o'

                    bateau.avancee(x - bateau.get_x(), y - bateau.get_y())
                    bateau.horizontal = horizontal

                    if self.peut_placer_bateau(bateau):
                        self.placer_bateau_sur_grille(bateau)
                        break
                    else:
                        print("Impossible de placer le bateau à cet endroit. Réessayez.")
                except ValueError:
                    print("Veuillez entrer un nombre valide pour la coordonnée X et Y.")

    def peut_placer_bateau(self, bateau):
        if bateau.horizontal:
            return (
                bateau.get_x() + bateau.get_taille() <= 10
                and all(
                    self.grille1[bateau.get_y() - 1][x - 1] == 0
                    for x in range(bateau.get_x(), bateau.get_x() + bateau.get_taille())
                )
            )
        else:
            return (
                bateau.get_y() + bateau.get_taille() <= 10
                and all(
                    self.grille[y - 1][bateau.get_x() - 1] == 0
                    for y in range(bateau.get_y(), bateau.get_y() + bateau.get_taille())
                )
            )

    def placer_bateau_sur_grille(self, bateau):
        if bateau.horizontal:
            for x in range(bateau.get_x(), bateau.get_x() + bateau.get_taille()):
                self.grille1[bateau.get_y() - 1][x - 1] = 1
        else:
            for y in range(bateau.get_y(), bateau.get_y() + bateau.get_taille()):
                self.grille1[y - 1][bateau.get_x() - 1] = 1

    def placer_bateaux_pour_joueur2(self):
       for bateau in self.bateaux2:
           while True:
               try:
                   x = int(input(f"Entrez la coordonnée X du {bateau.get_taille()}-bateau : "))
                   y = int(input(f"Entrez la coordonnée Y du {bateau.get_taille()}-bateau : "))
                   horizontal = input("Le bateau est-il horizontal ? (o/n) ").lower() == 'o'

                   bateau.avancee(x - bateau.get_x(), y - bateau.get_y())
                   bateau.horizontal = horizontal

                   if self.peut_placer_bateau_pour_joueur2(bateau):
                      self.placer_bateau_sur_grille_pour_joueur2(bateau)
                      break
                   else:
                      print("Impossible de placer le bateau à cet endroit. Réessayez.")
               except ValueError:
                   print("Veuillez entrer un nombre valide pour la coordonnée X et Y.")

    def peut_placer_bateau_pour_joueur2(self, bateau):
       if bateau.horizontal:
           return (
               bateau.get_x() + bateau.get_taille() <= 10
               and all(
                   self.grille2[bateau.get_y() - 1][x - 1] == 0
                   for x in range(bateau.get_x(), bateau.get_x() + bateau.get_taille())
               )
           )
       else:
           return (
               bateau.get_y() + bateau.get_taille() <= 10
               and all(
                   self.grille2[y - 1][bateau.get_x() - 1] == 0
                   for y in range(bateau.get_y(), bateau.get_y() + bateau.get_taille())
               )
           )

    def placer_bateau_sur_grille_pour_joueur2(self, bateau):
       if bateau.horizontal:
           for x in range(bateau.get_x(), bateau.get_x() + bateau.get_taille()):
               self.grille2[bateau.get_y() - 1][x - 1] = 1
       else:
           for y in range(bateau.get_y(), bateau.get_y() + bateau.get_taille()):
               self.grille2[y - 1][bateau.get_x() - 1] = 1

if __name__ == '__main__':
 cl = Bataille()
 cl.__init__()
 cl.afficher_grille1()
 cl.placer_bateaux()
 cl.afficher_grille1()
 cl.placer_bateaux_pour_joueur2()
 cl.afficher_grille2()