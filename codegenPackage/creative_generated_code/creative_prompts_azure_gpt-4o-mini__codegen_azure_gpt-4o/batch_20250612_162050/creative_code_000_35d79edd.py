"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Generate a Python script to automate bookkeeping tasks, including payroll processing and inventory management, as described by Vital Corporate Solutions.
Generated: DETERMINISTIC_35d79eddc1d388c4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
import json
from datetime import datetime

# Constants
PAYROLL_FILE = "payroll.csv"  # File containing employee payroll details
INVENTORY_FILE = "inventory.csv"  # File containing inventory details
LOG_FILE = "bookkeeping_log.txt"  # Log file to record operations

# Utility functions
def log_message(message):
    """
    Logs a message to the bookkeeping log file with a timestamp.
    :param message: Message to log
    """
    with open(LOG_FILE, "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {message}\n")

def load_csv(file_path):
    """
    Loads a CSV file into a list of dictionaries.
    :param file_path: Path to the CSV file
    :return: List of dictionaries representing rows in the CSV file
    """
    if not os.path.exists(file_path):
        log_message(f"Error: File {file_path} does not exist.")
        raise FileNotFoundError(f"File {file_path} not found.")
    
    try:
        with open(file_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except Exception as e:
        log_message(f"Error loading CSV file {file_path}: {str(e)}")
        raise

def save_csv(data, file_path):
    """
    Saves a list of dictionaries into a CSV file.
    :param data: List of dictionaries to save
    :param file_path: Path to the CSV file
    """
    try:
        with open(file_path, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        log_message(f"Data successfully saved to {file_path}.")
    except Exception as e:
        log_message(f"Error saving CSV file {file_path}: {str(e)}")
        raise

# Payroll processing
def calculate_payroll(file_path):
    """
    Processes payroll by calculating total salary for employees.
    :param file_path: Path to the payroll CSV file
    """
    try:
        payroll_data = load_csv(file_path)
        for employee in payroll_data:
            try:
                hourly_rate = float(employee["Hourly Rate"])
                hours_worked = float(employee["Hours Worked"])
                employee["Total Pay"] = round(hourly_rate * hours_worked, 2)
            except KeyError as e:
                log_message(f"Error processing payroll data: Missing column {str(e)}.")
                raise
            except ValueError:
                log_message("Error processing payroll data: Invalid numeric values.")
                raise
        save_csv(payroll_data, file_path)
        log_message("Payroll processing complete.")
    except Exception as e:
        log_message(f"Error during payroll processing: {str(e)}")

# Inventory management
def update_inventory(file_path, updates):
    """
    Updates inventory based on provided updates.
    :param file_path: Path to the inventory CSV file
    :param updates: Dictionary of item names and their updated quantities
    """
    try:
        inventory_data = load_csv(file_path)
        for item in inventory_data:
            item_name = item.get("Item Name")
            if item_name in updates:
                try:
                    new_quantity = int(updates[item_name])
                    item["Quantity"] = new_quantity
                except ValueError:
                    log_message(f"Error updating inventory for {item_name}: Invalid quantity value.")
                    raise
        save_csv(inventory_data, file_path)
        log_message("Inventory updates complete.")
    except Exception as e:
        log_message(f"Error during inventory update: {str(e)}")

# Main function
def main():
    """
    Main function to automate bookkeeping tasks.
    """
    try:
        log_message("Bookkeeping tasks started.")
        
        # Process payroll
        log_message("Starting payroll processing...")
        calculate_payroll(PAYROLL_FILE)
        
        # Update inventory
        log_message("Starting inventory updates...")
        updates = {
            "Item A": 50,  # Example updates
            "Item B": 20,
            "Item C": 75
        }
        update_inventory(INVENTORY_FILE, updates)
        
        log_message("Bookkeeping tasks completed.")
    except Exception as e:
        log_message(f"Error in bookkeeping tasks: {str(e)}")

# Entry point
if __name__ == "__main__":
    main()
```
