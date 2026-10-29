promedio=float(input("ingresa tu promedio:"))
#el numero imgresado es 9
if promedio<0:
    print("el numero es invalido")
elif promedio<=5:
    print("tu promedio es muy bajo")
elif promedio>5 and promedio<=6:
    print("tu promedio es bajo")
elif promedio>7 and promedio<=9:
    print("tu promedio es bueno")
elif promedio>9 and promedio<=10:
    print("tu promedio es exelente")
else:
    print("ese promedio no existe")            