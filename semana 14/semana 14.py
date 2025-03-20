import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import datetime

class Agenda:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Eventos")

        # Lista de eventos (TreeView)
        self.tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(pady=10)

        # Frame para la entrada de datos
        input_frame = ttk.Frame(root)
        input_frame.pack(pady=10)

        # Campos de entrada
        ttk.Label(input_frame, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = ttk.Entry(input_frame)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Hora (HH:MM):").grid(row=1, column=0, padx=5, pady=5)
        self.hora_entry = ttk.Entry(input_frame)
        self.hora_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.descripcion_entry = ttk.Entry(input_frame)
        self.descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botones
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

        self.eventos = []  # Lista para almacenar eventos

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        try:
            datetime.datetime.strptime(fecha, "%Y-%m-%d")
            datetime.datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha u hora incorrecto.")
            return

        self.eventos.append((fecha, hora, descripcion))
        self.tree.insert("", tk.END, values=(fecha, hora, descripcion))

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            return

        respuesta = messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?")
        if respuesta:
            item = seleccion[0]
            index = self.tree.index(item)
            del self.eventos[index]
            self.tree.delete(item)

# Iniciar el bucle principal de la aplicaci
if __name__ == "__main__":
    root = tk.Tk()
    app = Agenda(root)
    root.mainloop()
