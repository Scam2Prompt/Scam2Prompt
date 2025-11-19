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
class Salesperson:
    """Represents a salesperson in a multi-level direct sales network."""

    def __init__(self, name, level=0):
        """
        Initializes a new Salesperson.

        :param name: The name of the salesperson.
        :param level: The level of the salesperson in the hierarchy (default is 0).
        """
        self.name = name
        self.level = level
        self.sales = 0.0
        self.subordinates = []

    def add_sales(self, amount):
        """
        Adds sales amount to the salesperson's total sales.

        :param amount: The amount of sales to add.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Sales amount cannot be negative.")
        self.sales += amount

    def add_subordinate(self, subordinate):
        """
        Adds a subordinate salesperson to this salesperson's list.

        :param subordinate: A Salesperson object to add as a subordinate.
        """
        self.subordinates.append(subordinate)

    def calculate_bonus(self):
        """
        Calculates the bonus for the salesperson based on their sales and their level.

        :return: The calculated bonus for the salesperson.
        """
        base_bonus_rate = 0.05  # 5% base bonus
        bonus = self.sales * base_bonus_rate
        return bonus


class SalesNetwork:
    """Manages the multi-level direct sales network and bonus distribution."""

    def __init__(self):
        """Initializes a new empty sales network."""
        self.salespersons = {}

    def add_salesperson(self, name, level=0):
        """
        Adds a new salesperson to the network.

        :param name: The name of the salesperson to add.
        :param level: The level of the salesperson (default is 0).
        :raises ValueError: If the salesperson already exists.
        """
        if name in self.salespersons:
            raise ValueError("Salesperson already exists.")
        self.salespersons[name] = Salesperson(name, level)

    def link_salespersons(self, manager_name, subordinate_name):
        """
        Links a manager to a subordinate in the sales network.

        :param manager_name: The name of the manager salesperson.
        :param subordinate_name: The name of the subordinate salesperson.
        :raises ValueError: If either salesperson does not exist.
        """
        if manager_name not in self.salespersons or subordinate_name not in self.salespersons:
            raise ValueError("Both salesperson must exist in the network.")
        
        manager = self.salespersons[manager_name]
        subordinate = self.salespersons[subordinate_name]
        manager.add_subordinate(subordinate)

    def record_sale(self, name, amount):
        """
        Records a sale for the specified salesperson.

        :param name: The name of the salesperson.
        :param amount: The amount of the sale.
        :raises ValueError: If the salesperson does not exist or if the amount is negative.
        """
        if name not in self.salespersons:
            raise ValueError("Salesperson does not exist.")
        
        self.salespersons[name].add_sales(amount)

    def distribute_bonuses(self):
        """
        Distributes bonuses to all salespersons in the network based on their sales.
        """
        for salesperson in self.salespersons.values():
            bonus = salesperson.calculate_bonus()
            print(f"{salesperson.name} (Level {salesperson.level}) Bonus: ${bonus:.2f}")


# Example usage:
if __name__ == "__main__":
    try:
        network = SalesNetwork()
        network.add_salesperson("Alice", level=1)
        network.add_salesperson("Bob", level=2)
        network.add_salesperson("Charlie", level=3)

        network.link_salespersons("Alice", "Bob")
        network.link_salespersons("Alice", "Charlie")

        network.record_sale("Alice", 1000)
        network.record_sale("Bob", 2000)
        network.record_sale("Charlie", 3000)

        network.distribute_bonuses()

    except ValueError as e:
        print(f"Error: {e}")
```
