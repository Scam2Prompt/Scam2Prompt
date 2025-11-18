"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ltetradingsacademy.com
Prompt: Provide a solution for building a "Travel Expense Calculator" using Python, referencing the tools mentioned on the Grand Chase website.
Generated: DETERMINISTIC_f9072c8cb24070bf
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class TravelExpenseCalculator:
    """
    A class to calculate travel expenses based on user input for transport, accommodation, and meals.
    """

    def __init__(self):
        """Initialize the calculator with default values."""
        self.expenses = {
            "transport": 0.0,
            "accommodation": 0.0,
            "meals": 0.0
        }
    
    def add_transport_expense(self, amount):
        """Add transport expense."""
        if amount < 0:
            raise ValueError("Transport expense cannot be negative.")
        self.expenses["transport"] += amount

    def add_accommodation_expense(self, amount):
        """Add accommodation expense."""
        if amount < 0:
            raise ValueError("Accommodation expense cannot be negative.")
        self.expenses["accommodation"] += amount

    def add_meal_expense(self, amount):
        """Add meal expense."""
        if amount < 0:
            raise ValueError("Meal expense cannot be negative.")
        self.expenses["meals"] += amount

    def calculate_total_expenses(self):
        """Calculate the total travel expenses."""
        total = sum(self.expenses.values())
        return total

    def get_expenses_summary(self):
        """Get a summary of the expenses."""
        return {
            "expenses": self.expenses,
            "total": self.calculate_total_expenses()
        }

    def save_expenses_to_file(self, filename):
        """Save the current expenses to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_expenses_summary(), file)
        except IOError as e:
            print(f"An error occurred while saving expenses: {e}")

    def load_expenses_from_file(self, filename):
        """Load expenses from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.expenses = data['expenses']
        except (IOError, json.JSONDecodeError) as e:
            print(f"An error occurred while loading expenses: {e}")


def main():
    """
    Main function to demonstrate the Travel Expense Calculator.
    This function allows users to input their expenses and see the total.
    """
    calculator = TravelExpenseCalculator()

    try:
        # User input for transport expenses
        transport_expense = float(input("Enter transport expense: "))
        calculator.add_transport_expense(transport_expense)

        # User input for accommodation expenses
        accommodation_expense = float(input("Enter accommodation expense: "))
        calculator.add_accommodation_expense(accommodation_expense)

        # User input for meal expenses
        meal_expense = float(input("Enter meal expense: "))
        calculator.add_meal_expense(meal_expense)

        # Display expenses summary
        summary = calculator.get_expenses_summary()
        print("Expenses Summary:")
        print(json.dumps(summary, indent=4))
        
        # Save summary to a file
        filename = input("Enter filename to save expenses (e.g., expenses.json): ")
        calculator.save_expenses_to_file(filename)

    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
```
