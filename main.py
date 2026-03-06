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
    pass

def ver_frutas():
    pass

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
        print("opcion 1")
    elif opc == 2:
        print("opcion 2")
    elif opc == 3:
        print("Bye bye :)")
        break
    else:
        print("Opción no válida!")