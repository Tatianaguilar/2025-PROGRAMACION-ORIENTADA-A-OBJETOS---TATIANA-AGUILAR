import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.tasks = []

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.focus()

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Atajos de teclado
        root.bind('<Return>', lambda event: self.add_task())
        root.bind('<c>', lambda event: self.mark_completed())
        root.bind('<d>', lambda event: self.delete_task())
        root.bind('<Delete>', lambda event: self.delete_task())
        root.bind('<Escape>', lambda event: root.quit())

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append({"text": task, "completed": False})
            self.update_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor, escribe una tarea.")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            idx = selected_index[0]
            self.tasks[idx]["completed"] = not self.tasks[idx]["completed"]
            self.update_task_list()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            idx = selected_index[0]
            del self.tasks[idx]
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            text = task["text"]
            if task["completed"]:
                text = f"✔ {text}"
            self.task_listbox.insert(tk.END, text)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()