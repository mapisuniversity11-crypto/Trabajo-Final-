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


class cajero:
    def __init__(self, n1, n2, n5):
        self.n1 = n1
        self.n2 = n2
        self.n5 = n5
    def retiro(self, x):
        if x % 10000 != 0:
            return "La cantidad debe ser un multiplo de 10000"
        T_D =self.n1 * 10000 + self.n2 * 20000 + self.n5 * 50000 
        if x > T_D:
            return "Fondos insuficientes" 
        restante = x
        b5 = min(restante // 50000, self.n5)
        restante -= b5 * 50000
        b2 = min(restante // 20000, self.n2)
        restante -= b2 * 20000
        b1 = min(restante // 10000, self.n1)
        restante -= b1 * 10000
        if restante != 0:
            return "disculpe, no hay disponibilidad de billetes para esa cantidad de dinero"
        
        self.n5 -= b5
        self.n2 -= b2
        self.n1 -= b1
        return f"retiro exitoso: {b5} billetes de 50000, {b2}billetes de 20000, {b1} billetes de 10000"
    def consignacion(self, n1, n2, n5):
        self.n5 += n5
        self.n2 += n2
        self.n1 += n1
        return f"Consignación exitosa. {self.verificar_estado()}"
    def verificar_estado(self):
        return f"Billetes de 10000: {self.n1}, Billetes de 20000: {self.n2}, Billetes de 50000: {self.n5}" 

class polinomio:
    def __init__(self, l):
        self.l = L
    def __str__(self):
        terminos = []
        for i, a in enumerate(self.l ):
            if a == 0:
                continue
            if i == 0:
                terminos.append(str(a))
            elif i == 1:
                terminos.append(f"{a}x")
            else:
                terminos.append(f"{a}x^{i}")
        return "+".join(terminos) if terminos else "0"
    
    def __add__(self, other):
        n = max(len(self.l), len(other.l))
        L1 = self.l + [0] * (n- len(self.l))
        L2 = other.l + [0] * (n- len(other.l))
        return polinomio([L1[i] + L2[i] for i in range(n)])

    def __sub__(self, other):
        n = max(len(self.l), len(other.l))
        L1 = self.l + [0] * (n- len(self.l))
        L2 = other.l + [0] * (n- len(other.l))
        return polinomio([L1[i] - L2[i] for i in range(n)])

    def __rmul__(self, other):
        n = len(self.l) + len(other.l) - 1
        rta = [0] * n
        for i, a  in enumerate(self.l):
            for j ,b in enumerate(other.l):
                rta[i+j] += a*b
        return polinomio(rta)
    
    def evaluar(self, x):
        return sum(self.l[i] * (x ** i) for i in range(len(self.l)))

class pol_der(polinomio):
    def grado(self):
        l = self.l
        while len(l) > 1 and l[-1] == 0:
            l = l[::-1]
        return len(l) - 1
    def derivada(self):
        if len(self.l) == 1:
            return pol_der([0])
        nueva = [i * self.l[i] for i in range(1, len(self.l))]
        return pol_der[[b, m]]
        
