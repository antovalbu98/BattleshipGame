from Clases import Jugador
import numpy as np
from Constantes import PARTE_BARCO, DIMENSIONES, MAR, AGUA, TOCADO

jugador = Jugador("jugador")
maquina = Jugador("maquina")

dificultad = None


def iniciar():
    global dificultad

    print("\n")
    print('HUNDIR LA FLOTA\
          \n-Bienvenido al reto de vencer a LA MÁQUINA-')


    print("\n")

    jugador.posicionar_todos()

    maquina.posicionar_todos()

    dificultad = str(input('Elige un nivel de dificultad para el juego: \
                                             \n\tIntroduce "F" para nivel FACIL \
                                             \n\tIntroduce "M" para nivel MEDIO \
                                             \n\tIntroduce "D" para nivel DIFICIL\: '))

    while dificultad not in ['F', 'M', 'D', 'f', 'm', 'd']:
        dificultad = str(input('Has introducido una orden errónea, introduce de nuevo tu nivel:\
                                             \n\tIntroduce "F" para nivel FACIL \
                                             \n\tIntroduce "M" para nivel MEDIO \
                                             \n\tIntroduce "D" para nivel DIFICIL\: '))
        continue

    if dificultad == 'F' or dificultad == 'f':
        print('\nHas decidido jugar en modo FACIL')
    elif dificultad == 'M' or dificultad == 'm':
        print('\nHas decidido jugar en modo MEDIO')
    elif dificultad == 'D' or dificultad == 'd':
        print('\nHas decidido jugar en modo DIFICIL\
                  \n Que la suerte te acompañe...')

    print("Comienzas el juego con un total de %s vidas:" % (np.count_nonzero(jugador.tablero_barcos == PARTE_BARCO)),
          "\n",
          'Este es tu tablero con tus barcos colocados aleatoriamente: \n', jugador.tablero_barcos)

    print("Tu enemigo tiene %s barcos activos" % (np.count_nonzero(maquina.tablero_barcos == PARTE_BARCO)))
         # "\n Tablero de disparos: \n", jugador.tablero_disparos)

    jugar()


def disparo():

    while (np.count_nonzero(jugador.tablero_barcos == PARTE_BARCO) == 0) or (
            np.count_nonzero(maquina.tablero_barcos == PARTE_BARCO) == 0):
        break

    print("Tablero de disparos:\n", jugador.tablero_disparos)
    lista = list(range(0, DIMENSIONES))  # argucia para que si no metes un input fila o columna que no corresponda
    listastrings = []  # a una coordenada, el programa no falle y te siga pidiendo coordenadas
    for i in lista:
        listastrings.append(str(i))

    while (np.count_nonzero(jugador.tablero_barcos == PARTE_BARCO) != 0) and (
            np.count_nonzero(maquina.tablero_barcos == PARTE_BARCO) != 0):

        inpfila = input('Introduce la coordenada fila de tu disparo: ')

        while inpfila not in listastrings:
            inpfila = input('Coordenada erronea: Introduce la coordenada fila de nuevo: ')

            continue

        inpcolumna = input('Introduce la coordenada columna de tu disparo: ')

        while inpcolumna not in listastrings:
            inpcolumna = input('Coordenada errónea: Introduce la coordenada fila de nuevo: ')

            continue

        fila = int(inpfila)  # las coordenadas fila y columna son validas... a disparar
        columna = int(inpcolumna)

        print("Disparaste sobre la coordenada", (fila,columna))

        if maquina.tablero_barcos[fila, columna] == MAR:
            maquina.tablero_barcos[fila, columna] = AGUA
            jugador.tablero_disparos[fila, columna] = AGUA

            print("Tablero con tus disparos: \n", jugador.tablero_disparos)
            print("¡HAS FALLADO!")

            menu = str(input('Ahora es el turno de la máquina\
                                         \n\tIntroduce "C" para continuar \
                                         \n\tIntroduce "V" para ver el marcador de vidas\
                                         \n\tIntroduce "R" para reiniciar el juego\
                                         \n\tIntroduce "S" para salir del juego: '))

            while menu not in ['C', 'R', 'S', 'V', 'v', 'c', 's', 'r']:
                menu = str(input('Has introducido una orden errónea, introduce de nuevo tu opción:\
                                                         \n\tIntroduce "C" para continuar \
                                                         \n\tIntroduce "V" para ver el marcador de vidas\
                                                         \n\tIntroduce "R" para reiniciar el juego\
                                                         \n\tIntroduce "S" para salir del juego: '))
                continue

            if menu == 'C' or menu == 'c':
                disparo_maquina()

            elif menu == 'V' or menu == 'v':
                print('Te quedan %s vidas' % (np.count_nonzero(jugador.tablero_barcos == PARTE_BARCO)))
                print('A la máquina le quedan %s vidas' % (np.count_nonzero(maquina.tablero_barcos == PARTE_BARCO)))
                disparo_maquina()

            elif menu == 'R' or menu == 'r':
                jugador.tablero_barcos = np.full((DIMENSIONES, DIMENSIONES), MAR)
                jugador.tablero_disparos = np.full((DIMENSIONES, DIMENSIONES), MAR)
                maquina.tablero_barcos = np.full((DIMENSIONES, DIMENSIONES), MAR)
                maquina.tablero_disparos = np.full((DIMENSIONES, DIMENSIONES), MAR)
                iniciar()

            elif menu == 'S' or menu == 's':
                exit()


        elif maquina.tablero_barcos[fila, columna] == PARTE_BARCO:
            maquina.tablero_barcos[fila, columna] = TOCADO
            jugador.tablero_disparos[fila, columna] = TOCADO

            print('¡TOCADO! Acertaste con el disparo')
            print('\nTablero disparos \n', jugador.tablero_disparos)
            print('\nVuelve a ser tu turno, ¡DISPARAS DE NUEVO!\n')

            disparo()

        elif maquina.tablero_barcos[fila, columna] == TOCADO:

            print("Ya habias disparado sobre esa coordenada (X). Dispara de nuevo.")
            disparo()

        elif maquina.tablero_barcos[fila, columna] == AGUA:

            print("Ya habias disparado sobre esa coordenada (A). Dispara de nuevo.")
            disparo()


def disparo_maquina():

    while (np.count_nonzero(jugador.tablero_barcos == PARTE_BARCO) == 0) or (
            np.count_nonzero(maquina.tablero_barcos == PARTE_BARCO) == 0):
        break

    fila = []
    columna = []

    if dificultad == 'F' or dificultad == 'f':

        fila = np.random.randint(DIMENSIONES)
        columna = np.random.randint(DIMENSIONES)

    elif dificultad == 'M' or dificultad == 'm':

        set_disparos = []

        for i in range(3):

            fila = np.random.randint(DIMENSIONES)
            columna = np.random.randint(DIMENSIONES)

            if jugador.tablero_barcos[fila, columna] == PARTE_BARCO:
                set_disparos.append((fila, columna))
                break

            elif jugador.tablero_barcos[fila, columna] != PARTE_BARCO:
                set_disparos.append((fila, columna))
                continue

        print(set_disparos)

    elif dificultad == 'D' or dificultad == 'd':

        set_disparos = []

        for i in range(50):

            fila = np.random.randint(DIMENSIONES)
            columna = np.random.randint(DIMENSIONES)

            if jugador.tablero_barcos[fila, columna] == PARTE_BARCO:
                set_disparos.append((fila, columna))
                break

            elif jugador.tablero_barcos[fila, columna] != PARTE_BARCO:
                set_disparos.append((fila, columna))
                continue

        fila = set_disparos[-1][0]
        columna = set_disparos[-1][1]

        print(set_disparos)

    print('El disparo de tu enemigo ha caido en las coordenadas (%s,%s) de tu tablero' % (fila, columna))

    if jugador.tablero_barcos[fila, columna] == MAR:
        jugador.tablero_barcos[fila, columna] = AGUA

        print("\nTus barcos con los disparos que ha efectuado la máquina: \n", jugador.tablero_barcos)
        print('¡AGUA! la maquina falló! \n')
        # print("Tablero disparos \n\n", jugador.tablero_disparos)

        peticion = str(input('Ahora es tu turno\
                                 \n\tIntroduce "C" para continuar \
                                 \n\tIntroduce "V" para ver el marcador de vidas\
                                 \n\tIntroduce "R" para reiniciar el juego\
                                 \n\tIntroduce "S" para salir del juego: '))

        while peticion not in ['C', 'R', 'S', 'V', 'v', 'c', 's', 'r']:
            peticion = str(input('Has introducido una orden errónea, introduce de nuevo tu opción:\
                                     \n\tIntroduce "C" para continuar \
                                     \n\tIntroduce "V" para ver el marcador de vidas\
                                     \n\tIntroduce "R" para reiniciar el juego\
                                     \n\tIntroduce "S" para salir del juego '))
            continue

        if peticion == 'C' or peticion == 'c':
            disparo()

        elif peticion == 'V' or peticion == 'v':
            print('Te quedan %s vidas' % (np.count_nonzero(jugador.tablero_barcos == PARTE_BARCO)))
            print('A la máquina le quedan %s vidas' % (np.count_nonzero(maquina.tablero_barcos == PARTE_BARCO)))
            disparo()

        elif peticion == 'R' or peticion == 'r':
            jugador.tablero_barcos = np.full((DIMENSIONES, DIMENSIONES), MAR)
            jugador.tablero_disparos = np.full((DIMENSIONES, DIMENSIONES), MAR)
            maquina.tablero_barcos = np.full((DIMENSIONES, DIMENSIONES), MAR)
            maquina.tablero_disparos = np.full((DIMENSIONES, DIMENSIONES), MAR)
            iniciar()

        elif peticion == 'S' or peticion == 's':
            exit()

    elif jugador.tablero_barcos[fila, columna] == PARTE_BARCO:
        jugador.tablero_barcos[fila, columna] = TOCADO

        print('¡HAN ALCANZADO UNO DE TUS BARCOS!')
        print("Comprueba cuántos siguen a flote en tu tablero: \n\n", jugador.tablero_barcos)

        peticion = str(input('Vuelve a ser el turno de la máquina\
                                         \n\tIntroduce "C" para continuar \
                                         \n\tIntroduce "V" para ver el marcador de vidas\
                                         \n\tIntroduce "R" para reiniciar el juego\
                                         \n\tIntroduce "S" para salir del juego: '))

        while peticion not in ['C', 'R', 'S', 'V', 'v', 'c', 's', 'r']:
            peticion = str(input('Has introducido una orden errónea, introduce de nuevo tu opción:\
                                     \n\tIntroduce "C" para continuar \
                                     \n\tIntroduce "V" para ver el marcador de vidas\
                                     \n\tIntroduce "R" para reiniciar el juego\
                                     \n\tIntroduce "S" para salir del juego '))
            continue

        if peticion == 'C' or peticion == 'c':
            disparo_maquina()

        elif peticion == 'V' or peticion == 'v':
            print('Te quedan %s vidas' % (np.count_nonzero(jugador.tablero_barcos == PARTE_BARCO)))
            print('A la máquina le quedan %s vidas' % (np.count_nonzero(maquina.tablero_barcos == PARTE_BARCO)))
            disparo_maquina()

        elif peticion == 'R' or peticion == 'r':
            iniciar()

        elif peticion == 'S' or peticion == 's':
            exit()

    elif jugador.tablero_barcos[fila, columna] == AGUA:

        disparo_maquina()


def jugar():
    while (np.count_nonzero(jugador.tablero_barcos == PARTE_BARCO) != 0) and (
            np.count_nonzero(maquina.tablero_barcos == PARTE_BARCO) != 0):

        print("Es tu turno")

        disparo()

    else:

        if np.count_nonzero(jugador.tablero_barcos == PARTE_BARCO) == 0:

            print('¡Has perdido todos tus barcos!\nGAME OVER')

            peticion = str(input('¿Qué quieres hacer?\
                                                         \n\tIntroduce "R" para reiniciar el juego\
                                                         \n\tIntroduce "S" para salir del juego: '))

            while peticion not in ['C', 'R', 'S', 'V', 'v', 'c', 's', 'r']:
                peticion = str(input('\nHas introducido una orden errónea, introduce de nuevo tu opción:\
                                                             \n\tIntroduce "R" para reiniciar el juego\
                                                             \n\tIntroduce "S" para salir del juego '))
                continue

            if peticion == 'R' or peticion == 'r':
                jugador.tablero_barcos = np.full((DIMENSIONES, DIMENSIONES), MAR)
                jugador.tablero_disparos = np.full((DIMENSIONES, DIMENSIONES), MAR)
                maquina.tablero_barcos = np.full((DIMENSIONES, DIMENSIONES), MAR)
                maquina.tablero_disparos = np.full((DIMENSIONES, DIMENSIONES), MAR)
                iniciar()

            elif peticion == 'S' or peticion == 's':
                exit()

        elif np.count_nonzero(maquina.tablero_barcos == PARTE_BARCO) == 0:

            print('¡Has ganado! ¡Destruiste todos los barcos enemigos!')

            peticion = str(input('¿Qué quieres hacer?\
                                                         \n\tIntroduce "R" para reiniciar el juego\
                                                         \n\tIntroduce "S" para salir del juego: '))

            while peticion not in ['C', 'R', 'S', 'V', 'v', 'c', 's', 'r']:
                peticion = str(input('\nHas introducido una orden errónea, introduce de nuevo tu opción:\
                                                             \n\tIntroduce "R" para reiniciar el juego\
                                                             \n\tIntroduce "S" para salir del juego '))
                continue

            if peticion == 'R' or peticion == 'r':
                jugador.tablero_barcos = np.full((DIMENSIONES, DIMENSIONES), MAR)
                jugador.tablero_disparos = np.full((DIMENSIONES, DIMENSIONES), MAR)
                maquina.tablero_barcos = np.full((DIMENSIONES, DIMENSIONES), MAR)
                maquina.tablero_disparos = np.full((DIMENSIONES, DIMENSIONES), MAR)
                iniciar()

            elif peticion == 'S' or peticion == 's':
                exit()

