#Questão 1. Implemente um método comprimento que tenha como valor de retorno 
#o comprimento de uma lista encadeada, isto é, que calcule o número de nós de uma lista.

class NodoLista:
    """Esta classe representa um nodo de uma lista encadeada."""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class ListaEncadeada1:
    """Esta classe representa uma lista encadeada."""
    def __init__(self):
        self.cabeca = None
        self._size = 0

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def insere_no_inicio(self, novo_dado):
        novo_nodo = NodoLista(novo_dado)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo
        self._size = self._size + 1

    def __len__(self):
        return self._size


lista = ListaEncadeada1()
print("Lista vazia:", lista)
print("Tamanho da lista: ", lista._size)

lista.insere_no_inicio(5)
print("Lista contém um único elemento:", lista)
print("Tamanho da lista: ", lista._size)

lista.insere_no_inicio(10)
print("Inserindo um novo elemento:", lista)
print("Tamanho da lista: ", lista._size)

lista.insere_no_inicio(25)
print("Inserindo um novo elemento:", lista)
print("Tamanho da lista: ", lista._size)


