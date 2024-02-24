#Creamos la clase Pila
class Pila:
    def __init__(self):
        self.items = []

#Verificamos si la pila está vacía
    def esta_vacia(self):
        return len(self.items) == 0

#Agrega elementos a la pila
    def apilar(self, elemento):
        self.items.append(elemento)

#Elimina elementos de la pila
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")

#Muestra el elemento que está hasta arriba de la pila
    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

    def tamano(self):
        return len(self.items)

# Ejemplo cómo usar la pila

if __name__ == "__main__":
    pila = Pila()
    pila.apilar(9)
    pila.apilar(60)
    pila.apilar(88)
    print("Tope de la pila:", pila.ver_tope())
    print("Tamaño de la pila: ", pila.tamano())
    print("Desapilando elementos:")
    while not pila.esta_vacia():
        print(pila.desapilar())
