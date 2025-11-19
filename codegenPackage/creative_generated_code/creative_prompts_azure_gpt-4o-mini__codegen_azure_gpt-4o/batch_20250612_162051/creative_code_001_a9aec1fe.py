"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prgmea.pk
Prompt: Write a code snippet to automate the visitor registration process for the Pakistan Readymade Garments Manufacturers & Exporters Association.
Generated: DETERMINISTIC_a9aec1fe30300f3d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

# Constants for file paths (can be replaced with a database in production)
VISITOR_DATA_FILE = "visitor_data.json"

# Function to load existing visitor data
def load_visitor_data():
    try:
        with open(VISITOR_DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []
    except json.JSONDecodeError:
        # Handle corrupted file gracefully
        print("Error: Unable to decode visitor data file. Starting fresh.")
        return []

# Function to save visitor data
def save_visitor_data(data):
    try:
        with open(VISITOR_DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error: Unable to save visitor data. {e}")

# Function to register a new visitor
def register_visitor():
    print("Welcome to Pakistan Readymade Garments Manufacturers & Exporters Association Visitor Registration")
    
    # Collect visitor details
    name = input("Enter your name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    
    email = input("Enter your email: ").strip()
    if not email:
        print("Error: Email cannot be empty.")
        return
    
    phone = input("Enter your phone number: ").strip()
    if not phone:
        print("Error: Phone number cannot be empty.")
        return
    
    purpose = input("Enter purpose of visit: ").strip()
    if not purpose:
        print("Error: Purpose cannot be empty.")
        return
    
    # Capture registration time
    registration_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Store visitor details
    visitor = {
        "name": name,
        "email": email,
        "phone": phone,
        "purpose": purpose,
        "registration_time": registration_time
    }
    
    # Load existing data
    visitors = load_visitor_data()
    
    # Add new visitor to the list
    visitors.append(visitor)
    
    # Save updated data
    save_visitor_data(visitors)
    
    print("Visitor registered successfully!")
    print("Details:")
    print(json.dumps(visitor, indent=4))

# Main function to run the program
def main():
    while True:
        print("\n--- Visitor Registration System ---")
        print("1. Register a Visitor")
        print("2. Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            register_visitor()
        elif choice == "2":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
