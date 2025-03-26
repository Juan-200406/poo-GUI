import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Lista de Tareas")

        self.tareas = []  # Lista para almacenar las tareas
        self.tareas_completadas = [] # Lista para almacenar las tareas completadas

        # Campo de entrada para nuevas tareas
        self.entrada_tarea = tk.Entry(ventana, width=40)
        self.entrada_tarea.grid(row=0, column=0, padx=10, pady=10)

        # Botones
        self.boton_agregar = tk.Button(ventana, text="Añadir Tarea", command=self.agregar_tarea)
        self.boton_agregar.grid(row=0, column=1, padx=5, pady=10)

        self.boton_completar = tk.Button(ventana, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completar.grid(row=1, column=1, padx=5, pady=10)

        self.boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=2, column=1, padx=5, pady=10)

        # Lista de tareas
        self.lista_tareas = tk.Listbox(ventana, width=50)
        self.lista_tareas.grid(row=1, column=0, rowspan=3, padx=10, pady=10)

        # Vinculación de eventos
        self.entrada_tarea.bind("<Return>", lambda event: self.agregar_tarea())  # Añadir tarea con Enter
        self.lista_tareas.bind("<Double-Button-1>", lambda event: self.marcar_completada()) # Marcar con doble click

        self.actualizar_lista()

    def agregar_tarea(self):
        tarea = self.entrada_tarea.get()
        if tarea:
            self.tareas.append(tarea)
            self.entrada_tarea.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def marcar_completada(self):
        try:
            indice_seleccionado = self.lista_tareas.curselection()[0]
            tarea_completada = self.tareas.pop(indice_seleccionado)
            self.tareas_completadas.append(tarea_completada)
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def eliminar_tarea(self):
        try:
            indice_seleccionado = self.lista_tareas.curselection()[0]
            del self.tareas[indice_seleccionado]
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            self.lista_tareas.insert(tk.END, tarea)
        for tarea in self.tareas_completadas:
            self.lista_tareas.insert(tk.END, str(tarea) + " (Completada)")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = ListaTareasApp(ventana)
    ventana.mainloop()