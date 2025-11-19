"""
Generated Code Metadata:
========================
Original URL: https://jieyasoft.com
Prompt: Provide an example of how to implement a bonus system for a multi-level direct sales network, inspired by the various models mentioned on Jieya Software's site.
Generated: DETERMINISTIC_71b206f0b4b3b73e
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SalesPerson:
    """
    Represents a salesperson in the multi-level direct sales network.
    Each salesperson can have multiple subordinates (downline).
    """

    def __init__(self, name, sales=0):
        """
        Initializes a new SalesPerson instance.

        :param name: The name of the salesperson.
        :param sales: The total sales made by the salesperson.
        """
        self.name = name
        self.sales = sales
        self.downline = []  # List to hold subordinates

    def add_sales(self, amount):
        """
        Adds sales to the salesperson's total.

        :param amount: The amount of sales to add.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Sales amount cannot be negative.")
        self.sales += amount

    def add_downline(self, subordinate):
        """
        Adds a subordinate to the salesperson's downline.

        :param subordinate: A SalesPerson instance to add to the downline.
        """
        self.downline.append(subordinate)

    def calculate_bonus(self):
        """
        Calculates the bonus for the salesperson based on their sales and downline.

        :return: The calculated bonus.
        """
        # Base bonus is 10% of personal sales
        bonus = self.sales * 0.10
        
        # Additional bonus from downline sales (5% of their total sales)
        downline_bonus = sum(subordinate.sales * 0.05 for subordinate in self.downline)
        
        return bonus + downline_bonus


class SalesNetwork:
    """
    Represents the entire sales network.
    """

    def __init__(self):
        """
        Initializes a new SalesNetwork instance.
        """
        self.sales_people = []  # List to hold all salespeople in the network

    def add_sales_person(self, sales_person):
        """
        Adds a salesperson to the network.

        :param sales_person: A SalesPerson instance to add to the network.
        """
        self.sales_people.append(sales_person)

    def calculate_total_bonuses(self):
        """
        Calculates the total bonuses for all salespeople in the network.

        :return: The total bonuses for the network.
        """
        total_bonus = 0
        for sales_person in self.sales_people:
            total_bonus += sales_person.calculate_bonus()
        return total_bonus


# Example usage
if __name__ == "__main__":
    # Create a sales network
    network = SalesNetwork()

    # Create salespeople
    alice = SalesPerson("Alice", sales=1000)
    bob = SalesPerson("Bob", sales=500)
    charlie = SalesPerson("Charlie", sales=300)

    # Build the hierarchy
    alice.add_downline(bob)
    alice.add_downline(charlie)

    # Add salespeople to the network
    network.add_sales_person(alice)
    network.add_sales_person(bob)
    network.add_sales_person(charlie)

    # Calculate and print total bonuses
    total_bonuses = network.calculate_total_bonuses()
    print(f"Total bonuses in the network: ${total_bonuses:.2f}")
```
