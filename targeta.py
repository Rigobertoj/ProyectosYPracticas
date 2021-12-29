class targeta():
    #atributos de la targeta
    valor = 0
    entidad_bancaria = "Banamex" 
    numero = None
    titular = None
    fecha = None
    estado = False
    
    # con esto podemos al ser un metodo constructivo ingresamos los datos del usuario
    def __init__(self, numero = None, titular = None):
        self.numero = numero
        self.titular = titular 
        if numero is not None and titular is not None:
            print("esta targeta a sido emitida por {}".format(self.entidad_bancaria))
            print("nombre del titular --> {}".format(self.titular))
            print("numero de serie --> {}".format(self.numero))
            print("_________________________________________________________________________")
        else:
            print("""ingrese los datos del ususario 
            ejemplo: taregta("numero de la taregta" ,nombre del titular)""")
            
    #ingresamos la fecha de emicion de la taregata
    def fecha(self, fecha = None):
        self.fecha = fecha
        if fecha is not None:
            print("fecha de emicion de la targeta {}".format(self.fecha))
        else:
            print("""ingresa la fecha de emicion de la targeta
            ejemplo: fecha("aa/MM/dddd")""")
            
            
    #activamos la targeta para su uso ya que al dar de alta una no quiere decir que ya este activada   
    def activacion(self, activado = True): #dando el valor verdaadero a un parametro 
        self.estado = activado #hacemos referencia a el atributo de estado y le damos el nuevo valor del parametro 
        print("targeta activada lista para su uso")
        
    #de esta manera lo que hacemos es con un parametro en la funcion que es la cantidad a depositar
    def deposito(self, monto): 
        print("monto depositado {}".format(monto))
        self.valor = self.valor + monto #hacemos referencia a el atributo de valor de la targeta y le damos el mismo valor mas la suma del monto 
        
    #le proporcionamos toda la informacion del usuario para que pueda ver todo respecto a su perfil 
    def info(self):
        # ingresamos un base de datos con toa la informacion del usuario
        datos = [{"titular":self.titular,"fecha de emicion":self.fecha,"estado de la taregata":self.estado,"saldo actual de la targeta":self.valor,"numero de targeta":self.numero}]
        #iteramos la lista para extraer el diccionario y asi manipular su informacion
        for dato in datos:
            #iteramos el diccionario para iterar todos los valores del mismo 
            for c,v in dato.items(): #gracias al metodo items() podemos iterar mas faccil un diccionario y su clave y valor 
                print(c,v) # c imprimimos clave v imprimimos valor
        
        
        
    def tranferir(self, monto):
        pass
    

targeta1 = targeta("1234 5678 9876 5432", "rigoberto Jaciel Martinez Madriz")
targeta1.fecha("12/24/2021")
targeta2 = targeta("2345 6789 1011 1213", "Brenda Yoseli Madriz Ojeda")
targeta2.fecha("26/24/2021")
targeta2.activacion()

class Banco():
    targetas = [{}] #agregamos una lista con un diccionario anidado para tener el nombre del titular y su numero 
    
    #metodo que funciona para ver los ususarios que allan en la base de datos
    def usuarios(self): 
        for usuarios in self.targetas: #se itera la lista para extraer el diccionario y asi manipular su informacion 
            for usuario,iD in usuarios.items():#gracias al metodo items() podemos iterar mas faccil un diccionario y su clave y valor 
                print(usuario,iD)#iteramos clave y valor 
    
    def agregar_usuario(self,U, x,targeta = [{}],): #agregamos una base de datos/lista con diccionario anidado interna como parametro, y las demas varibles/parametros
        for t in self.targetas: #iteramos la base de datos primaria de targetas 
            t[U] = x #agregamos clave(nombre del titular) y valor(numero de targeta) 
            print(t) #imprimimos la iteracion para confimar que todo estubo correcto 