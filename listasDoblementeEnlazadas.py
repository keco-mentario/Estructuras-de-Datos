class Node:
    def __init__(self, contenido):
        self.data = contenido
        self.siguiente = None
        self.anterior = None


class ListaDoblementeEnlazada:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamaño = 0

    def insertarAlInicio(self, contenido):
        nuevoNodo = Node(contenido)
        if self.head is None:
            self.head = nuevoNodo
            self.tail = nuevoNodo
        else:
            nuevoNodo.siguiente = self.head
            self.head.anterior = nuevoNodo
            self.head = nuevoNodo
        self.tamaño += 1

    def insertarAlMedio(self, contenido, posicion): #clase
        #Verificar posicion válida
        if posicion < 0 or posicion > self.tamaño:
            print("Posición inválida.")
            return

        #Si la posición es 0, insertar al inicio
        if posicion == 0:
            self.insertarAlInicio(contenido)
            return

        #Si la posición corresponde al final, insertar al final
        if posicion == self.tamaño:
            self.insertarAlFinal(contenido)
            return

        nuevo_nodo = Node(contenido)
        actual = self.head

        #Llegar al nodo que actualmente ocupa la posicion
        for i in range(posicion):
            actual = actual.siguiente

        #Conectar el nuevo nodo
        anterior = actual.anterior

        nuevo_nodo.anterior = anterior
        nuevo_nodo.siguiente = actual

        anterior.siguiente = nuevo_nodo
        actual.anterior = nuevo_nodo

        self.tamaño += 1 

    def insertarAlFinal(self, contenido):
        nuevo_nodo = Node(contenido)
        if self.esta_vacia():
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.tail
            self.tail = nuevo_nodo
        self.tamaño += 1

    def display(self):
        actual = self.head
        while actual is not None:
            print(actual.data, end=" <-> ")
            actual = actual.siguiente
        print("None")

    def eliminarEnPosicion(self, posicion):
        if self.head is None:
            print("La lista está vacía.")
            return

        if posicion == 0:
            self.eliminarAlInicio()
            return

        actual = self.head
        contador = 0

        while actual is not None and contador < posicion:
            actual = actual.siguiente
            contador += 1

        if actual is None:
            print("Posición fuera de rango.")
            return

        if actual.anterior is None:
            self.eliminarAlInicio()
        elif actual.siguiente is None:
            self.eliminarAlFinal()
        else:
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            self.tamaño -= 1

    def eliminarAlInicio(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return

        if self.head.siguiente is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.siguiente
            self.head.anterior = None
        self.tamaño -= 1

    def eliminarAlFinal(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return

        if self.tail.anterior is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.anterior
            self.tail.siguiente = None
        self.tamaño -= 1

    def buscar(self, elemento):
        actual = self.head
        while actual is not None:
            if actual.data == elemento:
                return True
            actual = actual.siguiente
        return False

    def esta_vacia(self):
        return self.head is None

    def sustituir(self, posicion, nuevo_contenido):
        if posicion < 0 or posicion >= self.tamaño:
            print("Posición inválida.")
            return

        actual = self.head
        for _ in range(posicion):
            actual = actual.siguiente

        actual.data = nuevo_contenido

    def ordenarAlfabeticamente(self):
        if self.esta_vacia():
            print("La lista está vacía.")
            return

        actual = self.head
        while actual is not None:
            siguiente = actual.siguiente
            while siguiente is not None:
                if str(actual.data).casefold() > str(siguiente.data).casefold():
                    actual.data, siguiente.data = siguiente.data, actual.data
                siguiente = siguiente.siguiente
            actual = actual.siguiente

    def imprimirAdelante(self):
        self.display()

    def cantidadElementos(self):
        return self.tamaño

    def contarOcurrencias(self, elemento):
        actual = self.head
        contador = 0
        while actual is not None:
            if actual.data == elemento:
                contador += 1
            actual = actual.siguiente
        return contador

    def obtenerPosicion(self, elemento):
        actual = self.head
        posicion = 0
        while actual is not None:
            if actual.data == elemento:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1  # Elemento no encontrado

if __name__ == "__main__":
    lista = ListaDoblementeEnlazada()
    try:
        with open("datos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea != "":
                    lista.insertarAlFinal(linea)

        lista.ordenarAlfabeticamente()
        lista.imprimirAdelante()

        with open("Reporte.txt", "w", encoding="utf-8") as archivo:
            archivo.write("====================================\n")
            archivo.write("    REPORTE DE NOMBRES\n")
            archivo.write("====================================\n\n")
            archivo.write(
                "Cantidad de elementos: "
                + str(lista.cantidadElementos())
                + "\n\n"
            )

            archivo.write("Digite una palabra para buscar: Luis Diego\n")
            posicion = lista.obtenerPosicion("Luis Diego")
            archivo.write("La palabra está en la posición: " + str(posicion) + "\n")
            ocurrencias = lista.contarOcurrencias("Luis Diego")
            archivo.write(f"La palabra aparece " + str(ocurrencias) + " veces en la lista. \n\n")

            archivo.write("Lista ordenada alfabeticamente:\n")

            actual = lista.head
            while actual is not None:
                archivo.write(str(actual.data) + "\n")
                actual = actual.siguiente

    except FileNotFoundError:
        print("Error: el archivo datos.txt no existe.")
        exit()


