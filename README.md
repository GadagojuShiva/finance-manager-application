# Personal Finance Manager

This Python application serves as a simple Personal Finance Manager using the Tkinter library for the graphical user interface, SQLite for the database, and Pandas for data manipulation. The application allows users to set a budget, add expenses, view their budget, and generate financial reports.

## Prerequisites
- Python 3 installed on your system.
- Required Python packages can be installed using the following command:

    ```bash
    pip install tk tkcalendar pandas
    ```

## Instructions to Execute
1. **Clone the Repository:**

    ```bash
    git clone repo url
    cd Personal-Finance-Manager
    ```

2. **Run the Application:**

    ```bash
    python main.py
    ```

## Usage
- Click on the "Set Budget" button to set your monthly budget.
- Click on the "View Budget" button to see your current budget.
- Click on the "Add Expenses" button to add your daily expenses.
- Click on the "Generate Financial Report" button to view and download expense reports.

## Database
- The application uses SQLite, and the database file (`expenses.db`) will be created in the project directory.

**Note:**
- Make sure to close the application properly to ensure the database connection is closed.
- The application uses Tkinter, which may have limitations on certain systems (e.g., Mac OS). If you encounter issues, please ensure your Python environment and dependencies are correctly set up.

## How to Use
1. Set your monthly budget using the "Set Budget" button.
2. View your current budget using the "View Budget" button.
3. Add daily expenses using the "Add Expenses" button.
4. Generate financial reports using the "Generate Financial Report" button, and you can filter reports by year.
5. Download the expense report in CSV format using the "Download CSV" button.

## Database Schema
The SQLite database (`expenses.db`) contains a table named `expenses` with the following columns:
- `id` (INTEGER, Primary Key, Autoincrement)
- `category` (TEXT)
- `amount` (REAL)
- `date` (TEXT)

## Closing the Application
The application automatically closes the SQLite database connection when the main window is closed.


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
    git clone repo name
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
