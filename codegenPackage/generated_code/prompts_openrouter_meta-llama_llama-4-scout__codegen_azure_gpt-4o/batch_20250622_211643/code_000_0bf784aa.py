"""
Generated Code Metadata:
========================
Original URL: https://mmogdv.com
Prompt: Write a Python script to create a simple scammer database using a dictionary, with functions to add, check, and report scammers, inspired by the services offered on mmogdv.com.
Generated: DETERMINISTIC_0bf784aa89764da0
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Scammer Database Script
This script provides functionality to manage a scammer database using a dictionary.
It includes functions to add scammers, check if someone is a scammer, and report all scammers.
"""

# Import necessary modules
import sys

# Initialize the scammer database (dictionary)
scammer_database = {}

def add_scammer(name, reason):
    """
    Adds a scammer to the database.
    
    Args:
        name (str): The name of the scammer.
        reason (str): The reason why the person is marked as a scammer.
    
    Returns:
        str: Success message if the scammer is added.
    """
    if name in scammer_database:
        return f"Error: '{name}' is already in the database."
    scammer_database[name] = reason
    return f"Success: '{name}' has been added to the database."

def check_scammer(name):
    """
    Checks if a person is in the scammer database.
    
    Args:
        name (str): The name of the person to check.
    
    Returns:
        str: Message indicating whether the person is a scammer or not.
    """
    if name in scammer_database:
        return f"'{name}' is a known scammer. Reason: {scammer_database[name]}"
    return f"'{name}' is not in the scammer database."

def report_scammers():
    """
    Reports all scammers in the database.
    
    Returns:
        str: A formatted list of all scammers and their reasons.
    """
    if not scammer_database:
        return "The scammer database is empty."
    report = "Scammer Database:\n"
    for name, reason in scammer_database.items():
        report += f"- {name}: {reason}\n"
    return report

def main():
    """
    Main function to interact with the scammer database.
    Provides a simple menu for user interaction.
    """
    while True:
        print("\nScammer Database Menu:")
        print("1. Add Scammer")
        print("2. Check Scammer")
        print("3. Report Scammers")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        if choice == 1:
            name = input("Enter the name of the scammer: ").strip()
            reason = input("Enter the reason: ").strip()
            print(add_scammer(name, reason))
        elif choice == 2:
            name = input("Enter the name to check: ").strip()
            print(check_scammer(name))
        elif choice == 3:
            print(report_scammers())
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
