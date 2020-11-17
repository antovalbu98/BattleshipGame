import numpy as np
import random

from Constantes import DIMENSIONES, MAR, PARTE_BARCO, BARCOS, TOCADO, AGUA

class Jugador:

    def __init__(self, id):

        self.id_jugador = id
        self.tablero_barcos = np.full((DIMENSIONES, DIMENSIONES), MAR)
        self.tablero_disparos = np.full((DIMENSIONES, DIMENSIONES), MAR)

    def poner1barco(self, eslora):

            while True:

                fila = np.random.randint(DIMENSIONES)
                columna = np.random.randint(DIMENSIONES)
                orientacion = random.choice(['N', 'S', 'E', 'W'])

                if (orientacion == 'N') and ((np.count_nonzero(
                        self.tablero_barcos[fila - eslora:fila + 2, columna] != PARTE_BARCO)) == eslora + 2) and \
                        ((np.count_nonzero(self.tablero_barcos[fila - eslora + 1:fila + 1,
                                           columna - 1: columna + 2] != PARTE_BARCO)) == 3 * eslora):
                    self.tablero_barcos[fila:fila - eslora:-1, columna] = PARTE_BARCO
                    break

                elif (orientacion == "S") and ((np.count_nonzero(
                        self.tablero_barcos[fila - 1: fila + eslora + 1, columna] != PARTE_BARCO)) == eslora + 2) and \
                        ((np.count_nonzero(self.tablero_barcos[fila:fila + eslora,
                                           columna - 1: columna + 2] != PARTE_BARCO)) == 3 * eslora):
                    self.tablero_barcos[fila:fila + eslora:1, columna] = PARTE_BARCO
                    break

                elif (orientacion == "E") and ((np.count_nonzero(self.tablero_barcos[fila, columna - 1:(
                        columna + eslora + 1)] != PARTE_BARCO)) == eslora + 2) and \
                        ((np.count_nonzero(self.tablero_barcos[fila - 1: fila + 2,
                                           columna: columna + eslora] != PARTE_BARCO)) == 3 * eslora):
                    self.tablero_barcos[fila, columna:(columna + eslora):1] = PARTE_BARCO
                    break

                elif (orientacion == "W") and ((np.count_nonzero(
                        self.tablero_barcos[fila, columna - eslora: columna + 2] != PARTE_BARCO)) == eslora + 2) and \
                        ((np.count_nonzero(self.tablero_barcos[fila - 1: fila + 2,
                                           columna - eslora + 1: columna + 1] != PARTE_BARCO)) == 3 * eslora):
                    self.tablero_barcos[fila, columna: (columna - eslora): -1] = PARTE_BARCO
                    break

    def posicionar_todos(self):

        for i in BARCOS:
            self.poner1barco(BARCOS[i])