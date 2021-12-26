class Targeta():
    valor = 0
    entidad_bancaria = "Banamex" 
    
    def __init__(self, numero = None, titular = None):
        self.numero = numero
        self.titular = titular 
        if numero is not None and titular is not None:
            print("esta targeta a sido emitida por {}".format(self.entidad_bancaria))
            print("nombre del titular --> {}".format(self.titular))
            print("numero de serie --> {}".format(self.numero))
    
    def __init__(self, fecha = None):
        self.fecha = fecha
        if fecha is not None:
            print("fecha de emicion de la targeta {}".format(self.fecha))
        
    def activacion(self):
        print("targeta activada lista para su uso")
        
    def deposito(self, cantidad):
        print("cual es el monto a ingresar")
        self.cantidad = cantidad
        
    def tranferir(self, monto):
        pass

targeta = Targeta()
