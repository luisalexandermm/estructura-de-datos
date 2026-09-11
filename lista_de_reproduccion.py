# Lista de reproduccion musical
# Clase para crear cada nodo de la lista
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
# Clase donde voy a manejar la lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.inicio = None
    # Agregar una cancion al principio
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.inicio
        self.inicio = nuevo
        print("La cancion se agrego al inicio.")
    # Agregar una cancion al final
    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        if self.inicio is None:
            self.inicio = nuevo
            print("La cancion se agrego al final.")
            return
        actual = self.inicio
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo
        print("La cancion se agrego al final.")
    # Agregar una cancion en una posicion
    def insertar_posicion(self, dato, posicion):
        if posicion < 1:
            print("Esa posicion no es valida.")
            return
        nuevo = Nodo(dato)
        # Si la posicion es 1, queda de primera
        if posicion == 1:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
            print("La cancion se agrego correctamente.")
            return
        actual = self.inicio
        contador = 1
        while actual is not None and contador < posicion - 1:
            actual = actual.siguiente
            contador += 1
        if actual is None:
            print("Esa posicion no existe.")
            return
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo
        print("La cancion se agrego correctamente.")
    # Eliminar una cancion buscando su nombre
    def eliminar(self, dato):
        if self.inicio is None:
            print("No hay canciones para eliminar.")
            return
        # Revisar si la cancion es la primera
        if self.inicio.dato == dato:
            self.inicio = self.inicio.siguiente
            print("La cancion fue eliminada.")
            return
        actual = self.inicio
        while actual.siguiente is not None:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                print("La cancion fue eliminada.")
                return
            actual = actual.siguiente
        print("No encontre esa cancion en la lista.")
    # Buscar una cancion
    def buscar(self, dato):
        actual = self.inicio
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False
    # Mostrar todas las canciones
    def mostrar(self):
        if self.inicio is None:
            print("Todavia no hay canciones en la lista.")
            return
        actual = self.inicio
        posicion = 1
        print("--- Mi lista de canciones ---")
        while actual is not None:
            print(posicion, "-", actual.dato)
            actual = actual.siguiente
            posicion += 1
        print("-----------------------------")
    # Contar cuantas canciones hay
    def contar(self):
        contador = 0
        actual = self.inicio
        while actual is not None:
            contador += 1
            actual = actual.siguiente

        return contador
    # Revisar si la lista esta vacia
    def esta_vacia(self):
        if self.inicio is None:
            return True
        else:
            return False
# Aqui creo la lista que voy a utilizar
lista = ListaEnlazada()
while True:
    print(" MI LISTA DE CANCIONES")

    print("1. Agregar cancion al inicio")
    print("2. Agregar cancion al final")
    print("3. Agregar cancion en una posicion")
    print("4. Eliminar una cancion")
    print("5. Buscar una cancion")
    print("6. Mostrar mi lista")
    print("7. Contar canciones")
    print("8. Revisar si esta vacia")
    print("9. Salir")
    print()
    opcion = input("Escoja una opcion: ")
    if opcion == "1":
        cancion = input("Escriba el nombre de la cancion: ")
    elif opcion == "2":
        cancion = input("Escriba el nombre de la cancion: ")
        lista.insertar_final(cancion)
    elif opcion == "3":
        cancion = input("Escriba el nombre de la cancion: ")
        posicion = int(input("En que posicion la quiere poner: "))
        lista.insertar_posicion(cancion, posicion)
    elif opcion == "4":
        cancion = input("Escriba la cancion que quiere eliminar: ")
        lista.eliminar(cancion)
    elif opcion == "5":
        cancion = input("Escriba la cancion que quiere buscar: ")
        if lista.buscar(cancion):
            print("Si, esa cancion esta en la lista.")
        else:
            print("No, esa cancion no esta en la lista.")
    elif opcion == "6":
        lista.mostrar()
    elif opcion == "7":
        cantidad = lista.contar()
        print("En este momento hay", cantidad, "canciones.")
    elif opcion == "8":
        if lista.esta_vacia():
            print("La lista esta vacia.")
        else:
            print("La lista tiene canciones.")
    elif opcion == "9":
        print("Bueno, nos vemos. Programa terminado.")
        break
    else:
        print("Esa opcion no esta en el menu. Intente otra vez.")
