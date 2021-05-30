#DICCIONARIO
valores={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":1,"K":2,"L":3,"M":4,"N":5,"Ñ":6,"O":7,"P":8,"Q":9,"R":1,"S":2,"T":3,"U":4,"V":5,"W":6,"X":7,"Y":8,"Z":9, " ":0}

#LISTAS
lista_nombre1=[]
lista_nombre2=[]
lista_apellido1=[]
lista_apellido2=[]

############################################PRIMER NOMBRE############################################################

nombre1=input("Ingrese el primer nombre: ")

for i in nombre1: #Nombre 1
    posicion=nombre1.find(i)
    caracter=nombre1[posicion]
    valor=valores[caracter]
    lista_nombre1.append(valor)

def suma_nombre1(lista_nombre1): # Suma Nombre 1
    s_nombre1=0
    for i in lista_nombre1:
        s_nombre1=s_nombre1+i
    return s_nombre1

############################################SEGUNDO NOMBRE############################################################

nombre2=input("Ingrese el segundo nombre: ")

for i in nombre2: #Nombre 2
    posicion=nombre2.find(i)
    caracter=nombre2[posicion]
    valor=valores[caracter]
    lista_nombre2.append(valor)

def suma_nombre2(lista_nombre2): # Suma Nombre 2
    s_nombre2=0
    for i in lista_nombre2:
        s_nombre2=s_nombre2+i
    return s_nombre2


############################################PRIMER APELLIDO############################################################


apellido1=input("Ingrese el primer apellido: ")

for i in apellido1: #Apellido 1
    posicion=apellido1.find(i)
    caracter=apellido1[posicion]  
    valor=valores[caracter]
    lista_apellido1.append(valor)

def suma_apellido1(lista_apellido1): # Suma Apellido 1
    s_apellido1=0
    for i in lista_apellido1:
        s_apellido1=s_apellido1+i
    return s_apellido1


############################################SEGUNDO APELLIDO############################################################


apellido2=input("Ingrese el segundo apellido: ")

for i in apellido2: #Apellido 2
    posicion=apellido2.find(i)
    caracter=apellido2[posicion]  
    valor=valores[caracter]
    lista_apellido2.append(valor)

def suma_apellido2(lista_apellido2): # Suma Apellido 2
    s_apellido2=0
    for i in lista_apellido2:
        s_apellido2=s_apellido2+i
    return s_apellido2


#print("La suma del Nombre 1 es: " + str(suma_nombre1(lista_nombre1)))

#print("La suma del Nombre 2 es: " + str(suma_nombre2(lista_nombre2)))

#print("La suma del Apellido 1 es: " + str(suma_apellido1(lista_apellido1)))

#print("La suma del Apellido 2 es: " + str(suma_apellido2(lista_apellido2)))

suma_nombres = suma_nombre1(lista_nombre1) + suma_nombre2(lista_nombre2)
suma_apellidos = suma_apellido1(lista_apellido1) + suma_apellido2(lista_apellido2)

print("Su número de la suerte es: "+str(suma_nombres)+str(suma_apellidos))
input("Presione ENTER para finalizar")