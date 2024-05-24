# calculator_gui.py
import tkinter as tk
from tkinter import messagebox

# Function to perform addition operation
def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to perform subtraction operation
def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to perform multiplication operation
def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Function to perform division operation
def divide():
    try:
        result = float(entry1.get()) / float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("300x250")
root.configure(bg="#f0f0f0")

# Create entry fields for input
entry1_label = tk.Label(root, text="Number 1:", bg="#f0f0f0", font=("Arial", 10))
entry1_label.grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root, font=("Arial", 10))
entry1.grid(row=0, column=1, padx=10, pady=10)

entry2_label = tk.Label(root, text="Number 2:", bg="#f0f0f0", font=("Arial", 10))
entry2_label.grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root, font=("Arial", 10))
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create buttons for operations
add_button = tk.Button(root, text="Add", command=add, bg="#4CAF50", fg="white", font=("Arial", 10))
add_button.grid(row=2, column=0, padx=10, pady=10)

subtract_button = tk.Button(root, text="Subtract", command=subtract, bg="#4CAF50", fg="white", font=("Arial", 10))
subtract_button.grid(row=2, column=1, padx=10, pady=10)

multiply_button = tk.Button(root, text="Multiply", command=multiply, bg="#4CAF50", fg="white", font=("Arial", 10))
multiply_button.grid(row=3, column=0, padx=10, pady=10)

divide_button = tk.Button(root, text="Divide", command=divide, bg="#4CAF50", fg="white", font=("Arial", 10))
divide_button.grid(row=3, column=1, padx=10, pady=10)

# Label to display result
result_label = tk.Label(root, text="Result: ", bg="#f0f0f0", font=("Arial", 10))
result_label.grid(row=4, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()
