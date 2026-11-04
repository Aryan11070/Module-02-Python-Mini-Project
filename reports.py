"""
================================================================================
Personal Expense Tracker - Module 02 (Day 5 – Day 8)
File: reports.py
Description: Formatting and display functions for expense reports.
================================================================================

PROGRAMMING CONCEPTS DEMONSTRATED:
- Functions (def, parameters, return)
- For loops (iterating over lists and dictionaries)
- String manipulation (f-strings, alignment)
- Lists and dictionaries
"""


def display_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 45)
    print(f"       {title}")
    print("=" * 45)


def display_expenses_table(expenses):
    """
    Display a list of expenses in a neat table.

    Args:
        expenses (list): List of expense dictionaries.
    """
    if not expenses:
        print("\nNo expenses to display.")
        return

    print(f"\n{'ID':<5} {'Date':<12} {'Category':<15} "
          f"{'Description':<25} {'Amount':>10}")
    print("-" * 70)
    for expense in expenses:
        print(f"{expense['id']:<5} {expense['date']:<12} "
              f"{expense['category']:<15} "
              f"{expense['description']:<25} "
              f"{expense['amount']:>10.2f}")
    print("-" * 70)
    print(f"Total records: {len(expenses)}")


def display_total_expenses(total):
    """Display the grand total of all expenses."""
    print(f"\nTotal Expenses: {total:.2f}")


def display_monthly_summary(summary):
    """
    Display monthly expense summary.

    Args:
        summary (dict): Keys are 'YYYY-MM', values are totals.
    """
    if not summary:
        print("\nNo monthly data available.")
        return

    print(f"\n{'Month':<12} {'Total Expense':>15}")
    print("-" * 30)
    for month in sorted(summary.keys()):
        print(f"{month:<12} {summary[month]:>15.2f}")
    print("-" * 30)
    grand_total = sum(summary.values())
    print(f"{'Grand Total':<12} {grand_total:>15.2f}")


def display_category_summary(summary):
    """
    Display category-wise expense summary.

    Args:
        summary (dict): Keys are categories, values are dicts with
                        'total' and 'count'.
    """
    if not summary:
        print("\nNo category data available.")
        return

    print(f"\n{'Category':<18} {'Count':>8} {'Total':>12}")
    print("-" * 40)
    for category in sorted(summary.keys()):
        data = summary[category]
        print(f"{category:<18} {data['count']:>8} {data['total']:>12.2f}")
    print("-" * 40)
    grand_total = sum(data["total"] for data in summary.values())
    print(f"{'Grand Total':<18} {'':>8} {grand_total:>12.2f}")


if __name__ == "__main__":
    # Simple self-test when run directly
    print("Testing reports module...")
    test_expenses = [
        {"id": 1, "date": "2026-11-04", "category": "Food",
         "description": "Lunch", "amount": 250.0},
        {"id": 2, "date": "2026-11-05", "category": "Transport",
         "description": "Bus fare", "amount": 40.0},
    ]
    display_expenses_table(test_expenses)
    display_total_expenses(290.0)
    print("Reports module test complete.")