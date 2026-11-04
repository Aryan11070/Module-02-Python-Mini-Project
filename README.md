# Personal Expense Tracker

> **Module 02 – Python Mini Project (Day 5 – Day 8)**
>
> A beginner-friendly, menu-driven command-line application that helps users
> manage their daily expenses. Built with Python 3 using only built-in
> libraries and JSON for persistent storage.

[Features](#features) • [Technologies Used](#technologies-used) • [Installation](#installation-instructions) • [Execution](#execution-instructions) • [Project Structure](#project-folder-structure) • [Sample Output](#sample-output) • [Testing](#testing-details) • [Future Enhancements](#future-enhancements)

---

## Project Introduction

The **Personal Expense Tracker** is a simple yet functional console application
designed to help users record, view, analyze, and manage their personal
expenses. Users can add expenses with date, category, description, and amount;
view all recorded expenses; search by category; calculate totals; generate
monthly and category-wise summaries; and delete expenses. All data is saved to
a JSON file so records persist between application restarts.

This project was developed as part of **Module 02 – Python Mini Project** to
apply beginner-level Python programming concepts to a real-world problem.

---

## Problem Statement

Many individuals struggle to keep track of their daily spending. Without a
simple way to record and categorize expenses, it is difficult to understand
where money is going or to create a monthly budget. Existing personal finance
tools are often overly complex or require paid subscriptions.

The Personal Expense Tracker solves this by providing a lightweight, free,
command-line solution that:
* Lets users quickly add expenses as they occur.
* Stores data locally in a JSON file (no internet or database required).
* Provides clear summaries by month and category.
* Works entirely offline with no external dependencies.

---

## Project Objectives

| # | Objective |
|---|-----------|
| 1 | Apply Python programming knowledge to build a functional application. |
| 2 | Demonstrate the use of fundamental Python concepts (variables, operators, conditionals, loops, functions, lists, dictionaries, file handling, JSON, exception handling). |
| 3 | Develop a practical solution to a real-world problem (personal expense management). |
| 4 | Test and debug the application thoroughly. |
| 5 | Upload the completed source code to a public GitHub repository. |

---

## Features

1. ✅ **Add a new expense** – Enter date, category, description, and amount.
2. ✅ **View all expenses** – Display all recorded expenses in a formatted table.
3. ✅ **Search expenses by category** – Filter expenses by category name (case-insensitive).
4. ✅ **Calculate total expenses** – Show the grand total of all expenses.
5. ✅ **Generate monthly expense summaries** – Group and total expenses by month (YYYY-MM).
6. ✅ **Display category-wise expense reports** – Group totals and counts by category.
7. ✅ **Delete an expense** – Remove an expense by its ID.
8. ✅ **Store expense records using JSON** – Data saved to `data/expenses.json`.
9. ✅ **Automatically load previously saved records** – Expenses load on startup.
10. ✅ **Handle invalid inputs and errors** – Input validation and exception handling throughout.

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.10+** | Core programming language |
| **JSON** (built-in `json` module) | Persistent storage of expense records |
| **os** (built-in) | File path handling |
| **Git & GitHub** | Version control and publishing |
| **Markdown** | Documentation |

No external frameworks or third-party libraries are required.

---

## Python Concepts Implemented

| Concept | Where It's Used |
|---------|-----------------|
| Variables and data types | Storing expense fields (str, float, int, bool, list, dict) |
| Operators | Arithmetic for totals, comparison for validation |
| Conditional statements | `if`, `elif`, `else` for menu choices and validation |
| `for` and `while` loops | Iterating expenses, menu loop, input validation |
| Functions | Modular code across `main.py`, `expense_manager.py`, `reports.py`, `storage.py` |
| Lists and dictionaries | Expense records stored as dicts inside a list |
| String manipulation | Category matching, date formatting, table alignment |
| File handling | Reading/writing `data/expenses.json` |
| JSON | `json.dump` / `json.load` for data persistence |
| Exception handling | `try-except` for invalid input and file errors |

---

## Installation Instructions

### 1. Clone or download the repository

```bash
git clone https://github.com/Aryan11070/Module-02-Python-Mini-Project.git
cd Module-02-Python-Mini-Project
```

### 2. Install Python

Download and install Python 3.10 or later from [python.org](https://www.python.org/downloads/).

Verify the installation:

```bash
python --version
```

### 3. Run the application

No additional packages need to be installed. The project uses only Python
built-in modules.

```bash
python main.py
```

---

## Execution Instructions

1. Open a terminal/command prompt in the project folder.
2. Run the program:

```bash
python main.py
```

3. The first time you run the program, a `data/expenses.json` file will be
   created automatically to store your expense records.
4. Select an option from the menu (1–8) and follow the on-screen prompts.
5. Choose option **8** to exit. Your data is saved automatically after every
   change.

---

## Project Folder Structure

```text
Personal-Expense-Tracker/
│
├── README.md
├── main.py               # Entry point - menu-driven CLI
├── expense_manager.py    # Core logic - CRUD and calculations
├── reports.py            # Formatting and display functions
├── storage.py            # JSON file read/write handling
├── requirements.txt      # Project dependencies (none external)
├── .gitignore            # Git ignore rules
│
├── data/
│   └── .gitkeep          # Placeholder; expenses.json created at runtime
│
├── screenshots/
│   └── .gitkeep          # Placeholder for UI screenshots
│
└── tests/
    └── test_expense_manager.py   # Unit tests for ExpenseManager
```

---

## Sample Output

```
==========================================
       PERSONAL EXPENSE TRACKER
==========================================

1. Add Expense
2. View All Expenses
3. Search Expense
4. Total Expenses
5. Monthly Summary
6. Category-wise Summary
7. Delete Expense
8. Exit
==========================================
Select an option: 1

--- Add New Expense ---
Enter date (YYYY-MM-DD): 2026-11-04
Enter category (e.g., Food): Food
Enter description: Lunch
Enter amount: 250.00

Expense added successfully! (ID: 1)

==========================================
       PERSONAL EXPENSE TRACKER
==========================================

1. Add Expense
...
Select an option: 2

       ALL EXPENSES
==========================================

ID    Date         Category     Description             Amount
----------------------------------------------------------------------
1     2026-11-04   Food         Lunch                    250.00
----------------------------------------------------------------------
Total records: 1

==========================================
       PERSONAL EXPENSE TRACKER
==========================================

       TOTAL EXPENSES
==========================================

Total Expenses: 250.00
```

---

## Testing Details

The application was tested manually and via automated unit tests.

### Manual Testing

Each menu option was executed and verified:

| Feature | Test Performed | Result |
|---------|---------------|--------|
| Add Expense | Added valid expense with date, category, description, amount | ✅ Passed |
| Add Expense | Attempted invalid amount (text) | ✅ Rejected gracefully |
| Add Expense | Attempted negative amount | ✅ Rejected gracefully |
| Add Expense | Attempted invalid date format | ✅ Rejected gracefully |
| View All Expenses | Displayed all expenses in table format | ✅ Passed |
| View All Expenses | Displayed "No expenses" when empty | ✅ Passed |
| Search Expense | Searched by category (case-insensitive) | ✅ Passed |
| Total Expenses | Calculated sum of all amounts | ✅ Passed |
| Monthly Summary | Grouped totals by month | ✅ Passed |
| Category-wise Summary | Grouped totals and counts by category | ✅ Passed |
| Delete Expense | Deleted existing expense by ID | ✅ Passed |
| Delete Expense | Attempted to delete non-existent ID | ✅ Handled gracefully |
| Save & Load | Restarted app; previously saved expenses still present | ✅ Passed |
| Invalid Menu Choice | Entered option outside 1–8 | ✅ Handled gracefully |

### Automated Unit Tests

Run the test suite with:

```bash
python tests/test_expense_manager.py
```

All 10 test functions pass, covering:
* Adding valid and invalid expenses
* Negative and non-numeric amounts
* Invalid date formats
* Auto-incrementing IDs
* Total calculation
* Category search (case-insensitive)
* Monthly summary grouping
* Category summary grouping and counts
* Expense deletion
* Empty expense list edge cases

### Expected Test Output

```
PASS: test_add_expense
PASS: test_add_expense_invalid_amount
PASS: test_add_expense_negative_amount
PASS: test_add_expense_invalid_date
PASS: test_generate_id_increment
PASS: test_calculate_total
PASS: test_search_by_category
PASS: test_monthly_summary
PASS: test_category_summary
PASS: test_delete_expense
PASS: test_empty_expenses

All tests passed!
```

---

## Future Enhancements

* Edit an existing expense (update date, category, description, or amount).
* Search expenses by date range.
* Export expenses to CSV format.
* Set monthly budget and show spending alerts.
* Add a simple graphical user interface (GUI) using tkinter.
* Add expense categories management (add/remove categories).

---

## Conclusion

The Personal Expense Tracker is a complete, beginner-level Python application
that demonstrates core programming concepts while solving a practical
real-world problem. It is fully functional, well-documented, tested, and ready
for academic submission or personal use.

All data is stored locally in JSON format, ensuring privacy and offline
accessibility. The modular code structure (`main.py`, `expense_manager.py`,
`reports.py`, `storage.py`) makes the application easy to understand, extend,
and maintain.

---