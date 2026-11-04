"""
================================================================================
Personal Expense Tracker - Module 02 (Day 5 – Day 8)
File: expense_manager.py
Description: Core logic for managing expense records (CRUD + calculations).
================================================================================

PROGRAMMING CONCEPTS DEMONSTRATED:
- Variables and data types (str, float, int, bool, list, dict)
- Operators (arithmetic, comparison)
- Conditional statements (if, elif, else)
- For and while loops
- Functions (def, return, parameters, arguments)
- Lists and dictionaries (expense records)
- String manipulation (category matching, formatting)
- File handling and JSON (via storage.py)
- Exception handling (try-except for invalid input)
"""

from storage import load_expenses, save_expenses


class ExpenseManager:
    """Manages a collection of expense records."""

    def __init__(self):
        """Initialize the manager and load existing expenses from storage."""
        self.expenses = load_expenses()

    # ------------------------------------------------------------------
    # Helper: generate a new unique ID
    # ------------------------------------------------------------------
    def _generate_id(self):
        """Return the next available expense ID."""
        if not self.expenses:
            return 1
        max_id = max(expense["id"] for expense in self.expenses)
        return max_id + 1

    # ------------------------------------------------------------------
    # Helper: validate date format (YYYY-MM-DD)
    # ------------------------------------------------------------------
    @staticmethod
    def _is_valid_date(date_string):
        """Basic validation that date looks like YYYY-MM-DD."""
        if len(date_string) != 10:
            return False
        if date_string[4] != "-" or date_string[7] != "-":
            return False
        try:
            year = int(date_string[0:4])
            month = int(date_string[5:7])
            day = int(date_string[8:10])
        except ValueError:
            return False
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        return True

    # ------------------------------------------------------------------
    # Feature 1: Add a new expense
    # ------------------------------------------------------------------
    def add_expense(self, date, category, description, amount):
        """
        Add a new expense record.

        Args:
            date (str): Date in YYYY-MM-DD format.
            category (str): Expense category (e.g., Food, Transport).
            description (str): Short description of the expense.
            amount (float): Amount spent.

        Returns:
            bool: True if added successfully, False if validation fails.
        """
        # Validate inputs
        if not date or not category or not description:
            print("Error: Date, category, and description cannot be empty.")
            return False

        if not self._is_valid_date(date):
            print("Error: Date must be in YYYY-MM-DD format.")
            return False

        try:
            amount = float(amount)
        except ValueError:
            print("Error: Amount must be a valid number.")
            return False

        if amount < 0:
            print("Error: Amount cannot be negative.")
            return False

        category = category.strip()
        description = description.strip()

        expense = {
            "id": self._generate_id(),
            "date": date,
            "category": category,
            "description": description,
            "amount": amount,
        }

        self.expenses.append(expense)

        if save_expenses(self.expenses):
            print(f"\nExpense added successfully! (ID: {expense['id']})")
            return True
        else:
            # Remove from memory if save failed
            self.expenses.pop()
            print("Error: Failed to save expense to file.")
            return False

    # ------------------------------------------------------------------
    # Feature 2: View all expenses
    # ------------------------------------------------------------------
    def view_expenses(self):
        """Return the list of all expense records."""
        return self.expenses

    # ------------------------------------------------------------------
    # Feature 3: Search expenses by category
    # ------------------------------------------------------------------
    def search_by_category(self, category):
        """
        Return expenses matching the given category (case-insensitive).

        Args:
            category (str): Category to search for.

        Returns:
            list: Matching expense dictionaries.
        """
        category_lower = category.strip().lower()
        matching = []
        for expense in self.expenses:
            if expense["category"].lower() == category_lower:
                matching.append(expense)
        return matching

    # ------------------------------------------------------------------
    # Feature 4: Calculate total expenses
    # ------------------------------------------------------------------
    def calculate_total(self):
        """Return the sum of all expense amounts."""
        total = 0.0
        for expense in self.expenses:
            total += expense["amount"]
        return round(total, 2)

    # ------------------------------------------------------------------
    # Feature 5: Monthly expense summary
    # ------------------------------------------------------------------
    def monthly_summary(self):
        """
        Group expenses by month and return totals.

        Returns:
            dict: Keys are 'YYYY-MM' strings, values are total amounts.
        """
        summary = {}
        for expense in self.expenses:
            # Extract 'YYYY-MM' from 'YYYY-MM-DD'
            month_key = expense["date"][0:7]
            if month_key in summary:
                summary[month_key] += expense["amount"]
            else:
                summary[month_key] = expense["amount"]
        # Round all values
        for key in summary:
            summary[key] = round(summary[key], 2)
        return summary

    # ------------------------------------------------------------------
    # Feature 6: Category-wise expense report
    # ------------------------------------------------------------------
    def category_summary(self):
        """
        Group expenses by category and return totals and counts.

        Returns:
            dict: Keys are category names, values are dicts with
                  'total' and 'count'.
        """
        summary = {}
        for expense in self.expenses:
            cat = expense["category"]
            if cat in summary:
                summary[cat]["total"] += expense["amount"]
                summary[cat]["count"] += 1
            else:
                summary[cat] = {"total": expense["amount"], "count": 1}
        # Round totals
        for cat in summary:
            summary[cat]["total"] = round(summary[cat]["total"], 2)
        return summary

    # ------------------------------------------------------------------
    # Feature 7: Delete an expense by ID
    # ------------------------------------------------------------------
    def delete_expense(self, expense_id):
        """
        Delete the expense with the given ID.

        Args:
            expense_id (int): ID of the expense to delete.

        Returns:
            bool: True if deleted, False if not found.
        """
        for index, expense in enumerate(self.expenses):
            if expense["id"] == expense_id:
                deleted = self.expenses.pop(index)
                if save_expenses(self.expenses):
                    print(f"\nExpense ID {expense_id} "
                          f"('{deleted['description']}') deleted successfully.")
                    return True
                else:
                    # Put it back if save failed
                    self.expenses.insert(index, deleted)
                    print("Error: Failed to save changes to file.")
                    return False
        print(f"Error: No expense found with ID {expense_id}.")
        return False


if __name__ == "__main__":
    # Simple self-test when run directly
    print("Testing expense_manager module...")
    manager = ExpenseManager()
    manager.add_expense("2026-11-04", "Food", "Lunch", 250.0)
    manager.add_expense("2026-11-04", "Transport", "Bus fare", 40.0)
    print(f"Total expenses: {manager.calculate_total()}")
    print(f"Expenses count: {len(manager.view_expenses())}")
    print("Expense manager test complete.")