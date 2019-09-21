import tkinter as tk
from todo_form import TodoForm

root = tk.Tk()
root.geometry("400x600")
root.title("Todo List")

todoForm = TodoForm(root)

todoForm.mainloop()