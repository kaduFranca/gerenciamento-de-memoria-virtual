def ord(v):
  return v[1]#Funcao para pegar a Quantidade Referências, para usar de paramentro para ordenacao no metodo .sort
lista = [[1,12,10,20,1,1],[2,10,1,12,0,0],[3,11,2,21,1,0]]
print(f'Para a lista de frames:\n{lista}')
#FIFO
FIFO = []
for i in range(len(lista)):
  FIFO.append(lista[i][0])
FIFO.sort()
print(f'A sequencia de frames a ser substituidos utilizando FIFO será: {FIFO}')

#LFU
LFUincomplete = []
LFU = []
max = 0
for i in range(len(lista)):
  aux = []
  if lista[i][2] >= max:#if para verificar se o valor da Quantidade Referências é o maior, se for, joga pro fim do array LFUincomplete
    max = lista[i][2]
    aux.append(lista[i][0])
    aux.append(lista[i][2])
  if lista[i][2] < max:#if para verificar se o valor da Quantidade Referências é o menor, se for, joga pro inicio do array LFUincomplete
    aux.append(lista[i][0])
    aux.append(lista[i][2])
  LFUincomplete.append(aux)#faz a adcao do array local "aux" no array LFUincomplete
LFUincomplete.sort(key=ord)#Ordena o array LFUincomplete com base na Quantidade Referências
for i in range(len(LFUincomplete)):
  LFU.append(LFUincomplete[i][0])
print(f'A sequencia de frames a ser substituidos utilizando LFU será: {LFU}')

#LRU
LRUincomplete = []
LRU = []
max = 0
for i in range(len(lista)):
  aux = []
  if lista[i][3] >= max:#if para verificar se o valor da Quantidade Referências é o maior, se for, joga pro fim do array LRUincomplete
    max = lista[i][2]
    aux.append(lista[i][0])
    aux.append(lista[i][3])
  if lista[i][2] < max:#if para verificar se o valor da Quantidade Referências é o menor, se for, joga pro inicio do array LRUincomplete
    aux.append(lista[i][0])
    aux.append(lista[i][3])
  LRUincomplete.append(aux)#faz a adcao do array local "aux" no array LRUincomplete
LRUincomplete.sort(key=ord)#Ordena o array LRUincomplete com base na Quantidade Referências
for i in range(len(LRUincomplete)):
  LRU.append(LRUincomplete[i][0])
print(f'A sequencia de frames a ser substituidos utilizando LRU será: {LRU}')

return v[1]#Funcao para pegar a Quantidade Referências ou Tempo da última referência, para usar de paramentro para ordenacao no metodo .sort
lista = [[1,12,10,20,1,1],[2,10,1,12,0,0],[3,11,2,21,1,0]]
print(f'Para a lista de frames:\n{lista}')
#FIFO
FIFO = []
for i in range(len(lista)):
  FIFO.append(lista[i][0])
FIFO.sort()
print(f'A sequencia de frames a ser substituidos utilizando FIFO será: {FIFO}')

#LFU
LFUincomplete = []
LFU = []
for i in range(len(lista)):
  aux = []
  aux.append(lista[i][0])
  aux.append(lista[i][2])
  LFUincomplete.append(aux)#faz a adcao do array local "aux" no array LFUincomplete
LFUincomplete.sort(key=ord)#Ordena o array LFUincomplete com base na Quantidade Referências
for i in range(len(LFUincomplete)):
  LFU.append(LFUincomplete[i][0])
print(f'A sequencia de frames a ser substituidos utilizando LFU será: {LFU}')

#LRU
LRUincomplete = []
LRU = []
for i in range(len(lista)):
  aux = []
  aux.append(lista[i][0])
  aux.append(lista[i][3])
  LRUincomplete.append(aux)#faz a adcao do array local "aux" no array LRUincomplete
LRUincomplete.sort(key=ord)#Ordena o array LRUincomplete com base na Quantidade Referências
for i in range(len(LRUincomplete)):
  LRU.append(LRUincomplete[i][0])
print(f'A sequencia de frames a ser substituidos utilizando LRU será: {LRU}')

aux.append(lista[i][2])
  LFUincomplete.append(aux)#faz a adcao do array local "aux" no array LFUincomplete
LFUincomplete.sort(key=ord)#Ordena o array LFUincomplete com base na Quantidade Referências
for i in range(len(LFUincomplete)):
  LFU.append(LFUincomplete[i][0])
print(f'A sequencia de frames a ser substituidos utilizando LFU será: {LFU}')

#LRU
LRUincomplete = []
LRU = []
for i in range(len(lista)):
  aux = []
  aux.append(lista[i][0])
  aux.append(lista[i][3])
  LRUincomplete.append(aux)#faz a adcao do array local "aux" no array LRUincomplete
LRUincomplete.sort(reverse = True, key=ord)#Ordena o array LRUincomplete com base na Quantidade Referências
for i in range(len(LRUincomplete)):
  LRU.append(LRUincomplete[i][0])
print(f'A sequencia de frames a ser substituidos utilizando LRU será: {LRU}')

#NRU
NRUincomplete = []
NRU = []
for i in range(len(lista)):
  aux = []
  aux.append(lista[i][0])
  aux.append(lista[i][4]+lista[i][5])
  NRUincomplete.append(aux)#faz a adcao do array local "aux" no array LRUincomplete
NRUincomplete.sort(key=ord)#Ordena o array LRUincomplete com base na Quantidade Referências
for i in range(len(NRUincomplete)):
  NRU.append(NRUincomplete[i][0])
print(f'A sequencia de frames a ser substituidos utilizando NRU será: {NRU}')
