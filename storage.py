"""
================================================================================
Personal Expense Tracker - Module 02 (Day 5 – Day 8)
File: storage.py
Description: Handles reading and writing expense records to a JSON file.
================================================================================

PROGRAMMING CONCEPTS DEMONSTRATED:
- File handling (open, read, write)
- JSON (json.dump, json.load)
- Exception handling (try-except for file and JSON errors)
- os module for path handling
"""

import json
import os

# Path to the JSON data file where expenses are stored
EXPENSES_FILE = os.path.join("data", "expenses.json")


def load_expenses():
    """
    Load expense records from the JSON data file.

    Returns:
        list: A list of expense dictionaries. Returns an empty list if the
              file does not exist or contains invalid JSON.
    """
    try:
        if os.path.exists(EXPENSES_FILE):
            with open(EXPENSES_FILE, "r") as file:
                expenses = json.load(file)
            # Ensure we always return a list
            if isinstance(expenses, list):
                return expenses
            else:
                print("Warning: Data file contained invalid format. "
                      "Starting with empty records.")
                return []
        else:
            # No data file yet - start fresh
            return []
    except json.JSONDecodeError:
        print("Warning: Could not read data file (corrupted JSON). "
              "Starting with empty records.")
        return []
    except IOError as error:
        print(f"Warning: Could not read data file ({error}). "
              "Starting with empty records.")
        return []


def save_expenses(expenses):
    """
    Save expense records to the JSON data file.

    Args:
        expenses (list): List of expense dictionaries to save.

    Returns:
        bool: True if saving succeeded, False otherwise.
    """
    try:
        # Make sure the data folder exists before writing
        os.makedirs(os.path.dirname(EXPENSES_FILE), exist_ok=True)
        with open(EXPENSES_FILE, "w") as file:
            json.dump(expenses, file, indent=4)
        return True
    except IOError as error:
        print(f"Error: Could not save data file ({error}).")
        return False


if __name__ == "__main__":
    # Simple self-test when run directly
    print("Testing storage module...")
    test_expenses = [
        {"id": 1, "date": "2026-11-04", "category": "Food",
         "description": "Lunch", "amount": 250.0}
    ]
    if save_expenses(test_expenses):
        print("Save succeeded.")
    loaded = load_expenses()
    print(f"Loaded {len(loaded)} expense(s).")
    print("Storage module test complete.")