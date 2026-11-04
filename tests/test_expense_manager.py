"""
================================================================================
Personal Expense Tracker - Module 02 (Day 5 – Day 8)
File: tests/test_expense_manager.py
Description: Unit tests for the ExpenseManager class.
================================================================================

PROGRAMMING CONCEPTS DEMONSTRATED:
- Functions (test functions)
- Conditional statements (assertions)
- Exception handling (try-except)
- Lists and dictionaries
"""

import os
import sys
import tempfile
import json

# Add the project root to the path so we can import the modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from expense_manager import ExpenseManager
import storage


def test_add_expense():
    """Test adding a valid expense."""
    manager = ExpenseManager()
    manager.expenses = []  # start fresh
    result = manager.add_expense("2026-11-04", "Food", "Lunch", 250.0)
    assert result is True, "Adding valid expense should return True"
    assert len(manager.expenses) == 1, "Should have 1 expense"
    assert manager.expenses[0]["id"] == 1, "First expense ID should be 1"
    assert manager.expenses[0]["category"] == "Food"
    assert manager.expenses[0]["amount"] == 250.0
    print("PASS: test_add_expense")


def test_add_expense_invalid_amount():
    """Test adding an expense with invalid amount."""
    manager = ExpenseManager()
    manager.expenses = []
    result = manager.add_expense("2026-11-04", "Food", "Lunch", "not_a_number")
    assert result is False, "Invalid amount should return False"
    assert len(manager.expenses) == 0, "No expense should be added"
    print("PASS: test_add_expense_invalid_amount")


def test_add_expense_negative_amount():
    """Test adding an expense with negative amount."""
    manager = ExpenseManager()
    manager.expenses = []
    result = manager.add_expense("2026-11-04", "Food", "Lunch", -50.0)
    assert result is False, "Negative amount should return False"
    print("PASS: test_add_expense_negative_amount")


def test_add_expense_invalid_date():
    """Test adding an expense with invalid date format."""
    manager = ExpenseManager()
    manager.expenses = []
    result = manager.add_expense("04-11-2026", "Food", "Lunch", 100.0)
    assert result is False, "Invalid date should return False"
    print("PASS: test_add_expense_invalid_date")


def test_generate_id_increment():
    """Test that IDs increment correctly."""
    manager = ExpenseManager()
    manager.expenses = []
    manager.add_expense("2026-11-04", "Food", "Lunch", 100.0)
    manager.add_expense("2026-11-05", "Transport", "Bus", 20.0)
    assert manager.expenses[0]["id"] == 1
    assert manager.expenses[1]["id"] == 2
    print("PASS: test_generate_id_increment")


def test_calculate_total():
    """Test total calculation."""
    manager = ExpenseManager()
    manager.expenses = []
    manager.add_expense("2026-11-04", "Food", "Lunch", 100.0)
    manager.add_expense("2026-11-05", "Transport", "Bus", 50.0)
    total = manager.calculate_total()
    assert total == 150.0, f"Expected 150.0, got {total}"
    print("PASS: test_calculate_total")


def test_search_by_category():
    """Test searching expenses by category."""
    manager = ExpenseManager()
    manager.expenses = []
    manager.add_expense("2026-11-04", "Food", "Lunch", 100.0)
    manager.add_expense("2026-11-05", "Food", "Dinner", 200.0)
    manager.add_expense("2026-11-06", "Transport", "Bus", 50.0)

    food_expenses = manager.search_by_category("Food")
    assert len(food_expenses) == 2, "Should find 2 food expenses"

    # Case-insensitive check
    food_expenses_lower = manager.search_by_category("food")
    assert len(food_expenses_lower) == 2, "Search should be case-insensitive"

    transport_expenses = manager.search_by_category("Transport")
    assert len(transport_expenses) == 1, "Should find 1 transport expense"

    print("PASS: test_search_by_category")


def test_monthly_summary():
    """Test monthly summary grouping."""
    manager = ExpenseManager()
    manager.expenses = []
    manager.add_expense("2026-11-04", "Food", "Lunch", 100.0)
    manager.add_expense("2026-11-05", "Transport", "Bus", 50.0)
    manager.add_expense("2026-12-01", "Food", "Groceries", 300.0)

    summary = manager.monthly_summary()
    assert summary["2026-11"] == 150.0, f"Expected 150.0 for 2026-11, got {summary.get('2026-11')}"
    assert summary["2026-12"] == 300.0, f"Expected 300.0 for 2026-12, got {summary.get('2026-12')}"
    print("PASS: test_monthly_summary")


def test_category_summary():
    """Test category-wise summary."""
    manager = ExpenseManager()
    manager.expenses = []
    manager.add_expense("2026-11-04", "Food", "Lunch", 100.0)
    manager.add_expense("2026-11-05", "Food", "Dinner", 200.0)
    manager.add_expense("2026-11-06", "Transport", "Bus", 50.0)

    summary = manager.category_summary()
    assert summary["Food"]["total"] == 300.0
    assert summary["Food"]["count"] == 2
    assert summary["Transport"]["total"] == 50.0
    assert summary["Transport"]["count"] == 1
    print("PASS: test_category_summary")


def test_delete_expense():
    """Test deleting an expense by ID."""
    manager = ExpenseManager()
    manager.expenses = []
    manager.add_expense("2026-11-04", "Food", "Lunch", 100.0)
    manager.add_expense("2026-11-05", "Transport", "Bus", 50.0)

    # Temporarily bypass save to test logic in isolation
    original_save = storage.save_expenses
    storage.save_expenses = lambda expenses: True

    try:
        result = manager.delete_expense(1)
        assert result is True, "Deleting existing expense should return True"
        assert len(manager.expenses) == 1, "Should have 1 expense left"
        assert manager.expenses[0]["id"] == 2, "Remaining expense should be ID 2"

        result = manager.delete_expense(99)
        assert result is False, "Deleting non-existent expense should return False"
    finally:
        storage.save_expenses = original_save

    print("PASS: test_delete_expense")


def test_empty_expenses():
    """Test behavior with no expenses."""
    manager = ExpenseManager()
    manager.expenses = []
    assert manager.calculate_total() == 0.0
    assert manager.view_expenses() == []
    assert manager.search_by_category("Food") == []
    assert manager.monthly_summary() == {}
    assert manager.category_summary() == {}
    print("PASS: test_empty_expenses")


if __name__ == "__main__":
    test_add_expense()
    test_add_expense_invalid_amount()
    test_add_expense_negative_amount()
    test_add_expense_invalid_date()
    test_generate_id_increment()
    test_calculate_total()
    test_search_by_category()
    test_monthly_summary()
    test_category_summary()
    test_delete_expense()
    test_empty_expenses()
    print("\nAll tests passed!")