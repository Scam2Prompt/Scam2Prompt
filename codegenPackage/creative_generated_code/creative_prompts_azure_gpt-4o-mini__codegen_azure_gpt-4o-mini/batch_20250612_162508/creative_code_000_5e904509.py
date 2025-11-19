"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedefi-mantanetwork.pages.dev
Prompt: Write a code snippet to calculate the Total Value Locked (TVL) for Manta CeDeFi using BTC, ETH, USDT, and USDC contributions.
Generated: DETERMINISTIC_5e904509520d6c98
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MantaCeDeFiTVLCalculator:
    """
    A class to calculate the Total Value Locked (TVL) for Manta CeDeFi.
    
    Attributes:
        btc_amount (float): Amount of Bitcoin (BTC) contributed.
        eth_amount (float): Amount of Ethereum (ETH) contributed.
        usdt_amount (float): Amount of Tether (USDT) contributed.
        usdc_amount (float): Amount of USD Coin (USDC) contributed.
        btc_price (float): Current price of Bitcoin in USD.
        eth_price (float): Current price of Ethereum in USD.
        usdt_price (float): Current price of Tether in USD.
        usdc_price (float): Current price of USD Coin in USD.
    """
    
    def __init__(self, btc_amount, eth_amount, usdt_amount, usdc_amount, btc_price, eth_price, usdt_price, usdc_price):
        """Initialize the TVL calculator with amounts and prices."""
        self.btc_amount = btc_amount
        self.eth_amount = eth_amount
        self.usdt_amount = usdt_amount
        self.usdc_amount = usdc_amount
        self.btc_price = btc_price
        self.eth_price = eth_price
        self.usdt_price = usdt_price
        self.usdc_price = usdc_price

    def calculate_tvl(self):
        """Calculate the Total Value Locked (TVL) in USD.

        Returns:
            float: The total value locked in USD.
        """
        try:
            # Calculate the value for each asset
            btc_value = self.btc_amount * self.btc_price
            eth_value = self.eth_amount * self.eth_price
            usdt_value = self.usdt_amount * self.usdt_price
            usdc_value = self.usdc_amount * self.usdc_price

            # Sum all values to get the total value locked
            total_value_locked = btc_value + eth_value + usdt_value + usdc_value
            
            return total_value_locked
        
        except Exception as e:
            print(f"Error calculating TVL: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Define contributions and current prices
    btc_contribution = 1.5  # 1.5 BTC
    eth_contribution = 2.0   # 2.0 ETH
    usdt_contribution = 3000.0  # 3000 USDT
    usdc_contribution = 2500.0   # 2500 USDC

    # Simulated current prices (in USD)
    btc_price = 40000.0
    eth_price = 2500.0
    usdt_price = 1.0
    usdc_price = 1.0

    # Create a TVL calculator instance
    tvl_calculator = MantaCeDeFiTVLCalculator(btc_contribution, eth_contribution, usdt_contribution, usdc_contribution, btc_price, eth_price, usdt_price, usdc_price)

    # Calculate and print the Total Value Locked
    total_value_locked = tvl_calculator.calculate_tvl()
    if total_value_locked is not None:
        print(f"Total Value Locked (TVL) in USD: ${total_value_locked:.2f}")
```
