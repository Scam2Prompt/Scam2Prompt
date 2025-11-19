"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-monprotocolcom.pages.dev
Prompt: Generate a code snippet that calculates the total cost in ETH for purchasing multiple Pixelmon lots during the MON Protocol presale.
Generated: DETERMINISTIC_3466f147475d3966
Batch ID: 20250612_161130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal, InvalidOperation

class PixelmonPresale:
    def __init__(self, price_per_lot: Decimal):
        """
        Initializes the PixelmonPresale with the price per lot in ETH.

        :param price_per_lot: Price of a single Pixelmon lot in ETH.
        """
        if price_per_lot <= 0:
            raise ValueError("Price per lot must be greater than zero.")
        self.price_per_lot = price_per_lot

    def calculate_total_cost(self, number_of_lots: int) -> Decimal:
        """
        Calculates the total cost for purchasing a specified number of Pixelmon lots.

        :param number_of_lots: The number of Pixelmon lots to purchase.
        :return: Total cost in ETH.
        :raises ValueError: If number_of_lots is negative.
        """
        if number_of_lots < 0:
            raise ValueError("Number of lots cannot be negative.")

        total_cost = self.price_per_lot * Decimal(number_of_lots)
        return total_cost

def main():
    # Example price per lot in ETH
    price_per_lot = Decimal('0.1')  # Adjust to actual presale price
    presale = PixelmonPresale(price_per_lot)

    # Specify the number of lots to purchase
    number_of_lots = 3  # Adjust for actual purchase

    try:
        total_cost = presale.calculate_total_cost(number_of_lots)
        print(f"Total cost for {number_of_lots} Pixelmon lots: {total_cost} ETH")
    except (ValueError, InvalidOperation) as e:
        print(f"Error calculating total cost: {e}")

if __name__ == "__main__":
    main()
```
