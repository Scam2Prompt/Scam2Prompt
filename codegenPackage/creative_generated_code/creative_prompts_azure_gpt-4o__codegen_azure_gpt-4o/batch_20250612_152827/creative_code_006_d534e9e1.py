"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://newmoly.pages.dev
Prompt: Generate code to simulate buying and selling $Molly tokens on the Molly Gateway with a fee calculation of ~0%.
Generated: DETERMINISTIC_d534e9e106d09f27
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

class MollyGateway:
    def __init__(self, fee_percentage=0.0):
        """
        Initializes the MollyGateway with a fee percentage.

        Args:
            fee_percentage (float): The transaction fee percentage (default is 0%).
        """
        self.fee_percentage = decimal.Decimal(fee_percentage) / 100

    def calculate_fee(self, amount):
        """
        Calculates the transaction fee based on the fee percentage.

        Args:
            amount (Decimal): The amount of tokens being transacted.

        Returns:
            Decimal: The transaction fee.
        """
        return amount * self.fee_percentage

    def buy_tokens(self, amount):
        """
        Simulates buying Molly tokens.

        Args:
            amount (Decimal): The amount of tokens to buy.

        Returns:
            Decimal: The net amount of tokens bought after fees.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        fee = self.calculate_fee(amount)
        net_amount = amount - fee
        return net_amount

    def sell_tokens(self, amount):
        """
        Simulates selling Molly tokens.

        Args:
            amount (Decimal): The amount of tokens to sell.

        Returns:
            Decimal: The net amount received after fees.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        fee = self.calculate_fee(amount)
        net_amount = amount - fee
        return net_amount


def main():
    """
    Main function to demonstrate buying and selling Molly tokens.
    """
    try:
        # Simulate Molly Gateway with 0% fee
        gateway = MollyGateway(fee_percentage=0.0)

        # Example transaction amounts
        buy_amount = decimal.Decimal("100.0")  # Example buy amount in tokens
        sell_amount = decimal.Decimal("50.0")  # Example sell amount in tokens

        # Simulate buying tokens
        print("Simulating buying tokens...")
        net_buy = gateway.buy_tokens(buy_amount)
        print(f"Buy Amount: {buy_amount} $Molly")
        print(f"Net Tokens Received (after fees): {net_buy} $Molly")

        # Simulate selling tokens
        print("\nSimulating selling tokens...")
        net_sell = gateway.sell_tokens(sell_amount)
        print(f"Sell Amount: {sell_amount} $Molly")
        print(f"Net Amount Received (after fees): {net_sell} $Molly")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


if __name__ == "__main__":
    # Ensure consistent decimal precision throughout
    decimal.getcontext().prec = 28  
    main()
```
