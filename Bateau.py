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

    def est_touche(self, x, y):
       if self.horizontal:
           return self.x <= x < self.x + self.taille and self.y == y
       else:
           return self.x == x and self.y <= y < self.y + self.taille

    def get_horizontal(self):
        return self.horizontal

    def est_coule(self):
        return all(self.elements)


    def avancee(self, a, b):
        self.x +=a
        self.y +=b