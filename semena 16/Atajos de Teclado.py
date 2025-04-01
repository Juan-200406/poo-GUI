import tkinter as tk
from tkinter import messagebox

def main():
    """Función principal para inicializar y ejecutar la aplicación."""

    def agregar_tarea():
        """Agrega una nueva tarea a la lista."""
        tarea = entrada_tarea.get()
        if tarea:
            lista_tareas.insert(tk.END, tarea)
            entrada_tarea.delete(0, tk.END)  # Limpia el campo de entrada

    def marcar_completada():
        """Marca la tarea seleccionada como completada."""
        seleccion = lista_tareas.curselection()
        if seleccion:
            tarea = lista_tareas.get(seleccion[0])
            lista_tareas.delete(seleccion[0])
            lista_tareas.insert(seleccion[0], "✅ " + tarea)  # Añade un emoji para indicar completado
            lista_tareas.itemconfig(seleccion[0], fg="gray")  # Cambia el color del texto a gris

    def eliminar_tarea():
        """Elimina la tarea seleccionada."""
        seleccion = lista_tareas.curselection()
        if seleccion:
            lista_tareas.delete(seleccion[0])

    def cerrar_aplicacion(event=None):
        """Cierra la aplicación."""
        if messagebox.askokcancel("Cerrar", "¿Seguro que quieres salir?"):
            ventana.destroy()

    ventana = tk.Tk()
    ventana.title("Gestor de Tareas")
    ventana.geometry("500x600")
    # Campo de entrada y botones
    entrada_tarea = tk.Entry(ventana, width=50)
    entrada_tarea.pack(pady=10)

    frame_botones = tk.Frame(ventana)
    frame_botones.pack()

    boton_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_tarea)
    boton_agregar.pack(side=tk.LEFT)

    boton_completar = tk.Button(frame_botones, text="Completar", command=marcar_completada)
    boton_completar.pack(side=tk.LEFT)

    boton_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar_tarea)
    boton_eliminar.pack(side=tk.LEFT)
    # Lista de tareas
    lista_tareas = tk.Listbox(ventana, width=50)
    lista_tareas.pack(pady=10)

    # Atajos de teclado
    ventana.bind("<Return>", lambda event=None: agregar_tarea())  # Añadir con Enter
    ventana.bind("<c>", lambda event=None: marcar_completada())  # Completar con 'c'
    ventana.bind("<Delete>", lambda event=None: eliminar_tarea())  # Eliminar con Delete
    ventana.bind("<d>", lambda event=None: eliminar_tarea())  # Eliminar con 'd'
    ventana.bind("<Escape>", cerrar_aplicacion)  # Cerrar con Escape

    ventana.mainloop()

if __name__ == "__main__":
    main()