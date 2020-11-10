#creamos lista con todas las cartas
numeros = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']
#creamos lista todos los palos de la baraja
palos = ['o', 'c', 'e', 'b']

baraja = []

#Tenemos que concatenar las cartas con los palos para generar la baraja
def Crearbaraja ():
    for palo in palos:
        for numero in numeros:
            baraja.append(numero+palo)
    
    return baraja

Crearbaraja()
    

