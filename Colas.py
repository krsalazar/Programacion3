#Creamos la clase Cola
class Cola:
    def __init__(self):
        self.items = []

#Verifica que la cola no esté vacía
    def esta_vacia(self):
        return len(self.items) == 0

#Metodo para agregar elementos a la cola
    def agregar(self, elemento):
        self.items.append(elemento)

#Metodo para quitar elementos de la cola
    def quitar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía")

#Muestra el primer elemento que se agregó a la cola
    def ver_frente(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            return None

#Muestra el tamaño de la cola
    def tamano(self):
        return len(self.items)

# Ejemplo de uso
if __name__ == "__main__":
    cola = Cola()
    cola.agregar(8)
    cola.agregar(66)
    cola.agregar(44)
    print("Tamaño de la cola: ", cola.tamano())
    print("Frente de la cola: ", cola.ver_frente())
    print("Quitando elementos de la cola: ")
    while not cola.esta_vacia():
        print(cola.quitar())
