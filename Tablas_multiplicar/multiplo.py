VERDE = "\033[32m"
BLUE = "\033[94m"
BLANCO = "\033[37m"
AMARILLO = "\033[33m"
Magenta = "\033[35m"
RED = "\033[31m"



class multiplicación:
    def __init__(self):
        print("Tabla de multiplicar")

    def tablas(self):
        print("opcion 1. tabla del 1: Opción 2 tabla del 2 : Opción 3 tabla del 3...: Opción 10 tabla del 10")
        numero = int(input("Ingresa la tabla de multiplicar que desea observar en pantalla: "))
        print(f"{VERDE}TABLA DEL {numero}")
        if numero == 1:
            for i in range(0,21):
                for j in range(1,11):
                  multiplo = i*(j-9)
                print(f"{AMARILLO}{j-9} {BLANCO}x {BLUE}{i} {BLANCO}= {RED}{multiplo}")
        elif numero == 2:
            for i in range(0,21):
                for j in range(1,11):
                    multiplo = i*(j-8)
                print(f"{AMARILLO}{j-8} {BLANCO}x {BLUE}{i} {BLANCO}= {RED}{multiplo}")
        elif numero == 3:
            for i in range(0,21):
                for j in range(1,11):
                    multiplo = i*(j-7)
                print(f"{AMARILLO}{j-7} {BLANCO}x {BLUE}{i} {BLANCO}= {RED}{multiplo}")
        elif numero == 4:
            for i in range(0,21):
                for j in range(1,11):
                    multiplo = i*(j-6)
                print(f"{AMARILLO}{j-6} {BLANCO}x {BLUE}{i} {BLANCO}= {RED}{multiplo}")
        elif numero == 5:
            for i in range(0,21):
                for j in range(1,11):
                    multiplo = i*(j-5)
                print(f"{AMARILLO}{j-5} {BLANCO}x {BLUE}{i} {BLANCO}= {RED}{multiplo}")
        elif numero == 6:
            for i in range(0,21):
                for j in range(1,11):
                    multiplo = i*(j-4)
                print(f"{AMARILLO}{j-4} {BLANCO}x {BLUE}{i} {BLANCO}= {RED}{multiplo}")
        elif numero == 7:
            for i in range(0,21):
                for j in range(1,11):
                    multiplo = i*(j-3)
                print(f"{AMARILLO}{j-3} {BLANCO}x {BLUE}{i} {BLANCO}= {RED}{multiplo}")
        elif numero == 8:
            for i in range(0,21):
                for j in range(1,11):
                    multiplo = i*(j-2)
                print(f"{AMARILLO}{j-2} {BLANCO}x {BLUE}{i} {BLANCO}= {RED}{multiplo}")
        elif numero == 9:
            for i in range(0,21):
                for j in range(1,11):
                    multiplo = i*(j-1)
                print(f"{AMARILLO}{j-1} {BLANCO}x {BLUE}{i} {BLANCO}= {RED}{multiplo}")
        elif numero == 10:
            for i in range(0,21):
                for j in range(1,11):
                    multiplo = i*(j)
                print(f"{AMARILLO}{j} {BLANCO}x {BLUE}{i} {BLANCO}= {RED}{multiplo}")
        else:
            print("Ingresa un valor válido, tal como se le solicita.")


mensaje = multiplicación()
mensaje.tablas()