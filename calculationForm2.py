# Project Python Calculator form 2
import tkinter as tk

# Create a new Tkinter window
window = tk.Tk()
# title of the window:
window.title("Calculator Form 2")
# set the size of the window
window.geometry("400x200")
# Create the inputs 
num1_label = tk.Label(window, text="Enter first number:")
num1_entry = tk.Entry(window)
operator_label = tk.Label(window, text="Select operator:")
operator = tk.StringVar(window)
operator.set("+")
operator_dropdown = tk.OptionMenu(window, operator, "+", "-", "*", "/")
num2_label = tk.Label(window, text="Enter second number:")
num2_entry = tk.Entry(window)
result_label = tk.Label(window, text="Result:")
result_entry = tk.Entry(window, state="readonly")

# Define the functions
def calculate():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    op = operator.get()
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    result_entry.configure(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, result)
    result_entry.configure(state="readonly")
# create method for clear result:
def clear():
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    result_entry.configure(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.configure(state="readonly")
# add the inputs and the option of the calculation:
num1_label.grid(row=0, column=0)
num1_entry.grid(row=0, column=1)
operator_label.grid(row=1, column=0)
operator_dropdown.grid(row=1, column=1)
num2_label.grid(row=2, column=0)
num2_entry.grid(row=2, column=1)
result_label.grid(row=3, column=0)
result_entry.grid(row=3, column=1)
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=0)
clear_button = tk.Button(window, text="Clear", command=clear)
clear_button.grid(row=4, column=1)
# run the program:
window.mainloop()
