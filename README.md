# Personal Finance Manager

This code is a simple implementation of a Personal Finance Manager using Python's Tkinter for the graphical user interface (GUI), SQLite for database storage, and pandas for data manipulation. Here's a breakdown and explanation of the code:

## Purpose

The program allows users to manage their personal finances by setting budgets, adding expenses, viewing financial reports, and more.

## Components

1. **SQLite Database:**
   - Two tables are created: `users` for storing user information and `expenses` for storing expense details.
   - The database is named `expenses.db`.

2. **Class: PersonalFinanceManager:**
   - Manages the main application and GUI.

3. **GUI Components:**
   - Buttons for actions like setting budget, viewing budget, adding expenses, generating financial reports, logging in, registering, and deleting the account.
   - Windows for login, registration, setting budget, increasing budget, and adding expenses.

4. **Functions:**
   - `validate_login`: Validates user login credentials.
   - `validate_registration`: Validates new user registration.
   - `hash_password` and `verify_password`: Hashes and verifies user passwords using SHA-256.
   - `set_budget`, `view_budget`, `increase_budget`, `submit_increase_budget`: Handle budget-related functionalities.
   - `show_add_expense`, `submit_expense`, `get_total_expenses`: Handle expense-related functionalities.
   - `generate_report`, `show_report`, `download_csv`, `get_expenses_by_year`: Generate and display financial reports.
   - `get_year_options`: Get available years for filtering financial reports.

## How to Use

1. **Run the Application:**
   - Execute the script.
   - ![Alt Text](https://github.com/GadagojuShiva/finance-manager-application/blob/main/images/1.png)
   - Tkinter window opens with buttons for various financial management actions.

2. **Login or Register:**
   - Click on "Login" or "Register" to create an account or log in with existing credentials.

3. **Set Budget:**
   - Click "Set Budget" to set the budget for financial management.

4. **View and Increase Budget:**
   - After setting the budget, click "View Budget" to see the current budget.
   - You can also increase the budget by clicking "Increase Budget."

5. **Add Expenses:**
   - Click "Add Expenses" to add your daily expenses, specifying category, amount, and date.

6. **Generate Financial Report:**
   - Click "Generate Financial Report" to view a report of expenses based on selected years.

7. **Delete Account:**
   - Click "Delete Account" to delete your account permanently.

8. **Log Out:**
   - Log out using the exit button or closing the application.

## Prerequisites

1. **Python:**
   - Install Python on your system.

2. **Libraries:**
   - Install required libraries using `pip install tkinter tkcalendar pandas`.

3. **SQLite:**
   - No additional installation needed; SQLite comes with Python.

### Note

- **Security:**
  - This code uses a simple password hashing mechanism. In a real-world application, consider using more secure methods, such as bcrypt.
- **Data Storage:**
  - The user's data is stored in a local SQLite database. In a production environment, consider using a more robust database solution.

Ensure that you have the required prerequisites installed before running the script.



# Project Task Allocation based on Team Member's Skills and Roles

## Team Member 1 (Bairoju Saidachary - Database SQLite):

- **Database Setup:**
  - Design and create SQLite database for expenses.

- **SQL Operations:**
  - Implement basic SQL operations for expense records.

- **Advanced Queries:**
  - Develop SQL queries for monthly and yearly summaries.

- **Database Initialization Script:**
  - Write Python script to initialize the database.


## Team Member 2 (Gadagoju Shiva - Python GUI Development):

- **GUI Development:**
  - Create Tkinter-based GUI for Personal Finance Manager.

- **User Input Handling:**
  - Implement input validation for expense details.

- **Report Generation:**
  - Develop Python functions for financial reports.

- **CSV Export Functionality:**
  - Implement CSV export for expense data.

## Team Member 3 (Shivani - Integration and QA):

- **Integration:**
  - Ensure smooth integration of SQL and Python components.

- **Testing and Bug Fixing:**
  - Conduct thorough testing and address bugs.

- **Documentation:**
  - Document code and provide inline comments.

- **Code Review:**
  - Review code for best practices and style.

## Copyright Notice:
  - All rights reserved. Strictly subject to copyright laws. © 2023 by gadagojushiva.

