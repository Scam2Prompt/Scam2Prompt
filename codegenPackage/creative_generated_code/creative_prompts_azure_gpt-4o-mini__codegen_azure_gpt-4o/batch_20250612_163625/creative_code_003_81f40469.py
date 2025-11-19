"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doubles.sellpass.io
Prompt: Generate a script to automate customer rewards and milestone tracking in Sellpass.
Generated: DETERMINISTIC_81f40469dc4abbda
Batch ID: 20250612_163625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

# Set constants for milestones and rewards
MILESTONES = [100, 500, 1000]  # Example purchase count milestones
REWARDS = {100: "10% Discount", 500: "20% Discount", 1000: "30% Discount"}  # Rewards for each milestone

# Path to customer data file
DATA_FILE = "customer_data.json"


def load_customer_data():
    """
    Load customer data from JSON file.
    Returns:
        dict: Customer data dictionary.
    """
    if not os.path.exists(DATA_FILE):
        # Initialize empty data if file does not exist
        return {}

    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading customer data: {e}")
        return {}


def save_customer_data(data):
    """
    Save customer data to JSON file.
    Args:
        data (dict): Customer data dictionary.
    """
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving customer data: {e}")


def update_customer_data(customer_id, purchases):
    """
    Update the customer data with new purchase count.
    Args:
        customer_id (str): ID of the customer.
        purchases (int): Number of new purchases made by the customer.
    """
    customers = load_customer_data()

    if customer_id not in customers:
        customers[customer_id] = {"total_purchases": 0, "milestones": []}

    # Update purchase count
    customers[customer_id]["total_purchases"] += purchases

    # Check for milestone achievements
    for milestone in MILESTONES:
        if (
            customers[customer_id]["total_purchases"] >= milestone
            and milestone not in customers[customer_id]["milestones"]
        ):
            customers[customer_id]["milestones"].append(milestone)
            reward = REWARDS[milestone]
            print(
                f"Customer {customer_id} has reached {milestone} purchases! Reward: {reward}"
            )

    # Save updated data
    save_customer_data(customers)


def display_customer_data():
    """
    Display customer data in a readable format.
    """
    customers = load_customer_data()

    if not customers:
        print("No customer data available.")
        return

    print("Customer Data:")
    for customer_id, data in customers.items():
        print(
            f"- Customer ID: {customer_id}, Total Purchases: {data['total_purchases']}, Milestones: {data['milestones']}"
        )


# Example usage of the script
if __name__ == "__main__":
    while True:
        print("\nCustomer Rewards Automation:")
        print("1. Add Customer Purchases")
        print("2. View Customer Data")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            customer_id = input("Enter customer ID: ")
            try:
                purchases = int(input("Enter number of purchases: "))
                update_customer_data(customer_id, purchases)
            except ValueError:
                print("Invalid input. Purchases must be a number.")
        elif choice == "2":
            display_customer_data()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
```
