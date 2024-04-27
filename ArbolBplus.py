class NodoArbol:
    def __init__(self, hoja=True):
        self.hoja = hoja
        self.claves = []
        self.hijos = []
        self.siguiente = None


class ArbolBPlus:
    def __init__(self, t):
        self.raiz = NodoArbol()
        self.t = t

    def insert(self, value):
        raiz = self.raiz
        if len(raiz.claves) == (2 * self.t) - 1:
            nueva_raiz = NodoArbol(hoja=False)
            nueva_raiz.hijos.append(self.raiz)
            self.dividir_hijo(nueva_raiz, 0)
            self.raiz = nueva_raiz
            self.insertar_no_lleno(nueva_raiz, value)
        else:
            self.insertar_no_lleno(raiz, value)

    def insertar_no_lleno(self, nodo, valor):
        i = len(nodo.claves) - 1
        if nodo.hoja:
            nodo.claves.append(None)
            while i >= 0 and valor < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1
            nodo.claves[i + 1] = valor
        else:
            while i >= 0 and valor < nodo.claves[i]:
                i -= 1
            i += 1
            if len(nodo.hijos[i].claves) == (2 * self.t) - 1:
                self.dividir_hijo(nodo, i)
                if valor > nodo.claves[i]:
                    i += 1
            self.insertar_no_lleno(nodo.hijos[i], valor)

    def dividir_hijo(self, padre, indice):
        t = self.t
        hijos = padre.hijos[indice]
        nuevo_hijo = NodoArbol(hoja=hijos.hoja)
        padre.claves.insert(indice, hijos.claves[t - 1])
        padre.hijos.insert(indice + 1, nuevo_hijo)
        nuevo_hijo.claves = hijos.claves[t: (2 * t) - 1]
        hijos.claves = hijos.claves[:t - 1]
        if not hijos.hoja:
            nuevo_hijo.hijos = hijos.hijos[t:]
            hijos.hijos = hijos.hijos[:t]

    def buscar(self, valor):
        return self.buscar_arbol(self.raiz, valor)

    def buscar_arbol(self, nodo, valor):
        i = 0
        while i < len(nodo.claves) and valor > nodo.claves[i]:
            i += 1
        if i < len(nodo.claves) and valor == nodo.claves[i]:
            return True
        elif nodo.hoja:
            return False
        else:
            return self.buscar_arbol(nodo.hijos[i], valor)

    def recorrer(self):
        self.recorre_arbol(self.raiz)

    def recorre_arbol(self, nodo):
        if nodo is not None:
            if nodo.hoja:
                print(nodo.claves)
            else:
                for i in range(len(nodo.claves)):
                    self.recorre_arbol(nodo.hijos[i])
                    if i < len(nodo.claves):
                        print(nodo.claves[i])


# Ejemplo de uso
if __name__ == "__main__":
    arbolito = ArbolBPlus(3)  # t = 3
    claves = [10, 20, 5, 6, 12, 30, 7, 17]
    for key in claves:
        arbolito.insert(key)
    print('Recorrido del arbol B+ ')
    arbolito.recorrer()