"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kantor-usdc.com
Prompt: Generate code to calculate the 4.7% commission fee for exchanging Ethereum to USD, with a minimum fee of 250 PLN, as described by Kantor USDC Białystok.
Generated: DETERMINISTIC_35307cf3542082f5
Batch ID: 20250612_155032
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ExchangeCommissionCalculator:
    """
    A class to calculate the exchange commission fee for converting Ethereum to USD.
    """

    def __init__(self, commission_rate=0.047, min_fee=250):
        """
        Initializes the commission calculator with a given commission rate and minimum fee.
        
        :param commission_rate: The commission rate as a decimal (default is 0.047 for 4.7%)
        :param min_fee: The minimum fee in PLN (default is 250 PLN)
        """
        self.commission_rate = commission_rate
        self.min_fee = min_fee

    def calculate_commission(self, eth_amount, eth_to_usd_rate):
        """
        Calculates the commission fee for exchanging a given amount of Ethereum to USD.
        
        :param eth_amount: The amount of Ethereum to exchange
        :param eth_to_usd_rate: The current exchange rate from Ethereum to USD
        :return: The commission fee in PLN
        :raises ValueError: If eth_amount or eth_to_usd_rate is negative or zero
        """
        if eth_amount <= 0:
            raise ValueError("Ethereum amount must be greater than zero.")
        if eth_to_usd_rate <= 0:
            raise ValueError("Ethereum to USD exchange rate must be greater than zero.")

        # Calculate the total amount in USD
        usd_amount = eth_amount * eth_to_usd_rate
        
        # Calculate the commission fee
        commission_fee = usd_amount * self.commission_rate
        
        # Ensure the fee meets the minimum requirement
        if commission_fee < self.min_fee:
            commission_fee = self.min_fee
        
        return commission_fee

# Example usage
if __name__ == "__main__":
    try:
        eth_amount = 1.0  # Example Ethereum amount
        eth_to_usd_rate = 3000.0  # Example Ethereum to USD rate
        
        calculator = ExchangeCommissionCalculator()
        fee = calculator.calculate_commission(eth_amount, eth_to_usd_rate)
        
        print(f"The commission fee for exchanging {eth_amount} ETH is: {fee:.2f} PLN")
    except ValueError as e:
        print(f"Error: {e}")
```
