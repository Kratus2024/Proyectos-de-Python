# Haremos que el usuario ingrese la medida que desea calcular.
print("Convertidor de unidades: Longitud, masa, temperatura.")

def conversor():
    try:
        medida = input("Ingresa la unidad de medida que desea convertir (En minuscula): ").lower()
        n = int(input("Ingrese el número de medidas que va a calcular: "))
        # Medidas de longitud
        if medida == "longitud":
            print("Opcion 1: kilometros-metros ; Opción 2: metros-kilometros ; Opción 3: millas-kilometros.")
            print("Opción 4: millas-metros ; Opción 5: kilometros-millas ; Opción 6: metros-millas.")
            opcion = int(input("Ingrese alguna de las opciones mencionadas anteriormente: "))
            for i in range(n):
                valor = int(input("Valor de la medida: "))
                if opcion == 1: # Kilometros-Metros
                   print(f"El valor es {valor} km en metros equivale a: {valor*1000:.2f}m")
                elif opcion == 2: # Metros-Kilometros
                   print(f"El valor es {valor}m en kilometros equivale a: {valor/1000:.2f}km")
                elif opcion == 3: # Millas-Kilometros
                   print(f"El valor es {valor}mi en kilometros equivale a: {valor*1.60934:.2f}km")
                elif opcion == 4: # Millas-Metros
                   print(f"El valor es {valor}mi en mmetros equivale a: {valor*1609.34:.2f}m")
                elif opcion == 5: # Kilometros-Millas
                   print(f"El valor es {valor}km en millas equivale a: {valor/1.60934:.2f}mi")
                elif opcion == 6: # Metros-Millas
                   print(f"El valor es {valor}m en millas equivale a: {valor/1609.34:.2f}mi")

        # Medidas de Masa
        if medida == "masa":
            print("Opcion 1: kilogramos-Gramos ; Opción 2: Gramos-Kilogramos ; Opción 3: Libras-Kilogramos.")
            print("Opción 4: Libras-Gramos ; Opción 5: Kilogramos-Libras ; Opción 6: Gramos-Libras.")
            opcion = int(input("Ingrese alguna de las opciones mencionadas anteriormente: "))
            for i in range(n):
               valor = int(input("Valor de la medida: "))
               if opcion == 1: # Kilogramos-Gramos
                  print(f"El valor es {valor}kg en gramos equivale a: {valor*1000:.2f}g")
               elif opcion == 2: # Gramos-Kilogramos
                  print(f"El valor es {valor}g en kilogramos equivale a: {valor/1000:.2f}kg")
               elif opcion == 3: # Libras-Kilogramos
                  print(f"El valor es {valor}lb en kilogramos equivale a: {valor*0.453592:.2f}kg")
               elif opcion == 4: # Libras-Gramos
                  print(f"El valor es {valor}lb en gramos equivale a: {valor*453.592:.2f}g")
               elif opcion == 5: # Kilogramos-Libras
                   print(f"El valor es {valor}kg en libras equivale a: {valor/0.453592:.2f}lb")
               elif opcion == 6: # Gramos-Libras
                   print(f"El valor es {valor}g en libras equivale a: {valor/453.592:.2f}lb")

        # Medidas de Temperatura
        if medida == "temperatura":
            print("Opcion 1: Kelvin-Celsius ; Opción 2: Celsius-Kelvin ; Opción 3: Farenheit-Kelvin.")
            print("Opción 4: Farenheit-Celsius ; Opción 5: Kelvin-Farenheit ; Opción 6: Celsius-Farenheit.")
            opcion = int(input("Ingrese alguna de las opciones mencionadas anteriormente: "))
            for i in range(n):
               valor = int(input("Valor de la medida: "))
               if opcion == 1: # Kelvin-Celsius
                  print(f"El valor es {valor}K en grados Celsius equivale a: {valor-273.15:.2f}°C")
               elif opcion == 2: # Celsius-Kelvin
                  print(f"El valor es {valor}°C en Kelvin equivale a: {valor+273.15:2f}K")
               elif opcion == 3: # Farenheit-Kelvin
                  print(f"El valor es {valor}°F en Kelvin equivale a: {0.555*(valor-32)+ 273.15:.2f}K")
               elif opcion == 4: # Farenheit-Celsius
                  print(f"El valor es {valor}°F en grados Celsius equivale a: {0.555*(valor-32):.2f}°C")
               elif opcion == 5: # Kelvin-Farenheit
                   print(f"El valor es {valor}K en grados Farenheit equivale a: {(valor-273.15)*1.8 +32:.2f}°F")
               elif opcion == 6: # Celsius-Farenheit
                   print(f"El valor es {valor}°C en grados Farenheit equivale a: {(valor*1.8) +32:.2f}°F")

    except ValueError:
       print("Ingrese Valores Válidos")

conversor()