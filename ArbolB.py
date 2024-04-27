class NodoArbol:
    def __init__(self, hoja=True):
        self.hoja = hoja
        self.claves = []
        self.hijos = []


class ArbolB:
    def __init__(self, t):
        self.raiz = NodoArbol()
        self.t = t

    def insertar(self, valor):
        raiz = self.raiz
        if len(raiz.claves) == (2 * self.t) - 1:
            nueva_raiz = NodoArbol(hoja=False)
            nueva_raiz.hijos.append(self.raiz)
            self.dividir_hijo(nueva_raiz, 0)
            self.raiz = nueva_raiz
            self.insertar_no_lleno(nueva_raiz, valor)
        else:
            self.insertar_no_lleno(raiz, valor)

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
        hijo = padre.hijos[indice]
        nuevo_hijo = NodoArbol(hoja=hijo.hoja)
        padre.claves.insert(indice, hijo.claves[t - 1])
        padre.hijos.insert(indice + 1, nuevo_hijo)
        nuevo_hijo.claves = hijo.claves[t: (2 * t) - 1]
        hijo.claves = hijo.claves[:t - 1]
        if not hijo.hoja:
            nuevo_hijo.hijos = hijo.hijos[t:]
            hijo.hijos = hijo.hijos[:t]

    def recorre(self):
        self.recorre_arbol(self.raiz)

    def recorre_arbol(self, nodo):
        if nodo is not None:
            print(nodo.claves)
            if not nodo.hoja:
                for hijo in nodo.hijos:
                    self.recorre_arbol(hijo)


# Ejemplo de uso
if __name__ == "__main__":
    arbolito = ArbolB(3)  # t = 3
    claves = [10, 20, 5, 6, 12, 30, 7, 17]
    for clave in claves:
        arbolito.insertar(clave)
    print('Recorrido del Arbol B: ')
    arbolito.recorre()
