import threading
import time
import random

class Produtor:
    def __init__(self, identificador):
        self.identificador = identificador
        self.contador = 1  # Contador para identificar os itens produzidos

    def produzir(self, estoque):
        while True:
            # Tempo de produção aleatório entre 1 e 5 segundos
            tempo_espera = random.randint(1, 5)
            time.sleep(tempo_espera)
            
            # Criando um item
            item = (self.identificador, self.contador)
            sucesso = estoque.estocar(item)
            
            if sucesso:
                self.contador += 1
