import threading
import time
import random

class Produtor:
    def __init__(self, identificador):
        self.identificador = identificador
        self.contador = 1  

    def produzir(self, estoque):
        while True:
            tempo_espera = random.randint(1, 5)
            time.sleep(tempo_espera)
            
            item = (self.identificador, self.contador)
            sucesso = estoque.estocar(item)
            
            if sucesso:
                self.contador += 1
