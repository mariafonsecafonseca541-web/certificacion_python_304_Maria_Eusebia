#creando un diccionario
persona={
    "nombre":"MARY",
    "edad":15,
    "profecion":"programador",
    "estudiante":True
}
print(persona)
#accediendo a un valor en especifico
print(persona["nombre"])
#se puede usar el metodo get()
#es util porque no marca error si el valor no existe
print(persona.get("profecion"))