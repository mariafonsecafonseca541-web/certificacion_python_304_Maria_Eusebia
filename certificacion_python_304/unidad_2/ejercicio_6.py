tabla = [
    ["nombre","edad","calificacion"],
    ["luis",17,8.0],
    ["jimena",16,8.3],
    ["amanda",16,8.0],
    ["sherlyn",16,9.0],
    ["cecylia",15,10],
    ["litzhi",16,8.9],
    ["ivan",16,7.0],
    ["ivon",16,10],
    ["pedro",17,6.0],
    ["sofia",16,5.0]
]
nombre = input("ingresa un nombre")
filas= len(tabla)
columnas= len(tabla[0])
for i in range(filas):
    for j in range(columnas):
            if tabla[i][j] == nombre:
             print(f"nombre encintrado en la pocision [{i}][{j}]")
             print(f"edad {tabla[i][j]}")
             print(f"calificacion  {tabla[i][j]}") 