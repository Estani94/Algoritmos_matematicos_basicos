#Algorítmo 2: Derminar la cantidad de dígitos

#Definimos la función
def cantidad_digitos(numero):
    valor_remanente = numero
    contador = 0
    while valor_remanente > 0:
        valor_remanente = valor_remanente // 10
        contador += 1
    print(contador)
#Solicitamos al usuario que ingrese un número:
dato = int(input("Digite un número: "))
#Mostramos por pantalla los dígitos del número:
cantidad_digitos(dato)