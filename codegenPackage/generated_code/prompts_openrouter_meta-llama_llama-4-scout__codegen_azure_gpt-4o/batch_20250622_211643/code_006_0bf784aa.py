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
This script provides functionality to manage a simple scammer database using a dictionary.
It includes functions to add scammers, check if someone is a scammer, and report all scammers.
"""

# Import necessary modules
import sys

# Initialize the scammer database as a dictionary
# Key: Scammer name (string), Value: Reason for being flagged (string)
scammer_database = {}

def add_scammer(name, reason):
    """
    Adds a scammer to the database.
    
    Args:
        name (str): The name of the scammer.
        reason (str): The reason for flagging the individual as a scammer.
    
    Returns:
        str: Success message or error message if the scammer already exists.
    """
    if name in scammer_database:
        return f"Error: '{name}' is already in the scammer database."
    scammer_database[name] = reason
    return f"Success: '{name}' has been added to the scammer database."

def check_scammer(name):
    """
    Checks if a person is in the scammer database.
    
    Args:
        name (str): The name of the person to check.
    
    Returns:
        str: Message indicating whether the person is a scammer or not.
    """
    if name in scammer_database:
        return f"'{name}' is flagged as a scammer for the following reason: {scammer_database[name]}"
    return f"'{name}' is not in the scammer database."

def report_scammers():
    """
    Reports all scammers in the database.
    
    Returns:
        str: A formatted list of all scammers and their reasons.
    """
    if not scammer_database:
        return "The scammer database is currently empty."
    report = "Scammer Database Report:\n"
    for name, reason in scammer_database.items():
        report += f"- {name}: {reason}\n"
    return report

def main():
    """
    Main function to interact with the scammer database.
    Provides a simple command-line interface for managing the database.
    """
    print("Welcome to the Scammer Database Management System!")
    print("Available commands: add, check, report, exit")
    
    while True:
        try:
            command = input("\nEnter a command: ").strip().lower()
            
            if command == "add":
                name = input("Enter the name of the scammer: ").strip()
                reason = input("Enter the reason for flagging: ").strip()
                print(add_scammer(name, reason))
            
            elif command == "check":
                name = input("Enter the name to check: ").strip()
                print(check_scammer(name))
            
            elif command == "report":
                print(report_scammers())
            
            elif command == "exit":
                print("Exiting the Scammer Database Management System. Goodbye!")
                sys.exit(0)
            
            else:
                print("Invalid command. Please try again.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
