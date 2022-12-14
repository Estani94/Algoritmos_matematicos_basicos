#Algorítmo 1: Función para extraer los dígitos de un número

#Definimos la función
def extraer_digitos(numero):
 valor_remanente = numero
 while valor_remanente > 0:
    digito = valor_remanente % 10               #Se agrega una coma hacia la izquierda del número, el número a la derecha de la coma será nuestro
                                                #1er dígito
    valor_remanente = valor_remanente // 10     #Se corta el número que queda luego de dividirlo por 10 hasta la coma
    print(digito, end=' ')
 print()
#Solicitamos al usuario que ingrese un número:
dato = int(input("Digite un número: "))
#Mostramos por pantalla los dígitos del número
extraer_digitos(dato)