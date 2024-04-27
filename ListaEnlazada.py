#Definimos la clase Nodo que guardará el dato y el índice hacia el nodo siguiente
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None

#La clase ListaEnlazada maneja la lista enlazada como tal, índices, datos
class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.head is None:
            self.head = nuevo_nodo
            return
        ultimo_nodo = self.head
        while ultimo_nodo.next:
            ultimo_nodo = ultimo_nodo.siguiente
        ultimo_nodo.next = nuevo_nodo

    #Unicamente muestra en pantalla el contenido de la lista
    def imprime_lista(self):
        actual_nodo = self.head
        while actual_nodo:
            print(actual_nodo.dato, end=" -> ")
            actual_nodo = actual_nodo.siguiente
        print("None")

# Crea la lista enlazada con valores definidos por el usuario
def crea_lista_enlazada():
    lista_enlazada = ListaEnlazada()
    n = int(input("Ingresa la cantidad de nodos: "))
    for i in range(n):
        dato = input(f"Ingresa el valor del nodo {i + 1}: ")
        lista_enlazada.agregar(dato)
    return lista_enlazada

# Ejemplo de uso
if __name__ == "__main__":
    lista_enlazada = crea_lista_enlazada()
    lista_enlazada.imprime_lista()