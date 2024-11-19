import random


opciones = ['papel','tijera','piedra']

def OpcionRespuesta():
    return random.randint(0,2)

def Analizar(respuesta):
    opcion = respuesta.lower().strip()

    

    if (opcion not in opciones):
        return 'Opción incorrecta'
    else:
        return Jugar(opcion)
    
def Jugar(opcion):
    valor_jugador= opciones.index(opcion)
    valor_computador = OpcionRespuesta()

    opcion_computador=f'Computador:{opciones[valor_computador]}'
    
    if(valor_computador==valor_jugador):
        return opcion_computador+'\r\nNadie gana'

    if (((valor_jugador==0 and valor_computador==2) or valor_jugador>valor_computador) and not (valor_computador==0 and valor_jugador==2)):
        return opcion_computador+'\r\nGanas Tú'
    else:
        return opcion_computador+'\r\nGano Yo'


def Ronda():
    while True:
        opcion=input('Jugador (piedra,papel o tijera):')
        print(Analizar(opcion))

Ronda()
