import tkinter as tk
from todo_list import Todo, TodoService
from tkinter import font


class TodoForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # self.place(x=0, y=0)
        self.grid()
        # self.pack()
        self.todo_service = TodoService()
        self.render_form()
        self.todosFrame = self.render_todos


    def render_form(self):
        form = tk.Frame(self)
        form.grid(sticky="W", row=0, column=0)
        # form.place(x=0, y=0)
        # form.pack(side=tk.RIGHT)

        input = tk.Entry(form)
        input.grid(sticky="W", row=0, column=2)
        # input.place(x=0, y=0)
        # input.pack(side=tk.RIGHT)

        btnAdd = tk.Button(form, text="add", width=5, command=lambda: self.add_todo(input))
        btnAdd.grid(sticky="W", row=0, column=0)
        # btnAdd.place(x=100, y=0)
        # btnAdd.pack(side=k.RIGHT)


    @property
    def render_todos(self):
        listFrame = tk.Frame(self)
        # listFrame.place(x=0, y=50)
        listFrame.grid(sticky="W", row=1, column=0)
        y = 80

        for todo in self.todo_service.todos:

            todo_row = tk.Frame(listFrame)
            todo_row.grid(sticky="W", row=(1+self.todo_service.todos.index(todo)), column=0)

            # todo_row.place(x=0, y=y)
            # todo_row.pack()

            lbl = tk.Label(todo_row, text=todo.description, font="Tahoma 10", bg="yellow", fg="red")
            lbl.grid(sticky="W", row=(1+self.todo_service.todos.index(todo)), column=2)
            # lbl.place(x=0, y=y)
            # lbl.pack(side=tk.LEFT)

            btnRemove = tk.Button(todo_row, text="Удалить", command=lambda todo=todo: self.remove_todo(todo))
            btnRemove.grid(row=(1+self.todo_service.todos.index(todo)), column=1)
            # btnRemove.place(x=100, y=y)
            # btnRemove.pack(side=tk.LEFT)
            y += 40


        return listFrame


    def add_todo(self, input):
        self.todo_service.add_todo(Todo(input.get()))
        input.delete(0, len(input.get()))

        self.todosFrame.destroy()
        self.todosFrame = self.render_todos

    def remove_todo(self, todo):
        self.todo_service.remove_todo(todo)

        self.todosFrame.destroy()
        self.todosFrame = self.render_todos

