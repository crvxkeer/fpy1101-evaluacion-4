# =========================
# Sistema de Gestión de Libros
# =========================

# --- Validaciones ---
def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_copias(copias):
    return copias.isdigit() and int(copias) >= 0

def validar_prestamo(prestamo):
    return prestamo.isdigit() and int(prestamo) > 0

# --- Funciones principales ---
def agregar_libro(lista_libros):
    titulo = input("Ingrese título: ")
    if not validar_titulo(titulo):
        print("Error: título no puede estar vacío.")
        return
    
    copias = input("Ingrese cantidad de copias: ")
    if not validar_copias(copias):
        print("Error: copias debe ser un número entero y >= 0")
        return
    
    prestamo = input("Ingrese período de préstamo (días): ")
    if not validar_prestamo(prestamo):
        print("Error: préstamo debe ser un número entero y > 0")
        return
    
    libro = {
        "titulo": titulo,
        "copias": int(copias),
        "prestamo": int(prestamo),
        "disponible": False
    }
    lista_libros.append(libro)
    print("Libro agregado correctamente.")

def buscar_libro(lista_libros, titulo):
    for i, libro in enumerate(lista_libros):
        if libro["titulo"] == titulo:
            return i
    return -1

def eliminar_libro(lista_libros):
    titulo = input("Ingrese título a eliminar: ")
    pos = buscar_libro(lista_libros, titulo)
    if pos != -1:
        lista_libros.pop(pos)
        print(f"Libro '{titulo}' eliminado.")
    else:
        print(f"El libro '{titulo}' no se encuentra registrado.")

def actualizar_disponible(lista_libros):
    for libro in lista_libros:
        libro["disponible"] = libro["copias"] >= 1

def mostrar_libros(lista_libros):
    if len(lista_libros) == 0:
        print("No hay libros registrados todavía.")
        return
    
    actualizar_disponible(lista_libros)
    print("=== LISTA DE LIBROS ===")
    for libro in lista_libros:
        estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']} días")
        print(f"Estado: {estado}")
        print("-" * 30)

# --- Menú ---
def mostrar_menu():
    print("============ MENÚ PRINCIPAL ============")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("========================================")

def leer_opcion():
    opcion = input("Seleccione opción: ")
    if opcion.isdigit() and 1 <= int(opcion) <= 6:
        return int(opcion)
    else:
        print("Opción inválida.")
        return 0

# --- Programa principal ---
def main():
    lista_libros = []
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == 1:
            agregar_libro(lista_libros)
        elif opcion == 2:
            titulo = input("Ingrese título a buscar: ")
            pos = buscar_libro(lista_libros, titulo)
            if pos != -1:
                libro = lista_libros[pos]
                estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
                print("Título del libro:", libro["titulo"])
                print("Copias:", libro["copias"])
                print("Préstamo:", libro["prestamo"], "días")
                print("Estado:", estado)
            else:
                print("No se encontró el libro.")
        elif opcion == 3:
            eliminar_libro(lista_libros)
        elif opcion == 4:
            actualizar_disponible(lista_libros)
            print("Disponibilidad actualizada.")
        elif opcion == 5:
            mostrar_libros(lista_libros)
        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva pronto.")
            break

# Ejecutar
main()
