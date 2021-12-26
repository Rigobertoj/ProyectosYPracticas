class Pelicula:
    #constructor de clase 
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("se a creado la pelicula {} ".format(self.titulo, ))
        
    #destructor de clase
    def __del__ (self):
        print("se esta borrando la pelicula {}".format(self.titulo))
    
    
    
p = Pelicula("El padrino",175,1972)
del(p)