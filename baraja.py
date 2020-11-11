import random

#creamos lista con todas las cartas
numeros = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']
#creamos lista todos los palos de la baraja
palos = ['o', 'c', 'e', 'b']

#tenemos que concatenar las cartas con los palos para generar la baraja
def crearBaraja ():
    baraja = []
    for palo in palos:
        for numero in numeros:
            baraja.append(numero+palo)
    
    return baraja

#esta funcion nos ayuda a entender como intercambiar valores dentro de una lista
'''
def intercambio (v1,v2):
    aux = v1
    v1 = v2
    v2 = aux

    return v1, v2
'''

#Definimos una funcion que pueda intercambiar posiciones en cualquier lista.
def barajar (lista_de_cartas):

    #Poniendo in range conseguimos iterar en los indices de la lista (hasta la longitud de la lista), no los valores.
    for i in range(len(lista_de_cartas)):
        #usando el random.range creamos un valor de posicion nuevo que luego intercambiaremos con la i que vamos iterando
        nueva_posicion = random.randrange (len(lista_de_cartas))

        aux = lista_de_cartas[nueva_posicion]
        lista_de_cartas[nueva_posicion] = lista_de_cartas [i]
        lista_de_cartas [i] = aux
    
    return lista_de_cartas

miBaraja = crearBaraja()
barajar (miBaraja)
print (miBaraja)


        

    