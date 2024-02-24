# Se define la clase nodo para el árbol
class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


# Acá se manejarán los métodos del árbol
class ArbolBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz

    # Inserta un dato en un nodo
    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            self._insertar_recursivo(dato, self.raiz)

    # Se crea la referencia a los hijos izquierdo y derecho del nodo
    def _insertar_recursivo(self, dato, nodo_actual):
        if dato < nodo_actual.dato:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = NodoArbol(dato)
            else:
                self._insertar_recursivo(dato, nodo_actual.izquierda)
        elif dato > nodo_actual.dato:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = NodoArbol(dato)
            else:
                self._insertar_recursivo(dato, nodo_actual.derecha)
        else:

            pass

    # Muestra el recorrido inorden del árbol
    def inorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo.izquierda:
            self.inorden(nodo.izquierda)
        print(nodo.dato, end=" ")
        if nodo.derecha:
            self.inorden(nodo.derecha)


# Ejemplo de uso
if __name__ == "__main__":
    arbol = ArbolBinario()
    arbol.insertar(5)
    arbol.insertar(3)
    arbol.insertar(7)
    arbol.insertar(2)
    arbol.insertar(4)
    arbol.insertar(6)
    arbol.insertar(8)

    print("Recorrido Inorden:")
    arbol.inorden()
