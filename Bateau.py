class Bateau:
    def __init__(self, x=1, y=1, horizontal=True, taille=1):
        self.x = x
        self.y = y
        self.horizontal = horizontal
        self.taille = taille
        self.touche = False
        self.elements = [False] * taille



    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_taille(self):
        return self.taille

    def get_touche(self):
        return self.touche

    def get_horizontal(self):
        return self.horizontal

    def est_coule(self):
        return all(self.elements)
