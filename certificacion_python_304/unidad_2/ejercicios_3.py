letras = [
    ['a','b','c','d','e'],
    ['f','g','h','i','j'],
    ['k','l','m','n','ñ'],
    ['o','p','q','r','s'],
    ['t','u','v','w','x'],
    ['y','z','','','']
]

filas = 6
columnas = 5

for i in range(filas):
    for j in range(columnas):
        if letras [i] [j] !='':
         print(f"[{i}] [{j}]= {letras[i][j]} ")