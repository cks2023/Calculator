from tkinter import *
import tkinter as tk

operator = ""  # Global variable to store the operator string

def btnClick(number):
    global operator
    operator=operator+str(number)
    text_Input.set(operator)

def delete_from_operator(entry_widget):
    global operator
    operator = operator[:-1]
    entry_widget.delete(0, tk.END)
    entry_widget.insert(tk.END, operator)

root = tk.Tk()
root.title("Calculator")
text_Input=tk.StringVar()

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

b7=Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="7",bg="powder blue",command = lambda:btnClick(7)).grid(row=1,column=0)

b8=Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="8",bg="powder blue",command = lambda:btnClick(8)).grid(row=1,column=1)

b9=Button(root,padx=16,pady=16,bd=8,fg="black",font=("arial",20,"bold"),text="9",bg="powder blue",command = lambda:btnClick(9)).grid(row=1,column=2)


button_delete = tk.Button(root, text="Delete", padx=69, pady=20, command=lambda: delete_from_operator(entry))
button_delete.grid(row=1, column=1)

root.mainloop()