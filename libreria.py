print("=================================")
print("SISTEMA DE PRESTAMO DE LIBROS")
print("=================================")

# Sistema de préstamo de libros de una biblioteca
nombre_usuario = input("Ingrese el nombre del usuario: ")
nombre_libro = input("Nombre del libro que desea prestar: ")
print("\nVerificacion de datos del usuario")
tiene_carnet = input("¿El usuario tiene carnet? (si/no): ")
tiene_multas = input("¿El usuario tiene multas pendientes? (si/no): ")

print("\nProcesando solicitud de prestamo...")

dias_prestamo = 7
fecha_prestamo = "13/03/2026"

if tiene_carnet == "si" and tiene_multas == "no":

    print("Prestamo aprobado")
    print("Usuario:", nombre_usuario)
    print("Libro:", nombre_libro)
    print("Dias de prestamo:", dias_prestamo)
    print("Fecha del prestamo:", fecha_prestamo)

else:

    print("No se puede prestar el libro")

print("\nGracias por usar el sistema de biblioteca")
print("Fin del programa")