from Estoque import Estoque
from Produtor import Produtor
from Consumidor import Consumidor
import threading

def main():
    estoque = Estoque()

    produtores = [Produtor(i + 1) for i in range(3)]
    consumidores = [Consumidor(i + 1) for i in range(2)]

    threads_produtores = [
        threading.Thread(target=produtor.produzir, args=(estoque,))
        for produtor in produtores
    ]
    
    threads_consumidores = [
        threading.Thread(target=consumidor.consumir, args=(estoque,)) 
        for consumidor in consumidores
    ]

    for thread in threads_produtores:
        thread.daemon = True
        thread.start()

    for thread in threads_consumidores:
        thread.daemon = True
        thread.start()

    try:
        while True:
            pass  
    except KeyboardInterrupt:
        print("Execução interrompida.")

if __name__ == "__main__":
    main()
