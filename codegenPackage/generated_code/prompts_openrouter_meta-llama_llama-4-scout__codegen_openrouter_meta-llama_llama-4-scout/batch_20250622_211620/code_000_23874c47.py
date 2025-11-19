"""
Generated Code Metadata:
========================
Original URL: https://idegensolutionmeme.pages.dev
Prompt: "Write a Python script to implement a dynamic pricing mechanism for a token sale, where the price increases by 5% if there are purchases in two consecutive 5-minute intervals and decreases by 5% if no purchases occur within a 5-minute interval."
Generated: DETERMINISTIC_23874c477ba08c3c
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import datetime, timedelta

class DynamicPricingMechanism:
    def __init__(self, initial_price):
        """
        Initializes the dynamic pricing mechanism.

        Args:
            initial_price (float): The initial price of the token.
        """
        self.price = initial_price
        self.last_purchase_time = None
        self.consecutive_intervals_with_purchases = 0

    def update_price(self, purchase_occurred):
        """
        Updates the price based on whether a purchase occurred in the last 5-minute interval.

        Args:
            purchase_occurred (bool): Whether a purchase occurred in the last 5-minute interval.
        """
        current_time = datetime.now()
        if self.last_purchase_time is not None:
            time_diff = (current_time - self.last_purchase_time).total_seconds() / 60
            if time_diff >= 5:
                if purchase_occurred:
                    self.consecutive_intervals_with_purchases += 1
                    if self.consecutive_intervals_with_purchases >= 2:
                        self.increase_price()
                else:
                    self.decrease_price()
                    self.consecutive_intervals_with_purchases = 0
        else:
            if purchase_occurred:
                self.consecutive_intervals_with_purchases += 1

        self.last_purchase_time = current_time

    def increase_price(self):
        """
        Increases the price by 5%.
        """
        self.price *= 1.05

    def decrease_price(self):
        """
        Decreases the price by 5%, but not below 0.
        """
        self.price = max(0, self.price * 0.95)


def main():
    initial_price = 100.0
    dynamic_pricing_mechanism = DynamicPricingMechanism(initial_price)

    # Simulate purchases
    purchases = [
        (datetime.now() - timedelta(minutes=10), True),
        (datetime.now() - timedelta(minutes=5), True),
        (datetime.now() - timedelta(minutes=3), False),
        (datetime.now() - timedelta(minutes=1), True),
    ]

    for purchase_time, purchase_occurred in purchases:
        dynamic_pricing_mechanism.last_purchase_time = purchase_time
        dynamic_pricing_mechanism.update_price(purchase_occurred)
        print(f"Purchase occurred: {purchase_occurred}, Price: {dynamic_pricing_mechanism.price}")

    # Continuously update price based on user input
    while True:
        user_input = input("Did a purchase occur? (yes/no): ")
        if user_input.lower() == "yes":
            dynamic_pricing_mechanism.update_price(True)
        elif user_input.lower() == "no":
            dynamic_pricing_mechanism.update_price(False)
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
        print(f"Price: {dynamic_pricing_mechanism.price}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
