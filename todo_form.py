import tkinter as tk
from todo_list import Todo, TodoService


class TodoForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.todo_service = TodoService()
        self.render_form()
        self.todosFrame = self.render_todos()


    def render_todos(self):
        listFrame = tk.Frame(self)
        listFrame.pack()

        for todo in self.todo_service.todos:
            todo_row = tk.Frame(listFrame)
            todo_row.pack()

            lbl = tk.Label(todo_row, text=todo.description)
            lbl.pack(side=tk.RIGHT)

            btnRemove = tk.Button(todo_row, text="Удалить")
            btnRemove.pack(side=tk.RIGHT)

        return listFrame



    def render_form(self):
        form = tk.Frame(self)
        form.pack()

        input = tk.Entry(form)
        input.pack(side=tk.RIGHT)

        btnAdd = tk.Button(form, text="add", command=lambda :self.add_todo(input))
        btnAdd.pack(side=tk.RIGHT)

    def add_todo(self, input):
        self.todo_service.add_todo(Todo(input.get()))
        input.delete(0, len(input.get()))

        self.todosFrame.destroy()
        self.todosFrame = self.render_todos()

