import tkinter as tk

clicks_count = 0

root = tk.Tk() #главное окно
root.title("My app")
root.geometry("720x400")

lbl = tk.Label(root, text=clicks_count)
lbl.place(x=30, y=50)
# lbl["text"] = "next example"

def click_up():
    global clicks_count
    global lbl
    clicks_count += 1
    lbl["text"] = clicks_count

def click_down():
    global clicks_count
    global lbl
    clicks_count -= 1
    lbl["text"] = clicks_count

def click_common(is_up=True):
    global clicks_count
    global lbl
    clicks_count = clicks_count + 1 if is_up else clicks_count - 1
    lbl["text"] = clicks_count

btn_up = tk.Button(root, text="Up", command=lambda : click_common())
btn_up.place(x=0, y=70)
# btn_up.pack()

btn_down = tk.Button(root, text="Down", command=lambda :click_common(is_up=False))
btn_down.place(x=0, y=90)
# btn_down.pack()

input = tk.Entry(root)
input.place(x=20, y=0)

btn_get_input = tk.Button(root, text="Get input")
btn_get_input.place(x=50, y=30)

def  get_input():
    btn_get_input["text"] = input.get()
    input.delete(0, len(input.get()))

btn_get_input["command"] = get_input

# check = tk.Checkbutton(root,
#                        text="check",
#                        onvalue=lambda :print(1),
#                        ofvalue=lambda :print(0))
# check.pack(side=tk.BOTTOM)



#--- examples ---
# btn_first.place(x=50, y=50)
#
# btn_second = tk.Button(root, text="Click me")
# # btn_second.pack(side=tk.TOP)
# btn_second.grid(row=1, column=1)
#
# btn_third = tk.Button(root, text="Simple button")
# btn_third.grid(row=0, column=0)

# --- Example Lambda ---
# l = lambda x: print(x)
# l(1000000000)

# def test(test1):
#     test1()
#
# test(lambda :print(10))


root.mainloop()
