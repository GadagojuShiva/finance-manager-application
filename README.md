# Personal Finance Manager

## Overview
This Python application serves as a simple Personal Finance Manager using the Tkinter library for the graphical user interface (GUI) and SQLite for data storage. The application allows users to add expenses, generate financial reports, and download expense data in CSV format.

## Features
- **Add Expenses**: Users can input expense details, including category, amount, and date. The application validates user input for data integrity.

- **Generate Financial Report**: Users can view a financial report displaying expenses based on different time periods (All, Monthly, Yearly). The report includes a summary of total expenses and a downloadable option in CSV format.

## How to Execute
1. **Dependencies**: Ensure you have the required dependencies installed. You can install them using the following:
    ```bash
    pip install pandas
    ```

2. **Run the Application**: Execute the `main.py` file to launch the Personal Finance Manager.
    ```bash
    python main.py
    ```

3. **Using the Application**:
   - Click on "Add Expenses" to input new expenses.
   - Click on "Generate Financial Report" to view and download expense reports.
   - Click on "Exit" to close the application.

## Application Workflow
1. **Add Expenses**:
   - Click on "Add Expenses" to open a new window.
   - Enter expense details: Category (alphabetical), Amount (numeric), Date (dd-mm-yyyy).
   - Click "Submit" to add the expense or "Back" to cancel.

2. **Generate Financial Report**:
   - Click on "Generate Financial Report" to open a new window.
   - The default report shows all expenses. You can choose "Monthly" or "Yearly" from the dropdown to filter by time period.
   - The report includes a Treeview widget displaying Category, Amount, and Date columns.
   - Total expenses for the selected period are displayed, and you can download the report in CSV format using the "Download CSV" button.

3. **Exit Application**:
   - Click on "Exit" to close the application.

## Database
The application uses SQLite to store expense data. The database file is named `expenses.db`.

## Note
Ensure to close the application properly to close the database connection. The connection is closed automatically when the application is closed.

Feel free to explore and modify the code to suit your needs! But Please dont push any changes to main branch
