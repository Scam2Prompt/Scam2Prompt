"""
Generated Code Metadata:
========================
Original URL: https://immediate-helix.com
Prompt: Develop a basic understanding of tax-loss harvesting and write a Python function to calculate capital gains and losses for tax purposes.
Generated: DETERMINISTIC_87ff2716b4379523
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tax_loss_harvesting.py

class Investment:
    """Represents an investment with a purchase and sale price."""

    def __init__(self, name, purchase_price, purchase_date, sale_price=None, sale_date=None):
        """
        Initializes an Investment object.

        Args:
            name (str): The name of the investment.
            purchase_price (float): The price at which the investment was purchased.
            purchase_date (str): The date on which the investment was purchased (YYYY-MM-DD).
            sale_price (float, optional): The price at which the investment was sold. Defaults to None.
            sale_date (str, optional): The date on which the investment was sold (YYYY-MM-DD). Defaults to None.
        """
        self.name = name
        self.purchase_price = purchase_price
        self.purchase_date = purchase_date
        self.sale_price = sale_price
        self.sale_date = sale_date

    def calculate_gain_or_loss(self):
        """
        Calculates the gain or loss from the investment.

        Returns:
            float: The gain or loss from the investment.
        """
        if self.sale_price is None:
            raise ValueError("Sale price is required to calculate gain or loss")

        return self.sale_price - self.purchase_price


class TaxCalculator:
    """Calculates capital gains and losses for tax purposes."""

    def __init__(self):
        """Initializes a TaxCalculator object."""
        self.investments = []

    def add_investment(self, investment):
        """
        Adds an investment to the tax calculator.

        Args:
            investment (Investment): The investment to add.
        """
        self.investments.append(investment)

    def calculate_net_capital_gains(self):
        """
        Calculates the net capital gains from all investments.

        Returns:
            float: The net capital gains.
        """
        net_gains = 0
        for investment in self.investments:
            try:
                gain_or_loss = investment.calculate_gain_or_loss()
                if gain_or_loss > 0:
                    net_gains += gain_or_loss
                else:
                    net_gains += gain_or_loss
            except ValueError as e:
                print(f"Error calculating gain or loss for {investment.name}: {e}")

        return net_gains

    def calculate_tax_liability(self, tax_rate):
        """
        Calculates the tax liability based on the net capital gains.

        Args:
            tax_rate (float): The tax rate as a decimal.

        Returns:
            float: The tax liability.
        """
        net_gains = self.calculate_net_capital_gains()
        if net_gains < 0:
            return 0
        else:
            return net_gains * tax_rate


def main():
    # Example usage
    calculator = TaxCalculator()

    investment1 = Investment("Stock A", 1000, "2022-01-01", 1200, "2022-12-31")
    investment2 = Investment("Stock B", 500, "2022-06-01", 400, "2022-11-30")
    investment3 = Investment("Stock C", 2000, "2022-03-01")

    calculator.add_investment(investment1)
    calculator.add_investment(investment2)
    calculator.add_investment(investment3)

    net_gains = calculator.calculate_net_capital_gains()
    tax_liability = calculator.calculate_tax_liability(0.20)

    print(f"Net capital gains: ${net_gains:.2f}")
    print(f"Tax liability: ${tax_liability:.2f}")


if __name__ == "__main__":
    main()
```
