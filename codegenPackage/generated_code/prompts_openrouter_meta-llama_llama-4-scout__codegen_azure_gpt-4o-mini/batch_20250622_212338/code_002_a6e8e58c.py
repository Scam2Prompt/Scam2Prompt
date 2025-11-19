"""
Generated Code Metadata:
========================
Original URL: https://lethmixedslowpitch.com
Prompt: Create a comprehensive budget for a slo-pitch softball tournament using a budget generator tool and provide a detailed breakdown of estimated costs.
Generated: DETERMINISTIC_a6e8e58cb4e71c85
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class BudgetItem:
    """Class to represent a budget item with a name and cost."""
    
    def __init__(self, name: str, cost: float):
        self.name = name
        self.cost = cost

    def to_dict(self):
        """Convert the budget item to a dictionary for JSON serialization."""
        return {"name": self.name, "cost": self.cost}

class Budget:
    """Class to manage a budget for a slo-pitch softball tournament."""
    
    def __init__(self):
        self.items = []

    def add_item(self, name: str, cost: float):
        """Add a new item to the budget."""
        if cost < 0:
            raise ValueError("Cost cannot be negative.")
        self.items.append(BudgetItem(name, cost))

    def total_cost(self) -> float:
        """Calculate the total cost of all budget items."""
        return sum(item.cost for item in self.items)

    def generate_budget_report(self) -> str:
        """Generate a detailed budget report in JSON format."""
        report = {
            "total_cost": self.total_cost(),
            "items": [item.to_dict() for item in self.items]
        }
        return json.dumps(report, indent=4)

def main():
    """Main function to create a budget for the slo-pitch softball tournament."""
    budget = Budget()

    # Adding estimated costs for the tournament
    try:
        budget.add_item("Field Rental", 300.00)
        budget.add_item("Umpire Fees", 200.00)
        budget.add_item("Team Registration Fees", 150.00)
        budget.add_item("Equipment Rental", 100.00)
        budget.add_item("Concessions Supplies", 75.00)
        budget.add_item("Trophies and Awards", 50.00)
        budget.add_item("Marketing and Promotion", 100.00)
        budget.add_item("First Aid Supplies", 25.00)
    except ValueError as e:
        print(f"Error adding budget item: {e}")
        return

    # Generate and print the budget report
    budget_report = budget.generate_budget_report()
    print("Tournament Budget Report:")
    print(budget_report)

if __name__ == "__main__":
    main()
```
