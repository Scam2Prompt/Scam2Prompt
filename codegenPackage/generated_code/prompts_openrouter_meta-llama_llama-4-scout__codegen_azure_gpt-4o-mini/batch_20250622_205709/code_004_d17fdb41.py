"""
Generated Code Metadata:
========================
Original URL: https://ethreum.ru
Prompt: Develop a system for implementing various bonuses and loyalty programs, like the ones offered by Казино Р7, using a programming language of your choice.
Generated: DETERMINISTIC_d17fdb4141c1e79f
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LoyaltyProgram:
    """
    A class to represent a loyalty program for a casino.
    """

    def __init__(self, name, bonus_percentage):
        """
        Initializes the loyalty program with a name and bonus percentage.

        :param name: str - The name of the loyalty program
        :param bonus_percentage: float - The percentage of bonus awarded
        """
        self.name = name
        self.bonus_percentage = bonus_percentage
        self.customers = {}

    def add_customer(self, customer_id):
        """
        Adds a new customer to the loyalty program.

        :param customer_id: str - Unique identifier for the customer
        """
        if customer_id in self.customers:
            raise ValueError(f"Customer {customer_id} already exists.")
        self.customers[customer_id] = 0.0  # Initialize loyalty points

    def record_transaction(self, customer_id, amount):
        """
        Records a transaction for a customer and awards loyalty points.

        :param customer_id: str - Unique identifier for the customer
        :param amount: float - The amount of the transaction
        """
        if customer_id not in self.customers:
            raise ValueError(f"Customer {customer_id} not found.")
        if amount < 0:
            raise ValueError("Transaction amount must be positive.")

        # Calculate loyalty points based on the transaction amount
        points_awarded = amount * (self.bonus_percentage / 100)
        self.customers[customer_id] += points_awarded

    def get_loyalty_points(self, customer_id):
        """
        Retrieves the total loyalty points for a customer.

        :param customer_id: str - Unique identifier for the customer
        :return: float - Total loyalty points
        """
        if customer_id not in self.customers:
            raise ValueError(f"Customer {customer_id} not found.")
        return self.customers[customer_id]

    def redeem_points(self, customer_id, points):
        """
        Redeems loyalty points for a customer.

        :param customer_id: str - Unique identifier for the customer
        :param points: float - Number of points to redeem
        """
        if customer_id not in self.customers:
            raise ValueError(f"Customer {customer_id} not found.")
        if points < 0:
            raise ValueError("Points to redeem must be positive.")
        if points > self.customers[customer_id]:
            raise ValueError("Insufficient loyalty points.")

        self.customers[customer_id] -= points  # Deduct redeemed points

# Example usage
if __name__ == "__main__":
    try:
        loyalty_program = LoyaltyProgram("Casino Rewards", 10.0)  # 10% bonus
        loyalty_program.add_customer("customer_1")
        loyalty_program.record_transaction("customer_1", 100.0)  # $100 transaction
        print(f"Loyalty Points for customer_1: {loyalty_program.get_loyalty_points('customer_1')}")
        loyalty_program.redeem_points("customer_1", 5.0)  # Redeem 5 points
        print(f"Loyalty Points after redemption for customer_1: {loyalty_program.get_loyalty_points('customer_1')}")
    except ValueError as e:
        print(f"Error: {e}")
```
