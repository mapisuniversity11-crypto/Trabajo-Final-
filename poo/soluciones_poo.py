class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad < 0:
            return 'Cantidad no válida'
        self.saldo += cantidad
        #return self.consultar_saldo() # Esta linea retorna el saldo en cada deposito

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            return 'Retiro exitoso'
        
        return 'Fondos insuficientes'
    
    def consultar_saldo(self):
        return f'Su saldo es {self.saldo}'

class VectoresR3:
    def __init__(self, L):
        # Desempaquetado: Si L no tiene 3 elementos, falla solo.
        self.x, self.y, self.z = L 
        self.comp = L

    def __add__(self, v1):
        # Suma componente a componente
        suma = [self.comp[i] + v1.comp[i] for i in range(3)]
        return VectoresR3(suma)

    def __sub__(self, v1):
        # Resta componente a componente
        resta = [self.comp[i] - v1.comp[i] for i in range(3)]
        return VectoresR3(resta)

    def __rmul__(self, escalar):
        # Multiplicación por escalar (ej: 3 * vector)
        producto = [escalar * c for c in self.comp]
        return VectoresR3(producto)

    def producto_punto(self, v1):
        return sum(self.comp[i] * v1.comp[i] for i in range(3))

    def producto_cruz(self, v1):
        # Retorna un nuevo objeto VectoresR3
        cx = self.y * v1.z - self.z * v1.y
        cy = self.z * v1.x - self.x * v1.z
        cz = self.x * v1.y - self.y * v1.x
        return VectoresR3([cx, cy, cz])

    def __repr__(self):
        return f"VectoresR3({self.comp})"
    
import random
import string 
class Vehiculo:
    # Todos los parametros que se encuentran en el __init__ el usuario los puede cambiar
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        #EL usuario no lo modifica, este siempre inicia en cero 
        self.velocidad = 0 

    def acelerar(self, incremento):
        self.velocidad += incremento
        if self.velocidad > 200:
            self.velocidad = 200


    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"


class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
        letras = ''.join(random.choices(string.ascii_uppercase, k=3))
        digitos = ''.join(random.choices(string.digits, k=3))
        self.placa = letras + digitos

    def __str__(self):
        return f"{self.marca} {self.modelo} - Placa: {self.placa} - Puertas: {self.numero_puertas}"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo

    def hacer_caballito(self):
        if self.velocidad > 30:
            return '¡Caballito!'
        return 'Necesitas más velocidad'

    def __str__(self):
        return f"{self.marca} {self.modelo} - Tipo: {self.tipo}"
    
import math

class Figura:
    def __init__(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError('Implementar en subclase')

    def perimetro(self):
        raise NotImplementedError('Implementar en subclase')

    def __str__(self):
        return f"Figura de color {self.color}"

    def descripcion(self):
        tipo = type(self).__name__
        return (f"Soy una {tipo} de color {self.color} "
                f"con área {self.area():.2f} y perímetro {self.perimetro():.2f}")


class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Círculo de radio {self.radio} y color {self.color}"


class Triangulo(Figura):
    def __init__(self, color, base, altura, lado1, lado2, lado3):
        super().__init__(color)
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def __str__(self):
        return f"Triángulo de base {self.base} y color {self.color}"