# Sistema de préstamo de libros de una biblioteca

print("====================================")
print("     SISTEMA DE PRESTAMO DE LIBROS")
print("====================================")

# Pedir nombre del usuario
nombre_usuario = input("Ingrese el nombre del usuario: ")

while nombre_usuario == "" or not nombre_usuario.replace(" ", "").isalpha():
    print("Error: eso no es un nombre valido. Solo se permiten letras.")
    nombre_usuario = input("Ingrese el nombre del usuario: ")

# Pedir nombre del libro
nombre_libro = input("Ingrese el nombre del libro: ")

while nombre_libro == "":
    print("Error: debe escribir el nombre del libro.")
    nombre_libro = input("Ingrese el nombre del libro: ")

print("\nVerificacion de datos del usuario")

# Preguntar si tiene carnet
tiene_carnet = input("¿El usuario tiene carnet? (si/no): ")

while tiene_carnet != "si" and tiene_carnet != "no":
    print("Error: solo puede escribir si o no.")
    tiene_carnet = input("¿El usuario tiene carnet? (si/no): ")

# Preguntar si tiene multas
tiene_multas = input("¿El usuario tiene multas pendientes? (si/no): ")

while tiene_multas != "si" and tiene_multas != "no":
    print("Error: solo puede escribir si o no.")
    tiene_multas = input("¿El usuario tiene multas pendientes? (si/no): ")

print("\nProcesando solicitud de prestamo...")
print("------------------------------------")

# Datos del préstamo
dias_prestamo = 7
fecha_prestamo = "13/03/2026"

# Verificar condiciones
if tiene_carnet == "si" and tiene_multas == "no":

    print("\nPrestamo aprobado")
    print("--------------------------")
    print("Usuario:", nombre_usuario)
    print("Libro solicitado:", nombre_libro)
    print("Dias de prestamo:", dias_prestamo)
    print("Fecha del prestamo:", fecha_prestamo)
    print("Recuerde devolver el libro a tiempo")

else:

    print("\nNo se puede realizar el prestamo")
    print("--------------------------------")
    
    if tiene_carnet == "no":
        print("Motivo: el usuario no tiene carnet de biblioteca")
    
    if tiene_multas == "si":
        print("Motivo: el usuario tiene multas pendientes")

print("\nGracias por usar el sistema de biblioteca")
print("Fin del programa")