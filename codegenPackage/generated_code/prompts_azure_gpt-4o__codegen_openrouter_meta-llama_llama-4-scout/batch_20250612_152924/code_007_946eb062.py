"""
Generated Code Metadata:
========================
Original URL: https://pharmachoicecanada.ca
Prompt: Develop a script to calculate the financial benefits of joining a member-owned pharmacy cooperative, including profit sharing and purchasing power, as outlined by PharmaChoice Canada.
Generated: DETERMINISTIC_946eb06208266fff
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pharma_choice_calculator.py

class PharmaChoiceCalculator:
    """
    Calculates the financial benefits of joining a member-owned pharmacy cooperative.

    Attributes:
        annual_purchases (float): The total annual purchases made by the pharmacy.
        profit_sharing_rate (float): The profit sharing rate of the cooperative.
        purchasing_power_discount (float): The discount rate offered by the cooperative.
    """

    def __init__(self, annual_purchases, profit_sharing_rate, purchasing_power_discount):
        """
        Initializes a PharmaChoiceCalculator instance.

        Args:
            annual_purchases (float): The total annual purchases made by the pharmacy.
            profit_sharing_rate (float): The profit sharing rate of the cooperative.
            purchasing_power_discount (float): The discount rate offered by the cooperative.

        Raises:
            ValueError: If annual_purchases, profit_sharing_rate, or purchasing_power_discount is negative.
        """
        if annual_purchases < 0 or profit_sharing_rate < 0 or purchasing_power_discount < 0:
            raise ValueError("Annual purchases, profit sharing rate, and purchasing power discount must be non-negative.")

        self.annual_purchases = annual_purchases
        self.profit_sharing_rate = profit_sharing_rate / 100  # Convert to decimal
        self.purchasing_power_discount = purchasing_power_discount / 100  # Convert to decimal

    def calculate_profit_sharing(self):
        """
        Calculates the profit sharing benefit.

        Returns:
            float: The profit sharing benefit.
        """
        return self.annual_purchases * self.profit_sharing_rate

    def calculate_purchasing_power_savings(self):
        """
        Calculates the purchasing power savings.

        Returns:
            float: The purchasing power savings.
        """
        return self.annual_purchases * self.purchasing_power_discount

    def calculate_total_benefits(self):
        """
        Calculates the total financial benefits.

        Returns:
            float: The total financial benefits.
        """
        return self.calculate_profit_sharing() + self.calculate_purchasing_power_savings()


def main():
    try:
        annual_purchases = float(input("Enter the total annual purchases: $"))
        profit_sharing_rate = float(input("Enter the profit sharing rate (%): "))
        purchasing_power_discount = float(input("Enter the purchasing power discount (%): "))

        calculator = PharmaChoiceCalculator(annual_purchases, profit_sharing_rate, purchasing_power_discount)

        print("\nFinancial Benefits:")
        print(f"Profit Sharing: ${calculator.calculate_profit_sharing():.2f}")
        print(f"Purchasing Power Savings: ${calculator.calculate_purchasing_power_savings():.2f}")
        print(f"Total Benefits: ${calculator.calculate_total_benefits():.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
