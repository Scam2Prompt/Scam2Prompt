"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alwakeelacademy.com
Prompt: Develop a program to teach financial accounting concepts using the resources and tools referenced by Alwakeel Academy.
Generated: DETERMINISTIC_cbe495ccb919083f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code that fulfills the request:

```python
"""
Financial Accounting Learning Program

This program is designed to teach financial accounting concepts using resources and tools 
referenced by Alwakeel Academy. It provides interactive modules covering topics like journal entries, 
income statements, balance sheets, and financial ratios.

Author: Alwakeel Academy Integration
Language: Python
Last Updated: October 2023
"""

# Import necessary libraries
import json
import sys

# Define global constants for the resources
RESOURCES_FILE = "alwakeel_resources.json"

def load_resources(file_path):
    """
    Load financial accounting resources from a JSON file.

    Args:
        file_path (str): The path to the resources file.

    Returns:
        dict: A dictionary containing the resources data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Resources file '{file_path}' not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: Resources file '{file_path}' contains invalid JSON.")
        sys.exit(1)

def display_menu():
    """
    Display the main menu for the program.
    """
    print("\nWelcome to Financial Accounting Learning Program")
    print("Choose a module:")
    print("1. Journal Entries")
    print("2. Income Statements")
    print("3. Balance Sheets")
    print("4. Financial Ratios")
    print("5. Exit")

def handle_module_choice(choice, resources):
    """
    Handle the user's choice for a module.

    Args:
        choice (int): The user's choice.
        resources (dict): A dictionary containing the resources data.
    """
    if choice == 1:
        print("\n--- Journal Entries Module ---")
        print(resources.get('journal_entries', "No data available for Journal Entries."))
    elif choice == 2:
        print("\n--- Income Statements Module ---")
        print(resources.get('income_statements', "No data available for Income Statements."))
    elif choice == 3:
        print("\n--- Balance Sheets Module ---")
        print(resources.get('balance_sheets', "No data available for Balance Sheets."))
    elif choice == 4:
        print("\n--- Financial Ratios Module ---")
        print(resources.get('financial_ratios', "No data available for Financial Ratios."))
    elif choice == 5:
        print("\nThank you for using the program. Goodbye!")
        sys.exit(0)
    else:
        print("\nInvalid choice. Please try again.")

def main():
    """
    Main function to run the program.
    """
    # Load resources
    resources = load_resources(RESOURCES_FILE)

    # Start interactive loop
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
            handle_module_choice(choice, resources)
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 5.")

# Entry point of the program
if __name__ == "__main__":
    main()
```

### Notes:
1. To make this program functional, create a file named `alwakeel_resources.json` containing JSON data for the financial accounting concepts.
2. Example content for `alwakeel_resources.json`:
   ```json
   {
       "journal_entries": "Learn how to record transactions in bookkeeping.",
       "income_statements": "Understand revenue, expenses, and profit calculation.",
       "balance_sheets": "Study assets, liabilities, and equity structure.",
       "financial_ratios": "Explore ratios like ROI, debt-to-equity, and liquidity."
   }
   ```
3. Place the `alwakeel_resources.json` file in the same directory as the script.
