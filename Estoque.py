import threading
import time
import random

class Estoque:
    def __init__(self, tamanho_maximo=10):
        self.estoque = []
        self.tamanho_maximo = tamanho_maximo
        self.lock = threading.Lock()  

    def estocar(self, produto):
        with self.lock:
            if len(self.estoque) < self.tamanho_maximo:
                self.estoque.append(produto)
                print(f"Produtor {produto[0]} armazena item {produto[1]}")
            else:
                print("Estoque cheio, aguardando espaço.")
                return False
        return True

    def remover(self):
        with self.lock:
            if len(self.estoque) > 0:
                produto = self.estoque.pop(0)
                print(f"Consumidor {produto[0]} recebe item {produto[1]}")
                return produto
            else:
                print("Estoque vazio, aguardando item.")
                return None
