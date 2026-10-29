#declaramdo una lista 
try:
 alumnos=["jimena","sherlyn","sofia","cecilia","pedro"]
 print(alumnos[2])
 print(alumnos[4])
 calificacion=["6.0","8.7","5.4","9.0","9.6"]
 print("sherlyn tiene:",calificacion[2])
 print("sofia tiene:",calificacion[4])
except IndexError:
 print("mostrar numeron pares")