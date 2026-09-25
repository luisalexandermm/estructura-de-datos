class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.activo = None
    def agregar(self, nombre):
        nuevo = Nodo(nombre)
        if self.activo is None:
            nuevo.siguiente = nuevo
            self.activo = nuevo
        else:
            actual = self.activo
            while actual.siguiente != self.activo:
                actual = actual.siguiente

            nuevo.siguiente = self.activo
            actual.siguiente = nuevo
    def consultar_activo(self):
        if self.activo is None:
            print("No hay procesos activos")
        else:
            print("Proceso activo:", self.activo.nombre)
    def avanzar(self):
        if self.activo is None:
            print("No hay procesos para avanzar")
        else:
            self.activo = self.activo.siguiente
            print("Ahora el proceso activo es:", self.activo.nombre)
    def retirar_activo(self):
        if self.activo is None:
            print("No hay procesos para retirar")
            return
        nombre_retirado = self.activo.nombre
        if self.activo.siguiente == self.activo:
            self.activo = None
            print("Proceso retirado:", nombre_retirado)
            return
        anterior = self.activo
        while anterior.siguiente != self.activo:
            anterior = anterior.siguiente
        siguiente = self.activo.siguiente
        anterior.siguiente = siguiente
        self.activo = siguiente
        print("Proceso retirado:", nombre_retirado)
        print("Nuevo proceso activo:", self.activo.nombre)

    def mostrar_vuelta(self):
        if self.activo is None:
            print("No hay procesos")
            return
        actual = self.activo
        print("Vuelta completa:")
        while True:
            print(actual.nombre)
            actual = actual.siguiente
            if actual == self.activo:
                break
def main():
    procesos = ListaCircular()
    procesos.agregar("P1")
    procesos.agregar("P2")
    procesos.agregar("P3")
    procesos.agregar("P4")
    procesos.agregar("P5")
    print("ESTADO INICIAL")
    procesos.consultar_activo()
    procesos.mostrar_vuelta()
    print()
    print("PRIMERA VUELTA")
    for i in range(5):
        procesos.consultar_activo()
        procesos.avanzar()
    print()
    print("SEGUNDA VUELTA")
    for i in range(5):
        procesos.consultar_activo()
        procesos.avanzar()
    print()
    print("RETIRAR PROCESO ACTIVO")
    procesos.retirar_activo()
    procesos.mostrar_vuelta()
    print()
    print("AGREGAR PROCESO DURANTE LA EJECUCION")
    procesos.agregar("P6")
    procesos.mostrar_vuelta()
    print()
    print("AVANZAR DESPUES DE AGREGAR P6")
    procesos.avanzar()
    procesos.consultar_activo()

main()

