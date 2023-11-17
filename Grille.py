#Création de la grille
grille = [[0 for _ in range(10)] for _ in range(10)]

# Créer des étiquettes pour les colonnes et les lignes
colonnes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
lignes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Afficher les étiquettes des colonnes
print(' ', end='')
for c in colonnes:
   print(' ' + str(c), end='')
print()

# Afficher la grille avec les étiquettes des lignes
for i in range(len(grille)):
   print(str(lignes[i]), end='')
   for elt in grille[i]:
       print(' ' + str(elt), end='')
   print()