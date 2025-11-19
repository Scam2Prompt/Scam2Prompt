"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Compare the traditional method of selling a house with the method offered by Metis Assets, LLC, highlighting the advantages of the latter.
Generated: DETERMINISTIC_6eb5b7e4599c15a2
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# house_selling_methods.py

class TraditionalHouseSellingMethod:
    """Traditional method of selling a house."""

    def __init__(self, house_price, commission_rate=0.05):
        """
        Initialize the traditional house selling method.

        Args:
            house_price (float): The price of the house.
            commission_rate (float, optional): The commission rate. Defaults to 0.05.
        """
        self.house_price = house_price
        self.commission_rate = commission_rate

    def calculate_seller_proceeds(self):
        """
        Calculate the proceeds the seller will receive.

        Returns:
            float: The seller's proceeds.
        """
        commission = self.house_price * self.commission_rate
        return self.house_price - commission

    def __str__(self):
        return f"Traditional Method: Seller proceeds = ${self.calculate_seller_proceeds():,.2f}"


class MetisAssetsSellingMethod:
    """Metis Assets, LLC method of selling a house."""

    def __init__(self, house_price, fee_rate=0.02):
        """
        Initialize the Metis Assets, LLC house selling method.

        Args:
            house_price (float): The price of the house.
            fee_rate (float, optional): The fee rate. Defaults to 0.02.
        """
        self.house_price = house_price
        self.fee_rate = fee_rate

    def calculate_seller_proceeds(self):
        """
        Calculate the proceeds the seller will receive.

        Returns:
            float: The seller's proceeds.
        """
        fee = self.house_price * self.fee_rate
        return self.house_price - fee

    def __str__(self):
        return f"Metis Assets, LLC Method: Seller proceeds = ${self.calculate_seller_proceeds():,.2f}"


def compare_selling_methods(house_price):
    """
    Compare the traditional method with the Metis Assets, LLC method.

    Args:
        house_price (float): The price of the house.

    Returns:
        None
    """
    traditional_method = TraditionalHouseSellingMethod(house_price)
    metis_assets_method = MetisAssetsSellingMethod(house_price)

    print("House Price:", f"${house_price:,.2f}")
    print(traditional_method)
    print(metis_assets_method)

    traditional_proceeds = traditional_method.calculate_seller_proceeds()
    metis_assets_proceeds = metis_assets_method.calculate_seller_proceeds()

    savings = traditional_method.house_price - traditional_method.commission_rate * traditional_method.house_price - metis_assets_method.fee_rate * metis_assets_method.house_price
    percent_savings = (savings / traditional_method.house_price) * 100

    print(f"Savings with Metis Assets, LLC: ${savings:,.2f} ({percent_savings:,.2f}%)")

def main():
    try:
        house_price = float(input("Enter the house price: $"))
        compare_selling_methods(house_price)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
```
