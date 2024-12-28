Objetivo: O objetivo principal é estudar a utilização de threads e controle de regiões críticas na linguagem Python. Basicamente, estudar sobre o uso das bibliotecas thread e threading.

Tarefa: Implementar em python um sistema produtor-consumidor que vai utilizar objetos de três classes distintas: Produtor, Consumidor e Estoque. O sistema vai empregar 3 consumidores, 3 produtores e 1 estoque.

Cada objeto da classe Produtor vai funcionar numa thread que produzirá, a cada X segundos, um item representado por um par (int, int). O primeiro inteiro do par identifica o código do produtor e o segundo inteiro identifica o código do item. Cada item recebe um identificador diferente, criado incrementalmente. O tempo de produção de um item, em cada produtor,  custa X segundos (um tempo de atraso aleatório entre 1 e 5 segundos). Existe um limite máximo no tamanho do estoque; se o estoque estiver cheio, o produtor deve esperar até surgir espaço livre no estoque.

Cada objeto da classe Consumidor vai funcionar numa thread que consumirá, a cada Y segundos,  um item armazenado no estoque. Para variar o tempo Y de requisição do consumidor, utilize um atraso aleatório entre 1 e 3 segundos para cada pedido. Se o estoque estiver vazio quando o consumidor requisitar um item, ele deve esperar até o estoque fornecer o produto.

O objeto da classe Estoque implementa uma fila (FIFO) capaz de armazenar até 10 produtos, trate essa fila como região crítica. A cada item armazenado, o objeto imprimirá a mensagem “Produtor P armazena item Q.” onde P e Q são os identificadores do produtor e do item respectivamente. A cada item fornecido para um consumidor, o objeto imprimirá a mensagem “Consumidor C recebe item Q.”

Referências:
– repositório com exemplos sobre multiprogramação em python:
https://www.bogotobogo.com/python/Multithread/python_multithreading_creating_threads.php
