#ciclo externo para el numero de la base de la tabla
for i in range(1,4):
    print(f"---Tabla del {i}---")
    #ciclo interno nos mulplica la base (1) por el nimero (j)
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print(f"AQUI TERMINA LA TABLA DEL {i}")