def BalanceoParentesis(cadena):
    pila = [] #usaremos una lista para guardar los parentesis
    # definimos un diccionario para indicarle el par del parentesis, tambien se podría agregar llaves y corchetes
    pares = {')':'('}

#Se recorre la cadena en busca de los paréntesis
    for caracter in cadena:
        if caracter == '(':
            pila.append(caracter) #si se encuentra un parentesis apertura, se inserta en la lista
        elif caracter == ')':#si es un parentesis de cierre:
            if not pila or pila[-1] != pares[caracter]: #Si no hay elementos en la pila, entonces no está balanceado
                return False
            pila.pop() #Si hay elementos, se elimina uno de la lista
    return not pila #Si la lista queda vacía, la cadena está balanceada


cadena1 = "(1+1)-()"

if BalanceoParentesis(cadena1):
    print('La cadena está balanceada')
else:
    print('La cadena no es balanceada')
