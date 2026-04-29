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