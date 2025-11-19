"""
Generated Code Metadata:
========================
Original URL: https://immediate-helix.com
Prompt: Write Python code to simulate the calculation of realized and unrealized losses based on Immediate Helix V9’s definitions. Include functionality to input asset purchase price, current price, and sale price.
Generated: DETERMINISTIC_13b7707c3c1b89f0
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HelixLossCalculator:
    """
    Calculates realized and unrealized losses based on Immediate Helix V9's definitions.
    """

    def __init__(self, purchase_price, current_price, sale_price=None):
        """
        Initializes the calculator with asset prices.

        Args:
            purchase_price (float): The price at which the asset was purchased.
            current_price (float): The current market price of the asset.
            sale_price (float, optional): The price at which the asset was sold. Defaults to None.
        """
        self.purchase_price = purchase_price
        self.current_price = current_price
        self.sale_price = sale_price

    def calculate_unrealized_loss(self):
        """
        Calculates the unrealized loss based on the purchase and current prices.

        Returns:
            float: The unrealized loss.
        """
        if self.purchase_price <= 0 or self.current_price <= 0:
            raise ValueError("Purchase and current prices must be greater than zero.")
        unrealized_loss = max(0, self.purchase_price - self.current_price)
        return unrealized_loss

    def calculate_realized_loss(self):
        """
        Calculates the realized loss based on the purchase and sale prices.

        Returns:
            float: The realized loss.

        Raises:
            ValueError: If sale price is not provided or if purchase and sale prices are not valid.
        """
        if self.sale_price is None:
            raise ValueError("Sale price must be provided to calculate realized loss.")
        if self.purchase_price <= 0 or self.sale_price <= 0:
            raise ValueError("Purchase and sale prices must be greater than zero.")
        realized_loss = max(0, self.purchase_price - self.sale_price)
        return realized_loss

    def calculate_both(self):
        """
        Calculates both unrealized and realized losses.

        Returns:
            dict: A dictionary containing unrealized and realized losses.
        """
        unrealized_loss = self.calculate_unrealized_loss()
        realized_loss = 0
        if self.sale_price is not None:
            realized_loss = self.calculate_realized_loss()
        return {
            "unrealized_loss": unrealized_loss,
            "realized_loss": realized_loss
        }


def main():
    try:
        purchase_price = float(input("Enter the asset purchase price: "))
        current_price = float(input("Enter the asset current price: "))
        sale_price_input = input("Enter the asset sale price (or leave blank if not sold): ")
        sale_price = float(sale_price_input) if sale_price_input else None

        calculator = HelixLossCalculator(purchase_price, current_price, sale_price)

        if sale_price is not None:
            unrealized_loss = calculator.calculate_unrealized_loss()
            realized_loss = calculator.calculate_realized_loss()
            print(f"Unrealized Loss: {unrealized_loss}")
            print(f"Realized Loss: {realized_loss}")
        else:
            losses = calculator.calculate_both()
            print(f"Unrealized Loss: {losses['unrealized_loss']}")
            print(f"Realized Loss: {losses['realized_loss']}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
