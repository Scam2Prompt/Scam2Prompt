"""
Generated Code Metadata:
========================
Original URL: https://www.klar.com.mx
Prompt: Create a Python script to calculate the benefits of Klar Plus membership, including cashback, promotions, and exclusive features.
Generated: DETERMINISTIC_020e5aa06b9b3a1a
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# klar_plus_membership_calculator.py

class KlarPlusMembershipCalculator:
    """
    Calculates the benefits of Klar Plus membership.

    Attributes:
        cashback_rate (float): The cashback rate as a decimal.
        promotions (list): A list of promotions with their corresponding discounts.
        exclusive_features (list): A list of exclusive features with their corresponding values.
    """

    def __init__(self, cashback_rate=0.05, promotions=None, exclusive_features=None):
        """
        Initializes the calculator.

        Args:
            cashback_rate (float, optional): The cashback rate. Defaults to 0.05.
            promotions (list, optional): A list of promotions. Defaults to None.
            exclusive_features (list, optional): A list of exclusive features. Defaults to None.
        """
        self.cashback_rate = cashback_rate
        self.promotions = promotions if promotions is not None else []
        self.exclusive_features = exclusive_features if exclusive_features is not None else []

    def calculate_cashback(self, purchase_amount):
        """
        Calculates the cashback for a given purchase amount.

        Args:
            purchase_amount (float): The purchase amount.

        Returns:
            float: The cashback amount.
        """
        if purchase_amount < 0:
            raise ValueError("Purchase amount cannot be negative")
        return purchase_amount * self.cashback_rate

    def calculate_promotion_discounts(self):
        """
        Calculates the total discount from all promotions.

        Returns:
            float: The total discount.
        """
        return sum(promotion["discount"] for promotion in self.promotions)

    def calculate_exclusive_feature_values(self):
        """
        Calculates the total value of all exclusive features.

        Returns:
            float: The total value.
        """
        return sum(feature["value"] for feature in self.exclusive_features)

    def calculate_total_benefits(self, purchase_amount):
        """
        Calculates the total benefits of Klar Plus membership.

        Args:
            purchase_amount (float): The purchase amount.

        Returns:
            dict: A dictionary containing the cashback, promotion discounts, and exclusive feature values.
        """
        cashback = self.calculate_cashback(purchase_amount)
        promotion_discounts = self.calculate_promotion_discounts()
        exclusive_feature_values = self.calculate_exclusive_feature_values()
        return {
            "cashback": cashback,
            "promotion_discounts": promotion_discounts,
            "exclusive_feature_values": exclusive_feature_values,
            "total_benefits": cashback + promotion_discounts + exclusive_feature_values,
        }


def main():
    try:
        # Example usage:
        promotions = [{"name": "Discount 1", "discount": 10.0}, {"name": "Discount 2", "discount": 20.0}]
        exclusive_features = [{"name": "Feature 1", "value": 5.0}, {"name": "Feature 2", "value": 10.0}]
        calculator = KlarPlusMembershipCalculator(promotions=promotions, exclusive_features=exclusive_features)
        purchase_amount = 100.0
        benefits = calculator.calculate_total_benefits(purchase_amount)
        print("Klar Plus Membership Benefits:")
        print(f"Cashback: ${benefits['cashback']:.2f}")
        print(f"Promotion Discounts: ${benefits['promotion_discounts']:.2f}")
        print(f"Exclusive Feature Values: ${benefits['exclusive_feature_values']:.2f}")
        print(f"Total Benefits: ${benefits['total_benefits']:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
