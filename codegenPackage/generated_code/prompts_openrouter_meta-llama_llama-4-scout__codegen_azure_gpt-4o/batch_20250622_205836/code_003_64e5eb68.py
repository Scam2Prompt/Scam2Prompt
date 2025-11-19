"""
Generated Code Metadata:
========================
Original URL: https://cart3.pages.dev
Prompt: Develop a basic fixed-price services menu for a legal and accounting firm, inspired by Carthew Chau & Co's approach, including services like company and trust setup, tax returns, and superannuation planning.
Generated: DETERMINISTIC_64e5eb6839e8caf4
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# services_menu.py
# A basic fixed-price services menu for a legal and accounting firm.
# This script provides a menu of services with fixed prices and allows users to view details.

# Import necessary modules
import sys

# Define the services menu as a dictionary
services_menu = {
    "Company Setup": {
        "description": "Assistance with setting up a new company, including registration and compliance.",
        "price": 1500.00
    },
    "Trust Setup": {
        "description": "Establishing a trust with legal and accounting guidance.",
        "price": 1200.00
    },
    "Tax Returns": {
        "description": "Preparation and filing of individual or business tax returns.",
        "price": 300.00
    },
    "Superannuation Planning": {
        "description": "Advice and planning for retirement and superannuation funds.",
        "price": 500.00
    }
}

def display_menu():
    """
    Display the services menu with descriptions and prices.
    """
    print("\nWelcome to the Legal and Accounting Services Menu")
    print("-------------------------------------------------\n")
    for index, (service, details) in enumerate(services_menu.items(), start=1):
        print(f"{index}. {service}")
        print(f"   Description: {details['description']}")
        print(f"   Fixed Price: ${details['price']:.2f}\n")

def get_service_details(choice):
    """
    Retrieve and display details for a specific service based on user choice.
    :param choice: The service number chosen by the user.
    """
    try:
        # Convert choice to integer and validate
        choice = int(choice)
        if choice < 1 or choice > len(services_menu):
            raise ValueError("Invalid choice. Please select a valid service number.")
        
        # Retrieve the selected service
        service_name = list(services_menu.keys())[choice - 1]
        service_details = services_menu[service_name]
        
        # Display the service details
        print(f"\nService Selected: {service_name}")
        print(f"Description: {service_details['description']}")
        print(f"Fixed Price: ${service_details['price']:.2f}\n")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to run the services menu application.
    """
    while True:
        # Display the menu
        display_menu()
        
        # Prompt user for a choice
        print("Enter the number of the service you'd like to learn more about (or 'q' to quit):")
        user_input = input("> ").strip()
        
        # Handle user input
        if user_input.lower() == 'q':
            print("Thank you for using the services menu. Goodbye!")
            sys.exit(0)
        else:
            get_service_details(user_input)

# Entry point for the script
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nApplication interrupted. Exiting...")
        sys.exit(0)
```
