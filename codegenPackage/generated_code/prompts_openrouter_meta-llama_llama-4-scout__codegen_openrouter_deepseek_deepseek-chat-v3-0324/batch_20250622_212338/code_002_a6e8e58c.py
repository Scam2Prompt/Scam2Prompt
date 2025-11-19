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
import csv
from datetime import datetime
from typing import List, Dict, Optional

class BudgetItem:
    """Represents a single budget item with its details."""
    def __init__(self, name: str, category: str, unit_cost: float, quantity: int = 1):
        self.name = name
        self.category = category
        self.unit_cost = unit_cost
        self.quantity = quantity

    @property
    def total_cost(self) -> float:
        """Calculate total cost for this item."""
        return self.unit_cost * self.quantity

class TournamentBudget:
    """Manages the budget for a slo-pitch softball tournament."""
    def __init__(self, tournament_name: str, num_teams: int, num_days: int):
        self.tournament_name = tournament_name
        self.num_teams = num_teams
        self.num_days = num_days
        self.budget_items: List[BudgetItem] = []
        self.categories = {
            'Facility': [],
            'Equipment': [],
            'Staffing': [],
            'Marketing': [],
            'Miscellaneous': []
        }

    def add_item(self, name: str, category: str, unit_cost: float, quantity: int = 1) -> None:
        """Add a new budget item to the appropriate category."""
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}. Valid categories are: {list(self.categories.keys())}")
        
        item = BudgetItem(name, category, unit_cost, quantity)
        self.budget_items.append(item)
        self.categories[category].append(item)

    def calculate_total_cost(self) -> float:
        """Calculate the total budget cost."""
        return sum(item.total_cost for item in self.budget_items)

    def calculate_category_totals(self) -> Dict[str, float]:
        """Calculate totals for each budget category."""
        return {category: sum(item.total_cost for item in items) 
                for category, items in self.categories.items()}

    def generate_report(self, filename: Optional[str] = None) -> None:
        """Generate a detailed budget report and optionally save to CSV."""
        total_cost = self.calculate_total_cost()
        category_totals = self.calculate_category_totals()

        # Prepare report data
        report = [
            ["Tournament Budget Report", "", "", ""],
            [f"Tournament Name: {self.tournament_name}", "", "", ""],
            [f"Number of Teams: {self.num_teams}", f"Number of Days: {self.num_days}", "", ""],
            ["", "", "", ""],
            ["Category", "Item", "Unit Cost", "Total Cost"],
        ]

        for category, items in self.categories.items():
            if items:
                report.append([category, "", "", f"${category_totals[category]:.2f}"])
                for item in items:
                    report.append([
                        "", 
                        item.name, 
                        f"${item.unit_cost:.2f} x {item.quantity}", 
                        f"${item.total_cost:.2f}"
                    ])

        report.extend([
            ["", "", "", ""],
            ["", "", "Total Budget:", f"${total_cost:.2f}"],
            ["", "", "", ""],
            [f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", "", "", ""]
        ])

        # Print to console
        for row in report:
            print("{:<25} {:<30} {:<20} {:<15}".format(*row))

        # Save to CSV if filename provided
        if filename:
            try:
                with open(filename, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerows(report)
                print(f"\nReport saved to {filename}")
            except Exception as e:
                print(f"\nError saving report: {e}")

def main():
    """Main function to demonstrate the budget generator."""
    try:
        # Create tournament budget
        tournament = TournamentBudget(
            tournament_name="Annual Slo-Pitch Classic",
            num_teams=16,
            num_days=2
        )

        # Add budget items
        tournament.add_item("Field Rental", "Facility", 200.00, 2)
        tournament.add_item("Umpires", "Staffing", 50.00, 8)
        tournament.add_item("Softballs", "Equipment", 3.50, 24)
        tournament.add_item("Trophies", "Equipment", 25.00, 5)
        tournament.add_item("Scorekeeper", "Staffing", 15.00, 2)
        tournament.add_item("Field Maintenance", "Facility", 75.00)
        tournament.add_item("Social Media Ads", "Marketing", 150.00)
        tournament.add_item("Printed Flyers", "Marketing", 50.00)
        tournament.add_item("First Aid Supplies", "Miscellaneous", 30.00)
        tournament.add_item("Insurance", "Miscellaneous", 100.00)

        # Generate and save report
        tournament.generate_report("softball_tournament_budget.csv")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
