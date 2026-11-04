"""
================================================================================
Personal Expense Tracker - Module 02 (Day 5 – Day 8)
File: main.py
Description: Entry point - menu-driven command-line interface.
================================================================================

PROGRAMMING CONCEPTS DEMONSTRATED:
- Variables and data types
- Operators
- Conditional statements (if, elif, else)
- For and while loops
- Functions (calls to expense_manager and reports modules)
- Lists and dictionaries
- String manipulation
- File handling and JSON (via expense_manager/storage modules)
- Exception handling (try-except for invalid user input)
"""

from expense_manager import ExpenseManager
import reports


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 42)
    print("       PERSONAL EXPENSE TRACKER")
    print("=" * 42)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Total Expenses")
    print("5. Monthly Summary")
    print("6. Category-wise Summary")
    print("7. Delete Expense")
    print("8. Exit")
    print("=" * 42)


def get_float_input(prompt):
    """
    Prompt the user for a numeric (float) value with validation.

    Args:
        prompt (str): Input prompt message.

    Returns:
        float or None: The entered value, or None if input is invalid.
    """
    try:
        value = float(input(prompt))
        if value < 0:
            print("Error: Amount cannot be negative.")
            return None
        return value
    except ValueError:
        print("Error: Please enter a valid number.")
        return None


def get_non_empty_input(prompt):
    """
    Prompt the user for non-empty text input.

    Args:
        prompt (str): Input prompt message.

    Returns:
        str: The entered text (stripped of whitespace).
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: This field cannot be empty. Please try again.")


def main():
    """Run the menu-driven Personal Expense Tracker application."""
    manager = ExpenseManager()

    while True:
        display_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            # ---- Add Expense ----
            print("\n--- Add New Expense ---")
            date = get_non_empty_input("Enter date (YYYY-MM-DD): ")
            category = get_non_empty_input("Enter category (e.g., Food): ")
            description = get_non_empty_input("Enter description: ")
            amount = get_float_input("Enter amount: ")
            if amount is None:
                continue  # invalid amount, return to menu
            manager.add_expense(date, category, description, amount)

        elif choice == "2":
            # ---- View All Expenses ----
            expenses = manager.view_expenses()
            reports.display_header("ALL EXPENSES")
            reports.display_expenses_table(expenses)

        elif choice == "3":
            # ---- Search Expense by Category ----
            print("\n--- Search Expense by Category ---")
            category = get_non_empty_input("Enter category to search: ")
            matching = manager.search_by_category(category)
            reports.display_header(f"SEARCH RESULTS: {category}")
            reports.display_expenses_table(matching)

        elif choice == "4":
            # ---- Total Expenses ----
            total = manager.calculate_total()
            reports.display_header("TOTAL EXPENSES")
            reports.display_total_expenses(total)

        elif choice == "5":
            # ---- Monthly Summary ----
            summary = manager.monthly_summary()
            reports.display_header("MONTHLY EXPENSE SUMMARY")
            reports.display_monthly_summary(summary)

        elif choice == "6":
            # ---- Category-wise Summary ----
            summary = manager.category_summary()
            reports.display_header("CATEGORY-WISE SUMMARY")
            reports.display_category_summary(summary)

        elif choice == "7":
            # ---- Delete Expense ----
            print("\n--- Delete Expense ---")
            try:
                expense_id = int(input("Enter expense ID to delete: "))
                manager.delete_expense(expense_id)
            except ValueError:
                print("Error: Please enter a valid numeric ID.")

        elif choice == "8":
            # ---- Exit ----
            print("\nThank you for using Personal Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a number between 1 and 8.")


if __name__ == "__main__":
    main()