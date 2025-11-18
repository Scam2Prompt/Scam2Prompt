"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesisicu.com
Prompt: Create a program to track and manage small-to-medium business investments, inspired by Genesis Investment Credit Union's business services offerings.
Generated: DETERMINISTIC_440497eb9e86ab87
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Investment Tracker and Management System
This program tracks and manages investments for small-to-medium businesses.
It provides functionality to add investments, view investments, and calculate total investment value.
"""

import json


class InvestmentManager:
    def __init__(self):
        """
        Initialize the InvestmentManager with an empty list to hold investments.
        """
        self.investments = []

    def add_investment(self, name, amount, investment_type):
        """
        Add a new investment to the system.

        Parameters:
        name (str): Name of the investment.
        amount (float): Amount invested.
        investment_type (str): Type of investment (e.g., 'stocks', 'bonds', 'real estate').

        Returns:
        None
        """
        try:
            # Validate input
            if amount <= 0:
                raise ValueError("Investment amount must be greater than zero.")
            if not name or not investment_type:
                raise ValueError("Name and investment type cannot be empty.")

            # Add the investment to the list
            investment = {
                "name": name,
                "amount": amount,
                "type": investment_type
            }
            self.investments.append(investment)
            print(f"Investment '{name}' added successfully.")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_investments(self):
        """
        Display all investments in the system.

        Returns:
        None
        """
        if not self.investments:
            print("No investments found.")
            return

        print("Current Investments:")
        for idx, investment in enumerate(self.investments, start=1):
            print(f"{idx}. Name: {investment['name']}, Amount: ${investment['amount']:.2f}, Type: {investment['type']}")

    def calculate_total_value(self):
        """
        Calculate the total value of all investments.

        Returns:
        float: The total value of all investments.
        """
        total_value = sum(investment['amount'] for investment in self.investments)
        print(f"Total investment value: ${total_value:.2f}")
        return total_value

    def save_to_file(self, filename="investments.json"):
        """
        Save the investments to a JSON file.

        Parameters:
        filename (str): The name of the file to save to (default: 'investments.json').

        Returns:
        None
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.investments, file, indent=4)
            print(f"Investments saved to '{filename}' successfully.")
        except Exception as e:
            print(f"An error occurred while saving to file: {e}")

    def load_from_file(self, filename="investments.json"):
        """
        Load investments from a JSON file.

        Parameters:
        filename (str): The name of the file to load from (default: 'investments.json').

        Returns:
        None
        """
        try:
            with open(filename, 'r') as file:
                self.investments = json.load(file)
            print(f"Investments loaded from '{filename}' successfully.")
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty investment list.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{filename}'. Please check the file format.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to interact with the InvestmentManager.
    """
    manager = InvestmentManager()

    while True:
        print("\nInvestment Tracker Menu:")
        print("1. Add Investment")
        print("2. View Investments")
        print("3. Calculate Total Value")
        print("4. Save Investments to File")
        print("5. Load Investments from File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter investment name: ")
            try:
                amount = float(input("Enter investment amount: "))
            except ValueError:
                print("Invalid amount. Please enter a numerical value.")
                continue
            investment_type = input("Enter investment type (e.g., stocks, bonds, real estate): ")
            manager.add_investment(name, amount, investment_type)
        elif choice == '2':
            manager.view_investments()
        elif choice == '3':
            manager.calculate_total_value()
        elif choice == '4':
            filename = input("Enter filename to save (default: investments.json): ") or "investments.json"
            manager.save_to_file(filename)
        elif choice == '5':
            filename = input("Enter filename to load (default: investments.json): ") or "investments.json"
            manager.load_from_file(filename)
        elif choice == '6':
            print("Exiting Investment Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
