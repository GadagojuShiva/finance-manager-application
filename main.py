import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import pandas as pd
from datetime import datetime

# SQLite Database Initialization
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        amount REAL,
        date TEXT
    )
''')
conn.commit()

class PersonalFinanceManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Manager")

        # Apply a style theme
        style = ttk.Style()
        style.theme_use("clam")

        # Set color variables
        bg_color = "#F0F0F0"  # Light gray
        button_bg_color = "#4CAF50"  # Green
        button_fg_color = "white"

        # Create a custom style for the main frame
        style.configure("TFrame", background=bg_color)

        # Improve button styling with color and gradient effect
        style.configure("TButton", padding=10, font=("Helvetica", 12), background=button_bg_color, foreground=button_fg_color)
        style.map("TButton", background=[("active", "#45a049")])  # Lighter green on button press

        # Improve label styling
        style.configure("TLabel", font=("Helvetica", 12), background=bg_color)

        # Improve entry styling with rounded edges
        style.configure("TEntry", font=("Helvetica", 12), relief="flat")
        style.map("TEntry", relief=[('active', 'flat')])

        # Adjust window size and padding
        root.geometry("600x400")

        # Improve treeview styling
        style.configure("Treeview.Heading", font=("Helvetica", 12), background=button_bg_color, foreground=button_fg_color)
        style.configure("Treeview", font=("Helvetica", 11), background=bg_color)

        self.main_frame = ttk.Frame(root, padding="10", style="TFrame")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.add_expense_button = ttk.Button(self.main_frame, text="Add Expenses", command=self.show_add_expense)
        self.add_expense_button.grid(row=0, column=0, padx=5, pady=5)

        self.generate_report_button = ttk.Button(self.main_frame, text="Generate Financial Report", command=self.generate_report)
        self.generate_report_button.grid(row=0, column=1, padx=5, pady=5)

        self.exit_button = ttk.Button(self.main_frame, text="Exit", command=root.destroy)
        self.exit_button.grid(row=0, column=2, padx=5, pady=5)

        self.report_window = None  # Initialize the report_window as an instance variable

    def show_add_expense(self):
        self.add_expense_window = tk.Toplevel(self.root)
        self.add_expense_window.title("Add Expenses")

        # Improve entry widget alignment and add a subtle border
        self.category_label = ttk.Label(self.add_expense_window, text="Category:", style="TLabel")
        self.category_label.grid(row=0, column=0, padx=5, pady=5)
        self.category_entry = ttk.Entry(self.add_expense_window, justify="right", style="TEntry")
        self.category_entry.grid(row=0, column=1, padx=5, pady=5)

        self.amount_label = ttk.Label(self.add_expense_window, text="Amount:", style="TLabel")
        self.amount_label.grid(row=1, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(self.add_expense_window, justify="right", style="TEntry")
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.date_label = ttk.Label(self.add_expense_window, text="Date (dd-mm-yyyy):", style="TLabel")
        self.date_label.grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = ttk.Entry(self.add_expense_window, justify="right", style="TEntry")
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        self.submit_button = ttk.Button(self.add_expense_window, text="Submit", command=self.submit_expense)
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.back_button = ttk.Button(self.add_expense_window, text="Back", command=self.add_expense_window.destroy)
        self.back_button.grid(row=4, column=0, columnspan=2, pady=10)

    def submit_expense(self):
        category = self.category_entry.get().strip()
        amount = self.amount_entry.get().strip()
        date_str = self.date_entry.get().strip()

        if not category.isalpha():
            messagebox.showerror("Error", "Category should only contain alphabets.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount should be a valid number.")
            return

        try:
            date_obj = datetime.strptime(date_str, "%d-%m-%Y").date()
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use dd-mm-yyyy.")
            return

        cursor.execute('''
            INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)
        ''', (category, amount, date_obj))
        conn.commit()

        messagebox.showinfo("Success", "Expense added successfully.")
        self.add_expense_window.destroy()

    def generate_report(self):
        if self.report_window is not None and self.report_window.winfo_exists():
            self.report_window.destroy()

        self.report_window = tk.Toplevel(self.root)
        self.report_window.title("Financial Report")

        self.tree = ttk.Treeview(self.report_window, columns=("Category", "Amount", "Date"), show="headings", style="Treeview")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Date", text="Date")

        self.total_expense_label = ttk.Label(self.report_window, text="Total Expense: ₹0.00", style="TLabel")
        self.total_expense_label.pack(pady=10)

        self.download_button = ttk.Button(self.report_window, text="Download CSV", command=self.download_csv)
        self.download_button.pack(pady=10)

        self.show_report()

    def show_report(self, period=None):
        self.tree.delete(*self.tree.get_children())
        total_expense = 0

        if period == "Monthly":
            today = datetime.now()
            start_date = datetime(today.year, today.month, 1)
            end_date = datetime(today.year, today.month + 1, 1) - pd.DateOffset(days=1)
            df = pd.read_sql_query(f"SELECT * FROM expenses WHERE date BETWEEN '{start_date.strftime('%Y-%m-%d')}' AND '{end_date.strftime('%Y-%m-%d')}'", conn)
        elif period == "Yearly":
            today = datetime.now()
            start_date = datetime(today.year, 1, 1)
            end_date = datetime(today.year, 12, 31)
            df = pd.read_sql_query(f"SELECT * FROM expenses WHERE date BETWEEN '{start_date.strftime('%Y-%m-%d')}' AND '{end_date.strftime('%Y-%m-%d')}'", conn)
        else:
            df = pd.read_sql_query("SELECT * FROM expenses", conn)

        for index, row in df.iterrows():
            self.tree.insert("", tk.END, values=(row['category'], row['amount'], row['date']))
            total_expense += row['amount']

        self.total_expense_label.config(text=f"Total Expense: ₹{total_expense:.2f}")

        self.tree.pack(expand=tk.YES, fill=tk.BOTH)

    def download_csv(self):
        df = pd.read_sql_query("SELECT * FROM expenses", conn)
        if not df.empty:
            total_expense = df['amount'].sum()
            df = pd.concat([df, pd.DataFrame([['Total Expense', total_expense, '']], columns=['category', 'amount', 'date'])], ignore_index=True)

            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if file_path:
                df.to_csv(file_path, index=False)
                messagebox.showinfo("Success", "CSV file saved successfully.")
        else:
            messagebox.showinfo("Info", "No expenses to download.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalFinanceManager(root)
    root.mainloop()

# Close the database connection when the application is closed
conn.close()