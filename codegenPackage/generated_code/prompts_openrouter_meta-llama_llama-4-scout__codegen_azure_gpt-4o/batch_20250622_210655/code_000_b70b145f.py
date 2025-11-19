"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: "Generate a Python script to manage and track fire sprinkler system installations, including client information and service dates."
Generated: DETERMINISTIC_b70b145fea879273
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict

# File to store sprinkler system data
DATA_FILE = "sprinkler_systems.json"

# Load data from file
def load_data() -> List[Dict]:
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Return an empty list if the file does not exist
        return []
    except json.JSONDecodeError:
        # Handle corrupted JSON file
        print("Error: Data file is corrupted. Starting with an empty database.")
        return []

# Save data to file
def save_data(data: List[Dict]) -> None:
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error: Unable to save data. {e}")

# Add a new sprinkler system installation
def add_installation(client_name: str, client_address: str, service_date: str) -> None:
    try:
        # Validate service date format
        datetime.strptime(service_date, "%Y-%m-%d")
        
        data = load_data()
        new_entry = {
            "client_name": client_name,
            "client_address": client_address,
            "service_date": service_date
        }
        data.append(new_entry)
        save_data(data)
        print("Installation added successfully.")
    except ValueError:
        print("Error: Service date must be in YYYY-MM-DD format.")
    except Exception as e:
        print(f"Error: Unable to add installation. {e}")

# View all sprinkler system installations
def view_installations() -> None:
    data = load_data()
    if not data:
        print("No installations found.")
        return
    
    print("Sprinkler System Installations:")
    for idx, entry in enumerate(data, start=1):
        print(f"{idx}. Client Name: {entry['client_name']}")
        print(f"   Address: {entry['client_address']}")
        print(f"   Service Date: {entry['service_date']}")
        print("-" * 40)

# Main menu for user interaction
def main_menu() -> None:
    while True:
        print("\nFire Sprinkler System Management")
        print("1. Add Installation")
        print("2. View Installations")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            client_name = input("Enter client name: ")
            client_address = input("Enter client address: ")
            service_date = input("Enter service date (YYYY-MM-DD): ")
            add_installation(client_name, client_address, service_date)
        elif choice == "2":
            view_installations()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main_menu()
```
