#ejemplo 1 sin manejo de excepciones

try:
    numero1=float(input("ingresa el primer numero"))
    numero2=float(input("ingresa el segundo numero"))
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
   print("eror: no se puede dividir un numero entre cero")
except ValueError:
    print("eror: nose puede colocar letras")