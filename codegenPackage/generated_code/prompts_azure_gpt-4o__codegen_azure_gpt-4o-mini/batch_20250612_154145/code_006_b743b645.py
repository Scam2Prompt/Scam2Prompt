"""
Generated Code Metadata:
========================
Original URL: https://kktravelsolutions.co.tz
Prompt: Develop a program to manage corporate travel itineraries, including cost optimization and resource mobilization, inspired by KK Travel Solutions' corporate travel management solutions.
Generated: DETERMINISTIC_b743b645a6c4f537
Batch ID: 20250612_154145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class TravelItinerary:
    def __init__(self, employee_name: str, destination: str, travel_dates: List[str], budget: float):
        """
        Initialize a travel itinerary for an employee.

        :param employee_name: Name of the employee traveling
        :param destination: Destination of the travel
        :param travel_dates: List of travel dates
        :param budget: Budget allocated for the travel
        """
        self.employee_name = employee_name
        self.destination = destination
        self.travel_dates = travel_dates
        self.budget = budget
        self.expenses = []

    def add_expense(self, description: str, amount: float):
        """
        Add an expense to the itinerary.

        :param description: Description of the expense
        :param amount: Amount of the expense
        """
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")
        self.expenses.append({"description": description, "amount": amount})

    def total_expenses(self) -> float:
        """
        Calculate the total expenses incurred.

        :return: Total expenses
        """
        return sum(expense['amount'] for expense in self.expenses)

    def is_within_budget(self) -> bool:
        """
        Check if total expenses are within the allocated budget.

        :return: True if within budget, False otherwise
        """
        return self.total_expenses() <= self.budget

    def itinerary_summary(self) -> Dict[str, Any]:
        """
        Generate a summary of the itinerary.

        :return: Summary of the itinerary
        """
        return {
            "employee_name": self.employee_name,
            "destination": self.destination,
            "travel_dates": self.travel_dates,
            "budget": self.budget,
            "total_expenses": self.total_expenses(),
            "within_budget": self.is_within_budget(),
            "expenses": self.expenses
        }

class TravelManager:
    def __init__(self):
        """
        Initialize the Travel Manager to handle multiple itineraries.
        """
        self.itineraries = []

    def add_itinerary(self, itinerary: TravelItinerary):
        """
        Add a travel itinerary to the manager.

        :param itinerary: TravelItinerary object to be added
        """
        self.itineraries.append(itinerary)

    def save_itineraries(self, filename: str):
        """
        Save all itineraries to a JSON file.

        :param filename: Name of the file to save itineraries
        """
        try:
            with open(filename, 'w') as file:
                json.dump([itinerary.itinerary_summary() for itinerary in self.itineraries], file, indent=4)
        except IOError as e:
            print(f"Error saving itineraries to {filename}: {e}")

    def load_itineraries(self, filename: str):
        """
        Load itineraries from a JSON file.

        :param filename: Name of the file to load itineraries from
        """
        try:
            with open(filename, 'r') as file:
                itineraries_data = json.load(file)
                for data in itineraries_data:
                    itinerary = TravelItinerary(
                        employee_name=data['employee_name'],
                        destination=data['destination'],
                        travel_dates=data['travel_dates'],
                        budget=data['budget']
                    )
                    for expense in data['expenses']:
                        itinerary.add_expense(expense['description'], expense['amount'])
                    self.add_itinerary(itinerary)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading itineraries from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    travel_manager = TravelManager()

    # Create a new itinerary
    itinerary1 = TravelItinerary("John Doe", "New York", ["2023-10-01", "2023-10-05"], 1500.00)
    itinerary1.add_expense("Flight", 500.00)
    itinerary1.add_expense("Hotel", 600.00)
    itinerary1.add_expense("Meals", 200.00)

    # Add itinerary to manager
    travel_manager.add_itinerary(itinerary1)

    # Save itineraries to a file
    travel_manager.save_itineraries("itineraries.json")

    # Load itineraries from a file
    travel_manager.load_itineraries("itineraries.json")

    # Print summary of itineraries
    for itinerary in travel_manager.itineraries:
        print(itinerary.itinerary_summary())
```
