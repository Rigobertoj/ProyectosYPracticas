class Pelicula:
    #constructor de clase 
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("se a creado la pelicula {} ".format(self.titulo, ))
        
    #destructor de clase
    #def __del__ (self):
    #    print("se esta borrando la pelicula {}".format(self.titulo))
    
    #redefinimos el metodo str 
    def __str__(self):
        return "{} lanzada en {} con una duracion de {} minutos".format(self.titulo,self.lanzamiento,self.duracion) 
    
    
p = Pelicula("El padrino",175,1972)
print(str(p))