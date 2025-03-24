import json
import time

class GestorPostres:
    def __init__(self, archivo="postres.json"):
        self.archivo = archivo
        self.cargar_datos()

    def cargar_datos(self):
        try:
            with open(self.archivo, "r") as file:
                self.postres = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.postres = {}

    def guardar_datos(self):
        with open(self.archivo, "w") as file:
            json.dump(self.postres, file, indent=4)

    def mostrar_ingredientes(self):
        postre = input("Ingrese el nombre del postre: ")
        if postre in self.postres:
            print(f"Ingredientes de {postre}: {', '.join(self.postres[postre])}")
        else:
            print("El postre no existe.")

    def alta_postre(self):
        postre = input("Ingrese el nombre del nuevo postre: ")
        if postre in self.postres:
            print("El postre ya existe.")
        else:
            ingredientes = input("Ingrese los ingredientes separados por comas: ").split(",")
            self.postres[postre] = list(set([i.strip() for i in ingredientes]))  # Eliminar duplicados
            self.guardar_datos()
            print(f"Postre {postre} agregado con ingredientes: {self.postres[postre]}")

    def baja_postre(self):
        postre = input("Ingrese el nombre del postre a eliminar: ")
        if postre in self.postres:
            del self.postres[postre]
            self.guardar_datos()
            print(f"Postre {postre} eliminado.")
        else:
            print("El postre no existe.")

    def agregar_ingredientes(self):
        postre = input("Ingrese el nombre del postre: ")
        if postre in self.postres:
            nuevos_ingredientes = input("Ingrese los nuevos ingredientes separados por comas: ").split(",")
            self.postres[postre].extend([i.strip() for i in nuevos_ingredientes])
            self.postres[postre] = list(set(self.postres[postre]))  # Eliminar duplicados
            self.guardar_datos()
            print(f"Ingredientes actualizados de {postre}: {self.postres[postre]}")
        else:
            print("El postre no existe.")

    def eliminar_ingrediente(self):
        postre = input("Ingrese el nombre del postre: ")
        if postre in self.postres:
            ingrediente = input("Ingrese el ingrediente a eliminar: ")
            if ingrediente in self.postres[postre]:
                self.postres[postre].remove(ingrediente)
                self.guardar_datos()
                print(f"Ingrediente {ingrediente} eliminado de {postre}.")
            else:
                print("El ingrediente no existe en la lista.")
        else:
            print("El postre no existe.")

    def menu(self):
        while True:
            print("\nMenú de Gestión de Postres")
            print("1. Mostrar ingredientes de un postre")
            print("2. Agregar un nuevo postre")
            print("3. Eliminar un postre")
            print("4. Agregar ingredientes a un postre")
            print("5. Eliminar un ingrediente de un postre")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.mostrar_ingredientes()
            elif opcion == "2":
                self.alta_postre()
            elif opcion == "3":
                self.baja_postre()
            elif opcion == "4":
                self.agregar_ingredientes()
            elif opcion == "5":
                self.eliminar_ingrediente()
            elif opcion == "6":
                print("Saliendo...")
                break
            else:
                print("Opción no válida, intente de nuevo.")
            time.sleep(1)

if __name__ == "__main__":
    gestor = GestorPostres()
    gestor.menu()
