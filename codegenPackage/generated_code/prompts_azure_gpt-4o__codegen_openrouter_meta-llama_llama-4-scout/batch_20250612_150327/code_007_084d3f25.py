"""
Generated Code Metadata:
========================
Original URL: https://ethereum-mixer.io
Prompt: Create a script to calculate the maximum amount of Ethereum (up to 450 ETH) that can be mixed in a single transaction, factoring in the fixed fee and gas costs.
Generated: DETERMINISTIC_084d3f252ef57f72
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Ethereum Transaction Calculator

Calculates the maximum amount of Ethereum that can be mixed in a single transaction,
considering the fixed fee and gas costs.

Usage:
    python ethereum_calculator.py
"""

import math

class EthereumCalculator:
    def __init__(self, 
                 fixed_fee_wei: int = 21000 * 20,  # 21000 gas * 20 Gwei/ gas
                 gas_price_gwei: int = 20, 
                 max_eth: float = 450, 
                 eth_to_wei: int = 10**18):
        """
        Initializes the EthereumCalculator.

        Args:
        - fixed_fee_wei (int): The fixed fee in Wei. Defaults to 21000 gas * 20 Gwei/gas.
        - gas_price_gwei (int): The gas price in Gwei. Defaults to 20.
        - max_eth (float): The maximum amount of Ethereum in ETH. Defaults to 450.
        - eth_to_wei (int): The conversion rate from ETH to Wei. Defaults to 10^18.
        """
        self.fixed_fee_wei = fixed_fee_wei
        self.gas_price_gwei = gas_price_gwei
        self.max_eth = max_eth
        self.eth_to_wei = eth_to_wei

    def calculate_max_eth(self, 
                          gas_limit: int = 21000) -> float:
        """
        Calculates the maximum amount of Ethereum that can be mixed in a single transaction.

        Args:
        - gas_limit (int): The gas limit. Defaults to 21000.

        Returns:
        - float: The maximum amount of Ethereum in ETH.
        """
        # Calculate the total gas cost in Wei
        gas_cost_wei = gas_limit * self.gas_price_gwei * 10**9
        
        # Calculate the total cost in Wei (fixed fee + gas cost)
        total_cost_wei = self.fixed_fee_wei + gas_cost_wei
        
        # Convert the total cost from Wei to ETH
        total_cost_eth = total_cost_wei / self.eth_to_wei
        
        # Calculate the maximum amount of Ethereum that can be mixed
        max_mixable_eth = self.max_eth - total_cost_eth
        
        # Ensure the result is not negative
        if max_mixable_eth < 0:
            raise ValueError("The maximum mixable Ethereum is negative.")
        
        return max_mixable_eth


def main():
    try:
        calculator = EthereumCalculator()
        max_eth = calculator.calculate_max_eth()
        print(f"The maximum amount of Ethereum that can be mixed in a single transaction is: {max_eth:.2f} ETH")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
