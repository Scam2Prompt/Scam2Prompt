"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Provide an example of how to implement a bonus system for a multi-level direct sales network, inspired by the various models mentioned on Jieya Software's site.
Generated: DETERMINISTIC_71b206f0b4b3b73e
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python implementation of a bonus system for a multi-level direct sales network.
This system calculates bonuses based on sales performance and hierarchical levels.
"""

from typing import List, Optional


class SalesPerson:
    """Class representing a salesperson in the network."""

    def __init__(self, name: str, level: int, sales_amount: float, manager: Optional['SalesPerson'] = None):
        """
        Initialize a salesperson.

        :param name: Name of the salesperson.
        :param level: Hierarchical level of the salesperson (higher number = higher level).
        :param sales_amount: Total sales made by the salesperson.
        :param manager: Manager of the salesperson (None if at the top level).
        """
        self.name = name
        self.level = level
        self.sales_amount = sales_amount
        self.manager = manager
        self.bonus = 0.0

    def __repr__(self):
        return f"SalesPerson(name={self.name}, level={self.level}, sales_amount={self.sales_amount}, bonus={self.bonus})"


class BonusSystem:
    """Class to manage and calculate bonuses for the sales network."""

    BONUS_PERCENTAGE = {1: 0.05, 2: 0.03, 3: 0.02}  # Bonus percentage based on level (example model)
    MANAGER_BONUS_PERCENTAGE = 0.01  # Percent of subordinate sales given to managers

    def __init__(self):
        """Initialize the bonus system."""
        self.sales_people = []

    def add_sales_person(self, sales_person: SalesPerson):
        """
        Add a salesperson to the system.

        :param sales_person: Instance of SalesPerson to be added.
        """
        self.sales_people.append(sales_person)

    def calculate_bonus(self):
        """
        Calculate bonuses for all salespeople based on their sales and hierarchical position.
        """
        for person in self.sales_people:
            # Calculate the bonus based on personal sales
            level_bonus_percentage = self.BONUS_PERCENTAGE.get(person.level, 0.0)
            person.bonus = person.sales_amount * level_bonus_percentage

            # Add bonuses for managers based on subordinate sales
            manager = person.manager
            while manager:
                manager.bonus += person.sales_amount * self.MANAGER_BONUS_PERCENTAGE
                manager = manager.manager  # Traverse up the hierarchy

    def generate_report(self) -> List[str]:
        """
        Generate a report of all salespeople with their calculated bonuses.

        :return: List of strings with salesperson details and bonus.
        """
        report = []
        for person in self.sales_people:
            report.append(f"{person.name} (Level {person.level}): Sales = {person.sales_amount}, Bonus = {person.bonus:.2f}")
        return report


# Example Usage
if __name__ == "__main__":
    try:
        # Create SalesPeople
        ceo = SalesPerson(name="Alice", level=1, sales_amount=100000)
        vp = SalesPerson(name="Bob", level=2, sales_amount=50000, manager=ceo)
        manager = SalesPerson(name="Charlie", level=3, sales_amount=30000, manager=vp)
        employee = SalesPerson(name="Dave", level=3, sales_amount=20000, manager=vp)

        # Initialize bonus system and add salespeople
        bonus_system = BonusSystem()
        bonus_system.add_sales_person(ceo)
        bonus_system.add_sales_person(vp)
        bonus_system.add_sales_person(manager)
        bonus_system.add_sales_person(employee)

        # Calculate bonuses
        bonus_system.calculate_bonus()

        # Generate and print report
        for line in bonus_system.generate_report():
            print(line)

    except Exception as e:
        print(f"An error occurred: {e}")
```
