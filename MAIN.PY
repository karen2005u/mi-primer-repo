def calculadora():
    print("--- Calculadora Básica ---")
    print("1. Sumar")
    print("2. Restar")
    opcion = input("Selecciona una opción (1/2): ")
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    if opcion == '1':
        print(f"Resultado: {num1 + num2}")
    elif opcion == '2':
        print(f"Resultado: {num1 - num2}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    calculadora()