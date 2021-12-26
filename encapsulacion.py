class ejemplo:
    __atributo_privado = "soy un atributo inmodificable desde fuera"
    
    def __metodo_privado(self):
        print("soy un metodo inmodificable desde fuera")
        
    def metodo_publico(self):
        return self.__metodo_privado()
    
    def metodo_publico2(self):
        return self.__atributo_privado

e = ejemplo()
print(e.metodo_publico())
print(e.metodo_publico2())