class CalculadoraMCD:
    def calcular_mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

# Crear una instancia de la clase CalculadoraMCD
calculadora = CalculadoraMCD()

# Solicitar al usuario que ingrese los dos números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Calcular el MCD utilizando el método de la instancia
mcd = calculadora.calcular_mcd(num1, num2)

# Mostrar el resultado utilizando f-string
print(f"El máximo común divisor de {num1} y {num2} es: {mcd}")
