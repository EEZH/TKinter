import tkinter as tk
from todo_list import Todo, TodoService


class TodoForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.todo_service = TodoService()
        self.render_form()
        self.todosFrame = self.render_todos

    @property
    def render_todos(self):
        listFrame = tk.Frame(self)
        listFrame.pack()
        id = 0

        for todo in self.todo_service.todos:

            todo_row = tk.Frame(listFrame)
            todo_row.pack()

            lbl = tk.Label(todo_row, text=todo.description)
            lbl.pack(side=tk.LEFT)

            btnRemove = tk.Button(todo_row, text="Удалить", command=lambda todo=todo: self.remove_todo(todo))
            btnRemove.pack(side=tk.LEFT)
            id += 1

        return listFrame


    def render_form(self):
        form = tk.Frame(self)
        form.pack()

        input = tk.Entry(form)
        input.pack(side=tk.LEFT)

        btnAdd = tk.Button(form, text="add", command=lambda: self.add_todo(input))
        btnAdd.pack(side=tk.LEFT)

    def add_todo(self, input):
        self.todo_service.add_todo(Todo(input.get()))
        input.delete(0, len(input.get()))

        self.todosFrame.destroy()
        self.todosFrame = self.render_todos

    def remove_todo(self, todo):
        self.todo_service.remove_todo(todo)

        self.todosFrame.destroy()
        self.todosFrame = self.render_todos

