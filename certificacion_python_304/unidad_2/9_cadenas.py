#cadena y concatenacion con (+)
cadena1='hola'
cadena2='mundo'
multilinea="""esto es una cadena
 de varias lineas"""
print(cadena1+cadena2)#print
#cadena y repeticion
eco='ja'*3
print(eco)
#cambiar una cadena de minuscula a mayuscula
tu_nombre='MARIA FONSECA'
print(tu_nombre.upper())
#cambiar una cadena de mayuscula a minuscula
print(tu_nombre.lower())
#REMPLAZAR TEXTO EN UNA CADENA
frase="me gusta programacion"
print(frase.replace("programacion","matematicas"))
#formato de cadenas (f-string)
edad=15
nombre='MARIA FONSECA'
mensaje=f"hola, me llamo {nombre} y tengo {edad} años"
print(mensaje)
#contar las caracteristicas de una cadena 
texto="¡felicidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#comprobar si un texto contiene una palabra
oracion="aprender python es divertido"
if "ct" in oracion:
    print("encontrando")
else:
    print("no esta")    
#validar contenido con una cadena
nlista=15
print(nlista.isalpha())
print(nlista.isdigit())