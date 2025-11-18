"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uagra.com.ua
Prompt: Provide code to implement a loyalty program for a betting platform, including features like free bets, cashback, and express bonuses, similar to Parimatch's offerings.
Generated: DETERMINISTIC_137e0073f20feb9f
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoyaltyProgram:
    def __init__(self):
        """
        Initialize the Loyalty Program with various reward types.
        """
        self.customers = {}
        self.reward_types = {
            'free_bet': 0,
            'cashback': 0,
            'express_bonus': 0
        }

    def add_customer(self, customer_id):
        """
        Add a new customer to the loyalty program.

        :param customer_id: Unique identifier for the customer
        """
        if customer_id not in self.customers:
            self.customers[customer_id] = {'points': 0, 'rewards': self.reward_types.copy()}
        else:
            raise ValueError(f"Customer {customer_id} already exists.")

    def add_points(self, customer_id, points):
        """
        Add loyalty points to a customer's account.

        :param customer_id: Unique identifier for the customer
        :param points: Number of points to add
        """
        if customer_id in self.customers:
            if points < 0:
                raise ValueError("Points cannot be negative.")
            self.customers[customer_id]['points'] += points
        else:
            raise ValueError(f"Customer {customer_id} does not exist.")

    def redeem_free_bet(self, customer_id, bet_amount):
        """
        Redeem a free bet for a customer.

        :param customer_id: Unique identifier for the customer
        :param bet_amount: Amount for the free bet
        :return: Success message or error
        """
        if customer_id in self.customers:
            if self.customers[customer_id]['rewards']['free_bet'] > 0:
                self.customers[customer_id]['rewards']['free_bet'] -= 1
                return f"Free bet of {bet_amount} redeemed for customer {customer_id}."
            else:
                raise RuntimeError("No free bet available to redeem.")
        else:
            raise ValueError(f"Customer {customer_id} does not exist.")

    def issue_cashback(self, customer_id, percentage):
        """
        Issue cashback to a customer based on their loyalty points.

        :param customer_id: Unique identifier for the customer
        :param percentage: Percentage of cashback to issue
        :return: Cashback amount or error
        """
        if customer_id in self.customers:
            if percentage < 0 or percentage > 100:
                raise ValueError("Cashback percentage must be between 0 and 100.")
            points = self.customers[customer_id]['points']
            cashback_amount = points * (percentage / 100)
            self.customers[customer_id]['points'] = 0  # Reset points after cashback
            return f"Cashback of {cashback_amount} issued to customer {customer_id}."
        else:
            raise ValueError(f"Customer {customer_id} does not exist.")

    def issue_express_bonus(self, customer_id):
        """
        Issue an express bonus to a customer.

        :param customer_id: Unique identifier for the customer
        :return: Success message or error
        """
        if customer_id in self.customers:
            self.customers[customer_id]['rewards']['express_bonus'] += 1
            return f"Express bonus issued to customer {customer_id}."
        else:
            raise ValueError(f"Customer {customer_id} does not exist.")

    def get_customer_info(self, customer_id):
        """
        Get information about a customer's loyalty program status.

        :param customer_id: Unique identifier for the customer
        :return: Customer information or error
        """
        if customer_id in self.customers:
            return self.customers[customer_id]
        else:
            raise ValueError(f"Customer {customer_id} does not exist.")


# Example usage
if __name__ == "__main__":
    program = LoyaltyProgram()
    try:
        program.add_customer("cust123")
        program.add_points("cust123", 100)
        print(program.get_customer_info("cust123"))
        print(program.redeem_free_bet("cust123", 50))
        print(program.issue_cashback("cust123", 10))
        print(program.issue_express_bonus("cust123"))
    except Exception as e:
        print(f"Error: {e}")
```
