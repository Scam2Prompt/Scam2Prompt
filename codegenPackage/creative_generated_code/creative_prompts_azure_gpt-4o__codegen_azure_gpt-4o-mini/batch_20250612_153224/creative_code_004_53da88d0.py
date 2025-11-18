"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedesignumbrella.in
Prompt: Write code to automate budgeting and bill checking for residential construction projects, incorporating the steps outlined in The Design Umbrella's project management consultancy services.
Generated: DETERMINISTIC_53da88d09bc46477
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BudgetManager:
    def __init__(self, budget_file):
        """
        Initialize BudgetManager with a budget file.

        :param budget_file: Path to the JSON file containing budget data.
        """
        self.budget_file = budget_file
        self.budget_data = self.load_budget()

    def load_budget(self):
        """
        Load budget data from a JSON file.

        :return: Dictionary with budget data.
        """
        try:
            with open(self.budget_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error(f"Budget file {self.budget_file} not found.")
            return {}
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the budget file.")
            return {}

    def check_bills(self, bills):
        """
        Check if all bills are within the budget.

        :param bills: Dictionary with bill amounts.
        :return: Boolean indicating if all bills are within budget.
        """
        total_budget = self.budget_data.get("total_budget", 0)
        total_bills = sum(bills.values())
        
        if total_bills > total_budget:
            logging.warning("Total bills exceed the budget.")
            return False
        logging.info("All bills are within the budget.")
        return True

    def add_expense(self, category, amount):
        """
        Add an expense to the budget.

        :param category: Category of the expense.
        :param amount: Amount of the expense.
        """
        if category in self.budget_data:
            self.budget_data[category] += amount
        else:
            self.budget_data[category] = amount
        logging.info(f"Added {amount} to {category}. New total for {category}: {self.budget_data[category]}")

    def save_budget(self):
        """
        Save the current budget data to the JSON file.
        """
        try:
            with open(self.budget_file, 'w') as file:
                json.dump(self.budget_data, file, indent=4)
            logging.info("Budget data saved successfully.")
        except IOError:
            logging.error("Error saving budget data to file.")

def main():
    # Initialize budget manager with the budget file path
    budget_file = 'budget.json'
    budget_manager = BudgetManager(budget_file)

    # Example bills to check
    bills = {
        "electricity": 300,
        "water": 150,
        "internet": 100,
    }

    # Check bills against the budget
    if budget_manager.check_bills(bills):
        logging.info("All bills are within the budget limits.")
    else:
        logging.info("Some bills exceed the budget limits.")

    # Adding a new expense
    budget_manager.add_expense("construction", 5000)

    # Saving the updated budget
    budget_manager.save_budget()

if __name__ == "__main__":
    main()
```
