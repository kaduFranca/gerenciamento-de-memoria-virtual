# FIFO LFU LRU e NRU.

Aqui está uma breve explicação de cada um desses algoritmos:

FIFO (First-In, First-Out): Nesse algoritmo, a página mais antiga que foi trazida para a memória é a primeira a ser substituída. É como uma fila, onde a página que entrou primeiro é a primeira a sair. O FIFO não leva em consideração a frequência de uso ou a importância das páginas, apenas a ordem em que elas foram carregadas.

LFU (Least Frequently Used): O LFU é baseado na ideia de que as páginas que foram menos usadas no passado têm uma menor probabilidade de serem usadas no futuro. Esse algoritmo mantém uma contagem de quantas vezes cada página foi referenciada e, quando ocorre uma falta de página, substitui a página com a menor contagem.

LRU (Least Recently Used): O LRU substitui a página que não foi usada há mais tempo. Ele se baseia na ideia de que as páginas que não foram referenciadas por um longo período têm uma menor probabilidade de serem usadas em comparação com as páginas que foram usadas recentemente. O LRU geralmente é implementado mantendo uma lista ordenada das páginas com base em sua última referência, e a página no início da lista é substituída.

NRU (Not Recently Used): O NRU é uma versão simplificada do LRU, que divide as páginas em diferentes classes com base em seu estado de uso recente. Normalmente, essas classes são: (1) páginas referenciadas recentemente e modificadas, (2) páginas referenciadas recentemente, mas não modificadas, (3) páginas não referenciadas recentemente, mas modificadas, e (4) páginas não referenciadas recentemente e não modificadas. O NRU substitui uma página aleatória da classe de menor prioridade, dando preferência a páginas que não foram referenciadas recentemente.

Cada algoritmo possui vantagens e desvantagens, e a escolha de qual utilizar depende das características do sistema e dos requisitos específicos do ambiente em que está sendo aplicado.



Desenvolva os algoritmos de substituição de páginas FIFO, LFU LRU e NRU.

O algoritmo deverá receber por parâmetro a lista de frames alocadas na memória principal.

Cada frame contêm as informações de ID, tempo de carga, quantidade de referências, tempo da última referência, BR e BM.

Por exemplo:

![image](https://user-images.githubusercontent.com/102994285/203656955-509531a5-0421-4e94-966a-957e3657891d.png)

O algoritmo deverá retornar o ID do frame que deverá ser substituído.

O algoritmo deverá receber por parâmetro a lista de frames alocados.
O algoritmo deverá retornar o ID do frame a ser substituído.
O algoritmo deverá ser testado com diferentes listas de páginas.
Os algoritmos podem ser desenvolvidos em qualquer linguagem de programação
