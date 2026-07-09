#DATOS INICIALES 
libros = {
    #codigo -       nomnbre      - autor -    tipo -   año - editorial   - es novedad
    'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
    'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
    'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
    'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
    'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True],
    'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False],
}


prestamos = {
#codigo - multa - copias 
'L001':[500, 4],
'L002':[700, 0],
'L003':[300, 10],
'L004':[400, 2],
'L005':[600, 1],
'L006':[350, 6],
    
}

#FUNCIONES DEL SISTEMA 
def mostrar_menu():
    print("\n ==== MENU PRINCIPAL ====")
    print("1. Copias por genero \n2. Busqueda de libros por rango de multa \n3. Actualizar Multa de libro \n4. Agregar libro \n5. Eliminar Libro \n6. Salir")

def ingresar_validar_opcion():
    while True:
        try:
            ingreso_op = int(input(">> Ingrese una opcion (1-6): "))
            if ingreso_op not in [1,2,3,4,5,6]:
                print(f"[Error: '{ingreso_op}' no es válido.]")
                continue
            else:
                return ingreso_op
        except ValueError:
            print("[Error: Solo se permiten números. Letras y simbolos no son validos. Debe ingresar una opcion válida] \n")
            continue

# FUNCIONES -- OPCION 1 (COPIAS POR GENERO) X 
def copias_genero(genero):
    contador_libros_segunTipo = 0
    for libro in libros.items():
        if libro == genero:
            contador_libros_segunTipo += 1
    print(f"El total de copias disponibles es: {contador_libros_segunTipo}")

# FUNCIONES -- OPCION 2 (BUSQUEDA DE LIBRO POR RANGO DE MULTA)
def busqueda_multa(multa_min, multa_max):
    libros_condiciones = []

    for multa, copia in enumerate(prestamos):
        if multa[0] in [multa_min, multa_max] and copia[1] != 0:
            libros_condiciones.append(f"{libros[titulo][0]}--{libros[codigo]}")
            libros_condiciones.sort()

    if enumerate(libros_condiciones) > 0:
        print("Resultados: ") 
        print(libros_condiciones)  
    else:
        print("No hay libros en ese rango de multa.") 

# FUNCIONES -- OPCION 3 (BUSQUEDA DE LIBRO POR RANGO DE MULTA)
def actualizar_multa(codigo,nueva_multa,prestamos_diccionario):
    if codigo not in prestamos_diccionario.items():
        return False
    else:
        prestamos_diccionario[codigo][0] = nueva_multa
        return True

# FUNCIONES -- OPCION 4 (ADREGAR LIBRO)
# --- funciones de validacion individual
def validar_codigo(codigo):
    """ Nota: Val, esto solo verifica que sea sin espacios
    la otra verificacion va despues (creo...jeje)"""
    return codigo != "" 

def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_autor(autor):
    return autor.strip() != ""

def validar_genero(genero):
    return genero.strip() != ""

def validar_editorial(editorial):
    return editorial.strip() != ""

# --- Funcion Adregar libro (Maybe)
def adregar_libro(codigo, titulo,autor,genero,year,editorial,es_novedad,precio_multa,copias_disponibles):
    libros[codigo] = titulo, autor , genero , year , editorial, es_novedad
    prestamos[codigo] = precio_multa, copias_disponibles

    print(f"[Sistema: Libro ({titulo}) agregado con exito.]")
    return

# FUNCIONES -- OPCION 5 (ELIMINAR LIBRO)
def eliminar_libro(codigo):
    if codigo not in libros.items() and codigo not in prestamos.items():
        return False
    else:
        del libros['codigo']
        del prestamos['codigo']
        return True
    
    
#FLUJO DEL PROGRAMA
while True:
    mostrar_menu()
    op = ingresar_validar_opcion()
    if op == 1:
        print("-- COPIAS POR GENERO -- ")
        genero = input("Ingrese el genero a consultar: ").strip().lower()
        copias_genero(genero)
    elif op == 2:
        print("-- BUSQUEDA DE LIBROS POR RANGO -- ")
        while True:
            while True:
                try:
                    valor_minimo = int(input("Ingrese multa Minima: "))
                    break
                except ValueError:
                    print("[Error: Debe ingresar solo números enteros]")

            while True:
                try:
                    valor_maximo = int(input("Ingrese multa Maxima: "))
                    break
                except ValueError:
                    print("[Error: Debe ingresar solo números enteros]")

            if valor_maximo >= 0 and valor_minimo >= 0:
                if valor_minimo <= valor_maximo:
                    busqueda_multa(valor_minimo, valor_maximo)
                
                    break
                else:
                    print(["Error: El valor minimo debe ser menor o igual al valor maximo."])
                    continue
            else:
                print(["Error: Los valores deben ser mayores o iguales a 0."])
                continue

        
    elif op == 3:
        print("-- ACTUALIZAR MULTA DE LIBRO -- ")
        while True:
            codigo_libro = input("Ingrese el codigo de libro: ").strip().upper()
            while True:
                try:
                    valor_multa = int(input("Ingrese la nueva multa: $"))
                    break
                except ValueError:
                    print("[Error: La multa deben ser números. Letras o simbolos no están permitidos]")
                    continue
            #Luego de validar los datos ingresados, llamamos la funcion
            Retorno = actualizar_multa(codigo_libro,valor_multa,prestamos)
            if not Retorno:
                print("[Error: El codigo no existe]")
            else:
                print("[Sistema: Multa actualizada]")

            confirm = input("¿Desea actualizar otra multa? (s/n) \n>> ").strip().lower()=="s"
            if confirm:
                continue
            else:
                break 


    elif op == 4:
        print("-- AGREGAR LIBRO -- ")
        codigo = input("Ingrese el codigo del nuevo libro: ").strip().upper()
        bol_codigo = validar_codigo(codigo)
        if not bol_codigo:
            print("[Error: El codigo no puede estar vacio ]")
        else:
            if codigo in libros or codigo in prestamos.items():
                print("[Error: El codigo ya existe ]")
                bol_codigo2 = False 
            else:
                bol_codigo2 = True

                while True:
                    titulo = input("Ingrese el titulo del nuevo libro: ").strip().title()
                    bol_titulo = validar_titulo(titulo)
                    if not bol_titulo:
                        print("[Error: El titulo no puede estar vacio. Regresando al menu]")
                        break
                    
                    autor = input(f"Ingrese el autor de '{titulo}': ").strip().title()
                    bol_autor = validar_autor(autor)
                    if not bol_autor:
                        print("[Error: El autor no puede estar vacio. Regresando al menu ]")
                        break

                    genero = input(f"Ingrese el genero de '{titulo}': ").strip().capitalize()
                    bol_genero = validar_genero(genero)
                    if not bol_genero:
                        print("[Error: El genero no puede estar vacio. Regresando al menu ]")
                        break

                    try:
                        year = int(input(f"Ingrese el año de '{titulo}'"))
                        if year < 0:
                            print("[Error: El año debe ser un número entero mayor que 0. Regresando al menu]")
                            bol_year = False
                            break
                        else:
                            bol_year = True
                    except ValueError:
                        print("[Error: El año del libro debe ser un número. Regresando al menu ]")
                        bol_year = False
                        break

                    editorial = input(f"Ingrese la Editorial de '{titulo}': ").strip().capitalize()
                    bol_editorial = validar_editorial(editorial)
                    if not bol_editorial:
                        print("[Error: La editorial no puede estar vacia. Regresando al menu ]")
                        break
                    
                    es_novedad = input("¿Es novedad? (s/n): ").strip().lower()== "s"
                    if es_novedad:
                        bol_es_novedad = True
                    else:
                        bol_es_novedad = False
                    
                    try:
                        precio_multa = int(input(f"Ingrese el precio de multa para '{titulo}': $"))
                        if precio_multa < 0:
                            print("[Error: El precio de multa debe ser un número entero mayor que 0. Regresando al menu]")
                            bol_precio_multa = False
                            break
                        else:
                            bol_precio_multa = True

                    except ValueError:
                        print("[Error: El precio multa del libro debe ser un número. Regresando al menu ]")
                        bol_precio_multa = False
                        break
                    
                    try:
                        copias_disponibles = int(input(f"Ingrese la cantidad de copias disponibles de '{titulo}': "))
                        if copias_disponibles <= 0:
                            print("[Error: Las copias disponibles deben ser un número entero mayor o igual a 0. Regresando al menu]")
                            bol_copias_disponibles = False
                            break
                        else:
                            bol_copias_disponibles = True

                    except ValueError:
                        print("[Error: Las copias del libro debe ser un número. Regresando al menu ]")
                        bol_precio_multa = False
                        break

                    #Lista de validaciones
                    bols_validados = [bol_codigo2, bol_titulo,bol_autor,bol_genero, bol_year,bol_editorial,bol_es_novedad,bol_precio_multa,bol_copias_disponibles] 
                    if all(bols_validados):
                        #Aqui se confirma que todas las validaciones sean True.
                        adregar_libro(codigo,titulo,autor,genero,year,editorial,es_novedad,precio_multa,copias_disponibles)
    elif op == 5:
        codigo_libro = input("Ingrese el codigo del libro a borrar: ").strip().upper()
        siga = validar_codigo(codigo_libro)
        if siga:
            siga_texto = eliminar_libro(codigo_libro)
            if not siga_texto:
                print("[Estimado usuario: El codigo que desea borrar, no existe el sistema.]")
            else:
                print("Libro eliminado con exito")
    elif op == 6:
        print("Programa finalizando... \n")
        break







        




        






