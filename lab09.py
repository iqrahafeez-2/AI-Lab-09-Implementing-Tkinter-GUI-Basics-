import tkinter as tk
from tkinter import messagebox
import re

root = tk.Tk()
root.title("Employee Registration and Salary Utility System")
root.geometry("750x650")
root.configure(bg="#f0f4f8")

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def submit_form():
    first = first_name.get()
    last = last_name.get()
    email = email_entry.get()
    dept = department.get()

    if not first or not last or not email or not dept:
        messagebox.showerror("Error", "All fields are required!")
        return

    if any(char.isdigit() for char in first) or any(char.isdigit() for char in last):
        messagebox.showerror("Error", "Names cannot contain numbers!")
        return

    if not validate_email(email):
        messagebox.showerror("Error", "Enter a valid email address!")
        return

    messagebox.showinfo(
        "Success",
        f"Employee Registered Successfully!\n\n"
        f"Name: {first} {last}\n"
        f"Email: {email}\n"
        f"Department: {dept}"
    )

def calculate_salary():
    try:
        wage = float(daily_wage.get())
        days = int(working_days.get())

        if wage < 0 or days < 0:
            messagebox.showerror("Error", "Values cannot be negative!")
            return

        total = wage * days
        salary_result.config(text=f"Total Salary: Rs. {total:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Enter valid numeric values!")

def clear_fields():
    first_name.delete(0, tk.END)
    last_name.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    department.delete(0, tk.END)
    daily_wage.delete(0, tk.END)
    working_days.delete(0, tk.END)
    salary_result.config(text="Total Salary: Rs. 0")

notice = tk.Label(
    root,
    text="Welcome to Employee Registration and Salary Utility System",
    font=("Arial", 16, "bold"),
    bg="#2c3e50",
    fg="white",
    pady=10
)
notice.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

tk.Label(root, text="Employee Registration Form",
         font=("Arial", 14, "bold"),
         bg="#f0f4f8").grid(row=1, column=0, columnspan=2, pady=15)

tk.Label(root, text="First Name:", bg="#f0f4f8").grid(row=2, column=0, sticky="w", padx=20)
first_name = tk.Entry(root, width=30)
first_name.grid(row=2, column=1)

tk.Label(root, text="Last Name:", bg="#f0f4f8").grid(row=3, column=0, sticky="w", padx=20)
last_name = tk.Entry(root, width=30)
last_name.grid(row=3, column=1)

tk.Label(root, text="Email Address:", bg="#f0f4f8").grid(row=4, column=0, sticky="w", padx=20)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=4, column=1)

tk.Label(root, text="Department:", bg="#f0f4f8").grid(row=5, column=0, sticky="w", padx=20)
department = tk.Entry(root, width=30)
department.grid(row=5, column=1)

tk.Button(root, text="Submit", bg="#27ae60", fg="white",
          command=submit_form).grid(row=6, column=1, pady=15, sticky="w")

tk.Label(root, text="Salary Utility Calculator",
         font=("Arial", 14, "bold"),
         bg="#f0f4f8").grid(row=7, column=0, columnspan=2, pady=15)

tk.Label(root, text="Daily Wage:", bg="#f0f4f8").grid(row=8, column=0, sticky="w", padx=20)
daily_wage = tk.Entry(root, width=30)
daily_wage.grid(row=8, column=1)

tk.Label(root, text="Working Days:", bg="#f0f4f8").grid(row=9, column=0, sticky="w", padx=20)
working_days = tk.Entry(root, width=30)
working_days.grid(row=9, column=1)

tk.Button(root, text="Calculate Salary",
          bg="#2980b9", fg="white",
          command=calculate_salary).grid(row=10, column=1, pady=10, sticky="w")

salary_result = tk.Label(root,
                         text="Total Salary: Rs. 0",
                         font=("Arial", 12, "bold"),
                         bg="#f0f4f8")
salary_result.grid(row=11, column=1, pady=10)

tk.Button(root, text="Clear",
          bg="#f39c12", fg="white",
          command=clear_fields).grid(row=12, column=0, pady=20)

tk.Button(root, text="Exit",
          bg="#e74c3c", fg="white",
          command=root.quit).grid(row=12, column=1, pady=20)

root.mainloop()
