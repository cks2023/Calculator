import tkinter as tk

operator = ""  # Global variable to store the operator string

def delete_from_operator():
    global operator
    operator = operator[:-1]
    entry.delete(0, tk.END)
    entry.insert(tk.END, operator)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_delete = tk.Button(root, text="Delete", padx=69, pady=20, command=delete_from_operator)
button_delete.grid(row=1, column=1)

root.mainloop()
