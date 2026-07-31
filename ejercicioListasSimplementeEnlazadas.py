class Node:
  def __init__(self, contenido):
    self.data = contenido
    self.next = None #None = null

class ListaSimplementeEnlazada:
  def __init__(self):
    self.head = None

  def insertarAlInicio(self, contenido):
    nuevoNodo = Node(contenido) #Genera el nodo con el dato
    if self.head is None: # Si la lista está vacía
      self.head = nuevoNodo
    else:
      nuevoNodo.next = self.head
      self.head = nuevoNodo

  def insertarAlMedio(self, contenido):
    nuevoNodo = Node(contenido) #Genera el nodo con el dato
    if self.head is None: # Si la lista está vacía
      self.head = nuevoNodo
    else:
      print("Digite la posición a insertar el elemento: ")
      posicion = int(input())
      actual = self.head
      for i in range(posicion-2):
        actual = actual.next
      nuevoNodo.next = actual.next
      actual.next = nuevoNodo


  def insertarAlFinal(self, contenido):
    nuevoNodo = Node(contenido) #Genera el nodo con el dato
    if self.head is None: # Si la lista está vacía
      self.head = nuevoNodo
    else:
      actual = self.head
      while actual.next is not None:
        actual = actual.next
      actual.next = nuevoNodo

  def display(self):
    actual = self.head
    while actual is not None:
      print(actual.data, end=" -> ")
      actual = actual.next
    print(None)

  def eliminarEnPosicion(self, posicion):
    # Lista vacía
    if self.head is None:
        print("La lista está vacía.")
        return
    # Eliminar el primer nodo
    if posicion == 0:
        self.head = self.head.next
        return
    actual = self.head
    contador = 0
    # Buscar el nodo anterior a la posición
    while actual.next is not None and contador < posicion - 1:
        actual = actual.next
        contador += 1
    # Verificar si la posición existe
    if actual.next is None:
        print("Posición fuera de rango.")
        return
    # Saltar el nodo que se desea eliminar
    actual.next = actual.next.next

  def eliminarAlInicio(self):
    # Verificar si la lista está vacía
    if self.head is None:
        print("La lista está vacía.")
        return
    # Si no está vacía, eliminamos el nodo 1
    self.head = self.head.next

  def eliminarAlFinal(self):
    if self.head is None:
        print("La lista está vacía.")
        return

    if self.head.next is None:
        self.head = None
        return

    actual = self.head

    while actual.next.next is not None:
        actual = actual.next

    actual.next = None

  def buscar(self, elemento):
    actual = self.head
    while actual is not None:
        if actual.data == elemento:
            return True
        actual = actual.next
    return False

  def estaVacia(self):
    return self.head is None



lista1 = ListaSimplementeEnlazada()

while True:
    #clear screen
    #print("\033[H\033[J")  # ANSI escape code to clear the screen

    #Menu de opciones
    print("Menu de opciones:")
    print("1. Insertar al inicio")
    print("2. Insertar al final")
    print("3. Insertar al medio")
    print("4. Eliminar en posición")
    print("5. Eliminar al inicio")
    print("6. Eliminar al final")
    print("7. Buscar elemento")
    print("8. Esta la lista vacia?")
    print("9. Mostrar lista")
    print("0. Salir")
    
    print("Seleccione una opción: ")
    opcion = int(input())
    if opcion == 1:
        print("Digite el elemento a insertar al inicio: ")
        elemento = int(input())
        lista1.insertarAlInicio(elemento)
    elif opcion == 2:
        print("Digite el elemento a insertar al final: ")
        elemento = int(input())
        lista1.insertarAlFinal(elemento)
    elif opcion == 3:
        print("Digite el elemento a insertar al medio: ")
        elemento = int(input())
        lista1.insertarAlMedio(elemento)
    elif opcion == 4:
        print("Digite la posición a eliminar: ")
        posicion = int(input())
        lista1.eliminarEnPosicion(posicion)
    elif opcion == 5:
        lista1.eliminarAlInicio()
    elif opcion == 6:
        lista1.eliminarAlFinal()
    elif opcion == 7:
        print("Elemento a buscar: ")
        elemento = int(input())
        if lista1.buscar(elemento):
            print("Elemento encontrado.")
        else:
            print("Elemento no encontrado.")
    elif opcion == 8:
        if lista1.estaVacia():
            print("La lista está vacía.")
        else:
            print("La lista no está vacía.")
    elif opcion == 9:
        lista1.display()
    elif opcion == 0:
        break
    else:
        print("Opción no válida.")