frutas = []

def mostrar_menu():
    mostrar_separador()
    menu = """Bienvenido
1. Para agregar fruta
2. Para ver frutas
3. Para salir"""
    print(menu)
    mostrar_separador()
    

def mostrar_separador():
    print("*"*15)

def agregar_fruta():
    mostrar_separador()
    fruta = input("Ingrese el nombre de la fruta: ")
    frutas.append(fruta)

def ver_frutas():
    mostrar_separador()
    for i in range(len(frutas)):
        print(i+1, "-", frutas[i])

def pedir_opcion():
    opcion = int(input("Ingrese la opcion deseada: "))
    return opcion

while True:
    mostrar_menu()
    try:
        opc = pedir_opcion()
    except Exception:
        print("Hubo un error con su opción ingresada")
        opc = 3
    if opc == 1:
        agregar_fruta()
    elif opc == 2:
        ver_frutas()
    elif opc == 3:
        print("Bye bye :)")
        break
    else:
        print("Opción no válida!")