import math

# Lista para guardar el historial
historial = []

def obtener_numeros(cantidad=None):
    while True:
        try:
            entrada = input("Ingresa los números separados por coma: ")
            numeros = [float(num.strip()) for num in entrada.split(",")]
            
            if cantidad and len(numeros) != cantidad:
                print(f"Error: Debes ingresar exactamente {cantidad} números.")
                continue
                
            return numeros
        except ValueError:
            print("Error: Ingresa números válidos separados por comas.")

def guardar_historial(operacion, resultado):
    historial.append({"operacion": operacion, "resultado": resultado})

def mostrar_historial():
    print("\n--- Historial ---")
    for idx, registro in enumerate(historial, 1):
        print(f"{idx}. {registro['operacion']} = {registro['resultado']}")
    print("-----------------")

while True:
    print("\n" + "=" * 30)
    print("Calculadora Nivel Intermedio")
    print("=" * 30)
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Módulo")
    print("7. Raíz cuadrada")
    print("8. Ver historial")
    print("9. Salir")
    
    opcion = input("\nElige una opción (1-9): ")
    
    if opcion == "9":
        # Guardar historial en un archivo antes de salir
        with open("historial_calculadora.txt", "w") as f:
            for registro in historial:
                f.write(f"{registro['operacion']} = {registro['resultado']}\n")
        print("\n¡Hasta luego! Historial guardado en 'historial_calculadora.txt'")
        break
    
    if opcion not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("\033[91mError: Opción inválida.\033[0m")
        continue
    
    # Opción especial: Historial
    if opcion == "8":
        mostrar_historial()
        continue
    
    try:
        if opcion == "7":  # Raíz cuadrada
            num = float(input("Ingresa un número: "))
            if num < 0:
                print("\033[91mError: No existe raíz cuadrada real de números negativos.\033[0m")
                continue
            resultado = math.sqrt(num)
            operacion = f"√{num}"
        elif opcion in ["5", "6"]:  # Potencia o módulo (necesitan 2 números)
            numeros = obtener_numeros(2)
            a, b = numeros
            if opcion == "5":
                resultado = a ** b
                operacion = f"{a} ^ {b}"
                if b < 0 and a <= 0:
                    print("\033[91mError: Base negativa con exponente negativo no permitida.\033[0m")
                    continue
            elif opcion == "6":
                if b == 0:
                    print("\033[91mError: Módulo por cero no permitido.\033[0m")
                    continue
                resultado = a % b
                operacion = f"{a} % {b}"
        else:  # Otras operaciones básicas
            if opcion in ["1", "3"]:  # Suma o multiplicación (múltiples números)
                numeros = obtener_numeros()
                if opcion == "1":
                    resultado = sum(numeros)
                    operacion = " + ".join(map(str, numeros))
                else:
                    resultado = math.prod(numeros)
                    operacion = " * ".join(map(str, numeros))
            else:  # Resta o división (2 números)
                numeros = obtener_numeros(2)
                a, b = numeros
                if opcion == "2":
                    resultado = a - b
                    operacion = f"{a} - {b}"
                elif opcion == "4":
                    if b == 0:
                        print("\033[91mError: No se puede dividir entre cero.\033[0m")
                        continue
                    resultado = a / b
                    operacion = f"{a} / {b}"
        
        # Mostrar y guardar resultado
        print(f"\n\033[92mResultado: {operacion} = {resultado}\033[0m")
        guardar_historial(operacion, resultado)
        
    except Exception as e:
        print(f"\033[91mError inesperado: {str(e)}\033[0m")