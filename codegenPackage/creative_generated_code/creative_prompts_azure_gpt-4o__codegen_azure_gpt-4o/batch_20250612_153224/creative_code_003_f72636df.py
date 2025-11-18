"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gesec.com.co
Prompt: Write a script to manage emergency preparedness plans for organizations, incorporating key elements from GESEC's "Plan y Preparación ante Emergencias" service.
Generated: DETERMINISTIC_f72636dfbb5b7d63
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Emergency Preparedness Plan Manager

This script allows organizations to manage emergency preparedness plans,
incorporating key elements from GESEC's "Plan y Preparación ante Emergencias" service.

Features:
- Add, view, update, and delete emergency preparedness plans
- Ensure plans include critical elements: risk analysis, communication protocols, evacuation routes, and training schedules
- Error handling for invalid input and data integrity

Requirements:
- Python 3.7+
"""

import json
import os

# Constants
DATA_FILE = "emergency_plans.json"

# Initialize data storage
def initialize_data_storage():
    """
    Ensure the data file exists. If not, create an empty JSON file.
    """
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as file:
            json.dump([], file)

# Load plans
def load_plans():
    """
    Load emergency plans from the JSON file.
    Returns:
        List of plans (list of dicts).
    """
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

# Save plans
def save_plans(plans):
    """
    Save emergency plans to the JSON file.
    Args:
        plans: List of plans to save.
    """
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(plans, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

# Add a new plan
def add_plan():
    """
    Prompt user to add a new emergency preparedness plan.
    """
    print("\n--- Add Emergency Preparedness Plan ---")
    try:
        name = input("Plan Name: ")
        risk_analysis = input("Risk Analysis Summary: ")
        communication_protocols = input("Communication Protocols: ")
        evacuation_routes = input("Evacuation Routes: ")
        training_schedule = input("Training Schedule: ")

        # Validate inputs
        if not name or not risk_analysis or not communication_protocols or not evacuation_routes or not training_schedule:
            print("All fields are required!")
            return

        plan = {
            "name": name,
            "risk_analysis": risk_analysis,
            "communication_protocols": communication_protocols,
            "evacuation_routes": evacuation_routes,
            "training_schedule": training_schedule
        }

        plans = load_plans()
        plans.append(plan)
        save_plans(plans)

        print("Plan added successfully.")

    except Exception as e:
        print(f"Error adding plan: {e}")

# View all plans
def view_plans():
    """
    Display all emergency preparedness plans.
    """
    print("\n--- View Emergency Preparedness Plans ---")
    try:
        plans = load_plans()
        if not plans:
            print("No plans found.")
            return

        for idx, plan in enumerate(plans, start=1):
            print(f"\nPlan #{idx}")
            for key, value in plan.items():
                print(f"{key.capitalize()}: {value}")

    except Exception as e:
        print(f"Error viewing plans: {e}")

# Update an existing plan
def update_plan():
    """
    Update an existing emergency preparedness plan.
    """
    print("\n--- Update Emergency Preparedness Plan ---")
    try:
        plans = load_plans()
        if not plans:
            print("No plans found.")
            return

        view_plans()
        plan_index = int(input("Enter the plan number to update: ")) - 1

        if plan_index < 0 or plan_index >= len(plans):
            print("Invalid plan number.")
            return

        plan = plans[plan_index]
        print("\nEnter new values (leave blank to keep current value):")
        plan["name"] = input(f"Plan Name ({plan['name']}): ") or plan["name"]
        plan["risk_analysis"] = input(f"Risk Analysis ({plan['risk_analysis']}): ") or plan["risk_analysis"]
        plan["communication_protocols"] = input(f"Communication Protocols ({plan['communication_protocols']}): ") or plan["communication_protocols"]
        plan["evacuation_routes"] = input(f"Evacuation Routes ({plan['evacuation_routes']}): ") or plan["evacuation_routes"]
        plan["training_schedule"] = input(f"Training Schedule ({plan['training_schedule']}): ") or plan["training_schedule"]

        save_plans(plans)
        print("Plan updated successfully.")
    
    except Exception as e:
        print(f"Error updating plan: {e}")

# Delete a plan
def delete_plan():
    """
    Delete an emergency preparedness plan.
    """
    print("\n--- Delete Emergency Preparedness Plan ---")
    try:
        plans = load_plans()
        if not plans:
            print("No plans found.")
            return

        view_plans()
        plan_index = int(input("Enter the plan number to delete: ")) - 1

        if plan_index < 0 or plan_index >= len(plans):
            print("Invalid plan number.")
            return

        plans.pop(plan_index)
        save_plans(plans)

        print("Plan deleted successfully.")
    
    except Exception as e:
        print(f"Error deleting plan: {e}")

# Main menu
def main():
    """
    Main menu for managing emergency preparedness plans.
    """
    initialize_data_storage()

    while True:
        print("\n--- Emergency Preparedness Plan Manager ---")
        print("1. Add Plan")
        print("2. View Plans")
        print("3. Update Plan")
        print("4. Delete Plan")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_plan()
            elif choice == 2:
                view_plans()
            elif choice == 3:
                update_plan()
            elif choice == 4:
                delete_plan()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
