nombre = input("Ingrese su nombre:")
print("Hola", nombre)

edad = int(input("Ingrese su edad:"))
print("Tienes", edad)


nota1 = float(input("Ingrese nota1:"))
nota2 = float(input("Ingrese nota2:"))
nota3 = float(input("Ingrese nota3:"))

Promedio = (nota1+nota2+nota3)/3


if Promedio >=71:
    print("Aprobado")
else:
    print("No aprobado")