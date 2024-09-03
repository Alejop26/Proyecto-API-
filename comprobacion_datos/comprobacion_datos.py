lista_departamentos = ["AMAZONAS", "ANTIOQUIA", "ARAUCA", "ATLANTICO", "BOLIVAR", "BOYACA", "CALDAS", "CAQUETA", "CASANARE", "CAUCA", "CESAR", "CHOCO", "CORDOBA", "CUNDINAMARCA", "GUAINIA", "GUAVIARE", "HUILA", "GUAJIRA", "MAGDALENA", "META", "NARIÑO", "NORTE SANTANDER", "PUTUMAYO", "QUINDIO", "RISARALDA", "SAN ANDRES", "SANTANDER", "SUCRE", "TOLIMA", "VALLE", "VAUPES", "VICHADA"]

def comprobar_input_departamentos ():

    print("Por favor, ingrese el nombre del departamento a filtrar: ")
    nombre_departamento = input().upper()


    while (nombre_departamento not in lista_departamentos):

        print("\nIngresó un departamento no válido o no existente, intentelo de nuevo:")
        nombre_departamento = input().upper()

    return nombre_departamento

def comprobar_input_limite_datos ():

    print("\nPor favor, ingrese la cantidad de datos a consultar: ")
    cantidad_datos = input()

    while (cantidad_datos.isalpha()):
        print("\nIngresó un valor no válido, intentelo de nuevo:")
        cantidad_datos = input()

    return cantidad_datos