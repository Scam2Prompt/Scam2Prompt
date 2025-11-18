"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-heist-nana.web.app
Prompt: Create a function to calculate the total price of a transaction using Helio's payment system and display a disclaimer about the irreversibility of DeFi payments.
Generated: DETERMINISTIC_a91e1144a1d158ad
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HelioPaymentSystem:
    """
    A class to represent the Helio payment system.
    """

    def __init__(self, transaction_fee_percentage=0.02):
        """
        Initializes the HelioPaymentSystem with a given transaction fee percentage.

        Args:
            transaction_fee_percentage (float): The percentage fee charged on the transaction.
        """
        self.transaction_fee_percentage = transaction_fee_percentage

    def calculate_total_price(self, item_price, quantity):
        """
        Calculates the total price of a transaction including transaction fees.

        Args:
            item_price (float): The price of a single item.
            quantity (int): The number of items being purchased.

        Returns:
            float: The total price including fees.

        Raises:
            ValueError: If item_price or quantity is negative.
        """
        if item_price < 0 or quantity < 0:
            raise ValueError("Item price and quantity must be non-negative.")

        # Calculate total price before fees
        subtotal = item_price * quantity
        
        # Calculate transaction fee
        fee = subtotal * self.transaction_fee_percentage
        
        # Calculate total price
        total_price = subtotal + fee
        
        return total_price

    def display_disclaimer(self):
        """
        Displays a disclaimer about the irreversibility of DeFi payments.
        """
        disclaimer = (
            "Disclaimer: All payments made through the Helio payment system are "
            "irreversible. Please ensure that your transaction details are correct before proceeding."
        )
        print(disclaimer)


def main():
    """
    Main function to execute the payment calculation and display the disclaimer.
    """
    try:
        helio_payment = HelioPaymentSystem()
        
        item_price = float(input("Enter the price of the item: "))
        quantity = int(input("Enter the quantity of items: "))
        
        total_price = helio_payment.calculate_total_price(item_price, quantity)
        print(f"Total price including fees: ${total_price:.2f}")
        
        helio_payment.display_disclaimer()
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
