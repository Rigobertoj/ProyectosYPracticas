import math
class Punto():
    x = 0 
    y = 0 
    x2 = 0
    y2 = 0
    def __init__(self, x = None, y = None ):
        self.x = x
        self.y = y
        
    def __str__(self):
        print("({},{})".format(self.x, self.y))
        
    def cuadrante(self):
        if self.x > 0  and self.y > 0:
            print("cuadrante 1")
            
        elif self.x < 0 and self.y > 0:
            print("cuadrante 2")
            
        elif self.x < 0 and self.y < 0:
            print("cuadrante 3")
            
        elif self.x > 0 and self.y < 0:
            print("cuadrante 4")
            
        else:
            print("tu punto esta en el origen (0,0)")
            
    def vector(self, x2 = None, y2 = None):
        if x2 is not None and y2 is not None:
            self.x2 = x2
            self.y2 = y2
            v = (self.x2 - self.x, self.y2 - self.y)
            print(v)
        else:
            print("introduce los valores del punto 2")
            print("ejemplo: e.vector(4,5)")
            
    def distancia(self, x2 = None, y2 = None):
        if x2 is not None and y2 is not None:
            self.x2
            self.y2
            d = math.sqrt((self.x2-self.x)**2 + (self.y2-self.y)**2)
            print("la distancia entre los puntos que introduciste {}".format(d))
            
class Rectangulo():
    x = 0 
    y = 0 
    x2 = 0 
    y2 = 0
    x3 = 0
    y3 = 0
    x4 = 0
    y4 = 0
    def __init__(self, x = 0, y = 0, x2 = 0, y2 = 0 ):
        if x >= 0  and y >= 0 and x2 >= 0  and y2 >= 0:
            self.x = x
            self.y = y
            self.x2 = x2
            self.y2 = y2
            self.x3 = self.x2
            self.y3 = self.y
            self.x4 = self.x
            self.y4 = self.y2
            base = print("""puntos del rectangulo p1){},{} p2){},{} p3){},{} p4){},{} """.format(self.x,self.y,self.x2,self.x2,self.x3,self.y3,self.x4,self.y4))
    def base(self):
        b = self.x3 - self.x
        print("la base del rectangulo es {}".format(b))
        
    def altura(self):
        h = self.y4 - self.x
        print("la altura del rectangulo es {}".format(h))
    def area(self):
        b = self.x3 - self.x
        h = self.y4 - self.y
        a = b * h
        print("el area del rectangulo es {}".format(a))