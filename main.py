class CalculadoraMCD:
    def calcular_mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def calcular_mcm(self, a, b):
        mcd = self.calcular_mcd(a, b)
        return (a * b) // mcd

# Crear una instancia de la clase CalculadoraMCD
calculadora = CalculadoraMCD()

# Solicitar al usuario que ingrese los dos números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Calcular el MCD utilizando el método de la instancia
mcd = calculadora.calcular_mcd(num1, num2)

# Calcular el MCM utilizando el método de la instancia
mcm = calculadora.calcular_mcm(num1, num2)

# Mostrar el resultado
print(f"El máximo común divisor de {num1} y {num2} es: {mcd}")
print(f"El mínimo común múltiplo de {num1} y {num2} es: {mcm}")
