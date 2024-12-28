import threading
import time
import random

class Consumidor:
    def __init__(self, identificador):
        self.identificador = identificador

    def consumir(self, estoque):
        while True:
            tempo_espera = random.randint(1, 3)
            time.sleep(tempo_espera)

            item = estoque.remover()

            if item is None:
                time.sleep(1)
