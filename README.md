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

- **GitHub Repository:**
  - (FinanceManager-py07-Dev) Push your files to the GitHub repository. Ensure to add a brief comment while pushing.

## Team Member 2 (Gadagoju Shiva - Python GUI Development):

- **GUI Development:**
  - Create Tkinter-based GUI for Personal Finance Manager.

- **User Input Handling:**
  - Implement input validation for expense details.

- **Report Generation:**
  - Develop Python functions for financial reports.

- **CSV Export Functionality:**
  - Implement CSV export for expense data.

- **GitHub Repository:**
  - (FinanceManager-py07-Dev) Push your files to the GitHub repository. Ensure to add a brief comment while pushing.

## Team Member 3 (Shivani - Integration and QA):

- **Integration:**
  - Ensure smooth integration of SQL and Python components.

- **Testing and Bug Fixing:**
  - Conduct thorough testing and address bugs.

- **Documentation:**
  - Document code and provide inline comments.

- **Code Review:**
  - Review code for best practices and style.

- **GitHub Repository:**
  - (FinanceManager-py07-Dev) Push your files, including bug fixes, to the GitHub repository. Ensure to add a brief comment while pushing.

## Note:

**(FinanceManager-py07-Dev)** This repository is designated for ongoing development and is not intended for production use. Once we meet the project requirements and achieve a stable state, a separate repository will be created for production deployment. Please refrain from using the code in this repository for production purposes.

Thank you for your understanding.

## Pushing and Pulling Changes:

To contribute to the development:
1. **Clone the repository:**
    ```bash
    git clone [repository-url]
    cd FinanceManager-py07-Dev
    ```
2. **Make changes and develop code.**
3. **Before pushing changes, ensure you pull the latest updates:**
    ```bash
    git pull origin main
    ```
4. **Stage your changes:**
    ```bash
    git add .
    ```
5. **Commit the changes with a date and brief description:**
    ```bash
    git commit -m "YYYY-MM-DD: Brief comment describing your changes"
    ```
6. **Push to the repository:**
    ```bash
    git push origin main
    ```

Feel free to explore and modify the code to suit your needs! But Please dont push any changes to main branch
