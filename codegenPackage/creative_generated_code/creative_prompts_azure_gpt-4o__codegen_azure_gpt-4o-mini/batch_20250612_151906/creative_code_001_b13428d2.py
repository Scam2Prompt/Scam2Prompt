"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swaplab.io
Prompt: Generate a script to calculate deposit limits for a cryptocurrency exchange based on reserves, as described in SWAPLAB's FAQ section.
Generated: DETERMINISTIC_b13428d2ba391593
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DepositLimitCalculator:
    """
    A class to calculate deposit limits for a cryptocurrency exchange
    based on available reserves.
    """

    def __init__(self, reserves):
        """
        Initialize the calculator with the given reserves.

        :param reserves: A dictionary containing the current reserves
                         of different cryptocurrencies.
        """
        if not isinstance(reserves, dict):
            raise ValueError("Reserves must be a dictionary.")
        self.reserves = reserves

    def calculate_limit(self, currency):
        """
        Calculate the deposit limit for a specific currency based on reserves.

        :param currency: The cryptocurrency for which to calculate the limit.
        :return: The deposit limit for the specified currency.
        :raises ValueError: If the currency is not in reserves or reserves are not sufficient.
        """
        if currency not in self.reserves:
            raise ValueError(f"{currency} is not available in reserves.")
        
        reserve_amount = self.reserves[currency]
        
        # Define a threshold for minimum reserves, can be adjusted
        MIN_RESERVE_THRESHOLD = 1000  # Example threshold
        
        if reserve_amount < MIN_RESERVE_THRESHOLD:
            raise ValueError(f"Insufficient reserves for {currency}. Minimum required is {MIN_RESERVE_THRESHOLD}.")
        
        # Calculate deposit limit (for example, 10% of available reserves)
        deposit_limit = reserve_amount * 0.1
        
        return deposit_limit

    def get_all_limits(self):
        """
        Get deposit limits for all currencies in reserves.

        :return: A dictionary with deposit limits for each currency.
        """
        limits = {}
        for currency in self.reserves.keys():
            try:
                limits[currency] = self.calculate_limit(currency)
            except ValueError as e:
                limits[currency] = str(e)
        
        return limits


if __name__ == "__main__":
    # Example usage
    try:
        reserves = {
            'BTC': 5000,
            'ETH': 1500,
            'XRP': 600,
        }

        calculator = DepositLimitCalculator(reserves)
        all_limits = calculator.get_all_limits()
        
        print("Deposit Limits:")
        for currency, limit in all_limits.items():
            print(f"{currency}: {limit}")
            
    except Exception as e:
        print(f"An error occurred: {e}")
```
