import random

class Motor:
    def __init__ (self, Cilindraje, Potencia):
        self.cilindraje = Cilindraje
        self.caballos = Potencia

class SistemasdelCarro:
    def __init__(self, hidraulico, electrico, itsok):
        self.sish = hidraulico
        self.sise = electrico
        self.ok = itsok

def arranque(motor):
    if motor.cilindraje > 5:
        return "listo para usar"
    else:
        return "no estoy listo"

class Chasis:
    def __init__ (self, color, modelo, forma):
        self.c = color
        self.m = modelo
        self.f = forma

class Carro:
    def __init__ (self, Motor, SistemadelCarro, Chasis):
        self.motor = Motor
        self.sistemas = SistemadelCarro
        self.chasis = Chasis

def verificarsistemas(motor, sistema):
    if sistema.ok == True:
        return arranque(motor)
    else:
        return "no esta listo revise los sistemas del carro"

    
        
    



mot=Motor(10,87)
sis=SistemasdelCarro("hidra", "general", True)
cha=Chasis("blanco", "nissan", "estandar")  


car = Carro(mot, sis, cha)

print verificarsistemas(car.motor, car.sistemas)


