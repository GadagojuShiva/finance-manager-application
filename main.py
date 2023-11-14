import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkcalendar import DateEntry
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

        self.setup_style()
        self.create_main_frame()

        self.date_cal = None
        self.report_window = None
        self.budget_window = None
        self.budget = 0

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        bg_color = "#F0F0F0"
        button_bg_color = "#4CAF50"
        button_fg_color = "white"

        style.configure("TFrame", background=bg_color)
        style.configure("TButton", padding=10, font=("Helvetica", 12),
                        background=button_bg_color, foreground=button_fg_color)
        style.map("TButton", background=[("active", "#45a049")])
        style.configure("TLabel", font=("Helvetica", 12), background=bg_color)
        style.configure("TEntry", font=("Helvetica", 12), relief="flat")
        style.map("TEntry", relief=[('active', 'flat')])
        style.configure("Treeview.Heading", font=("Helvetica", 12),
                        background=button_bg_color, foreground=button_fg_color)
        style.configure("Treeview", font=(
            "Helvetica", 11), background=bg_color)

    def create_main_frame(self):
        self.main_frame = ttk.Frame(self.root, padding="10", style="TFrame")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.add_buttons_to_main_frame()

    def add_buttons_to_main_frame(self):
        self.set_budget_button = ttk.Button(
            self.main_frame, text="Set Budget", command=self.set_budget)
        self.set_budget_button.grid(row=0, column=0, padx=5, pady=5)

        self.view_budget_button = ttk.Button(
            self.main_frame, text="View Budget", command=self.view_budget)
        self.view_budget_button.grid(row=0, column=1, padx=5, pady=5)

        self.add_expense_button = ttk.Button(
            self.main_frame, text="Add Expenses", command=self.show_add_expense, state=tk.DISABLED)
        self.add_expense_button.grid(row=0, column=2, padx=5, pady=5)

        self.generate_report_button = ttk.Button(
            self.main_frame, text="Generate Financial Report", command=self.generate_report, state=tk.DISABLED)
        self.generate_report_button.grid(row=0, column=3, padx=5, pady=5)

        self.exit_button = ttk.Button(
            self.main_frame, text="Exit", command=self.root.destroy)
        self.exit_button.grid(row=0, column=4, padx=5, pady=5)

    def set_budget(self):
        self.budget_window = tk.Toplevel(self.root)
        self.budget_window.title("Set Budget")

        self.budget_label = ttk.Label(
            self.budget_window, text="Budget:", style="TLabel")
        self.budget_label.grid(row=0, column=0, padx=5, pady=5)
        self.budget_entry = ttk.Entry(
            self.budget_window, justify="right", style="TEntry")
        self.budget_entry.grid(row=0, column=1, padx=5, pady=5)

        self.submit_budget_button = ttk.Button(
            self.budget_window, text="Submit", command=self.submit_budget)
        self.submit_budget_button.grid(row=1, column=0, columnspan=2, pady=10)

    def view_budget(self):
        if self.budget == 0:
            messagebox.showinfo("Budget", "No budget set.")
        else:
            messagebox.showinfo("Budget", f"Current Budget: ₹{self.budget:.2f}")

    def submit_budget(self):
        budget_str = self.budget_entry.get().strip()

        try:
            new_budget = float(budget_str)
        except ValueError:
            messagebox.showerror("Error", "Budget should be a valid number.")
            return

        if messagebox.askyesno("Confirm", f"Set budget to ₹{new_budget:.2f}?"):
            self.budget = new_budget
            messagebox.showinfo(
                "Success", f"Budget set to ₹{self.budget:.2f}")
            self.budget_window.destroy()

            self.add_expense_button["state"] = tk.NORMAL
            self.generate_report_button["state"] = tk.NORMAL

    def show_add_expense(self):
        self.add_expense_window = tk.Toplevel(self.root)
        self.add_expense_window.title("Add Expenses")

        self.category_label = ttk.Label(
            self.add_expense_window, text="Category:", style="TLabel")
        self.category_label.grid(row=0, column=0, padx=5, pady=5)
        self.category_entry = ttk.Entry(
            self.add_expense_window, justify="right", style="TEntry")
        self.category_entry.grid(row=0, column=1, padx=5, pady=5)

        self.amount_label = ttk.Label(
            self.add_expense_window, text="Amount:", style="TLabel")
        self.amount_label.grid(row=1, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(
            self.add_expense_window, justify="right", style="TEntry")
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.date_label = ttk.Label(
            self.add_expense_window, text="Date:", style="TLabel")
        self.date_label.grid(row=2, column=0, padx=5, pady=5)
        self.date_cal = DateEntry(self.add_expense_window, background='darkblue',
                                  foreground='white', borderwidth=2, year=2023, month=11, day=14)  # Customize as needed
        self.date_cal.grid(row=2, column=1, padx=5, pady=5)

        self.submit_button = ttk.Button(
            self.add_expense_window, text="Submit", command=self.submit_expense)
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.back_button = ttk.Button(
            self.add_expense_window, text="Back", command=self.add_expense_window.destroy)
        self.back_button.grid(row=4, column=0, columnspan=2, pady=10)

    def submit_expense(self):
        category = self.category_entry.get().strip()
        amount = self.amount_entry.get().strip()

        if not category.isalpha():
            messagebox.showerror(
                "Error", "Category should only contain alphabets.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount should be a valid number.")
            return

        try:
            date_obj = self.date_cal.get_date()
        except ValueError:
            messagebox.showerror(
                "Error", "Invalid date format. Please use the calendar.")
            return

        if amount > self.budget - self.get_total_expenses():
            messagebox.showerror(
                "Budget Exceeded", "Expense exceeds the budget. Please adjust the amount.")
            return

        cursor.execute('''
            INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)
        ''', (category, amount, date_obj))
        conn.commit()

        messagebox.showinfo("Success", "Expense added successfully.")
        self.add_expense_window.destroy()

    def get_total_expenses(self):
        df = pd.read_sql_query("SELECT * FROM expenses", conn)
        total_expense = df['amount'].sum()
        return total_expense

    def generate_report(self):
        if self.report_window is not None and self.report_window.winfo_exists():
            self.report_window.destroy()

        self.report_window = tk.Toplevel(self.root)
        self.report_window.title("Financial Report")

        self.tree = ttk.Treeview(self.report_window, columns=(
            "Category", "Amount", "Date"), show="headings", style="Treeview")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Date", text="Date")

        self.total_expense_label = ttk.Label(
            self.report_window, text=f"Total Expense: ₹0.00", style="TLabel")
        self.total_expense_label.pack(pady=10)

        self.sort_label = ttk.Label(
            self.report_window, text="Sort by Year:", style="TLabel")
        self.sort_label.pack(pady=10)

        self.sort_combobox = ttk.Combobox(
            self.report_window, values=self.get_year_options())
        self.sort_combobox.set("All Years")
        self.sort_combobox.pack(pady=5)
        self.sort_combobox.bind("<<ComboboxSelected>>", self.show_report)

        self.download_button = ttk.Button(
            self.report_window, text="Download CSV", command=self.download_csv)
        self.download_button.pack(pady=10)

        self.show_report()

    def show_report(self, event=None):
        self.tree.delete(*self.tree.get_children())
        total_expense = 0

        selected_year = self.sort_combobox.get()

        df = self.get_expenses_by_year(selected_year)

        for index, row in df.iterrows():
            self.tree.insert("", tk.END, values=(
                row['category'], row['amount'], row['date']))
            total_expense += row['amount']

        self.total_expense_label.config(
            text=f"Total Expense: ₹{total_expense:.2f}")

        self.tree.pack(expand=tk.YES, fill=tk.BOTH)

    def get_expenses_by_year(self, selected_year):
        if selected_year == "All Years":
            return pd.read_sql_query("SELECT * FROM expenses", conn)
        else:
            start_date = datetime.strptime(
                f"January-{selected_year}", "%B-%Y").date()
            end_date = datetime.strptime(
                f"December-{selected_year}", "%B-%Y").date() + pd.DateOffset(days=31)
            return pd.read_sql_query(
                f"SELECT * FROM expenses WHERE date BETWEEN '{start_date}' AND '{end_date}'", conn)

    def download_csv(self):
        selected_year = self.sort_combobox.get()
        df = self.get_expenses_by_year(selected_year)

        if not df.empty:
            total_expense = df['amount'].sum()
            df = pd.concat([df, pd.DataFrame([['Total Expense', total_expense, '']], columns=[
                           'category', 'amount', 'date'])], ignore_index=True)

            file_path = filedialog.asksaveasfilename(
                defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if file_path:
                df.to_csv(file_path, index=False)
                messagebox.showinfo("Success", "CSV file saved successfully.")
        else:
            messagebox.showinfo("Info", "No expenses to download.")

    def get_year_options(self):
        df = pd.read_sql_query("SELECT * FROM expenses", conn)
        if not df.empty:
            years = pd.to_datetime(df['date']).dt.year.unique()
            return ["All Years"] + list(map(str, years))
        return ["All Years"]


if __name__ == "__main__":
    root = tk.Tk()
    app = PersonalFinanceManager(root)
    root.mainloop()

# Close the database connection when the application is closed
conn.close()
