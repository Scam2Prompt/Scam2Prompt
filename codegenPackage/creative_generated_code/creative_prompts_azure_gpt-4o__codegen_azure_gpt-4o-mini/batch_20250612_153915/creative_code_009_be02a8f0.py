"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum.iceiy.com
Prompt: Generate a script to calculate the cost savings of using Arbitrum compared to Ethereum Layer 1 for transactions.
Generated: DETERMINISTIC_be02a8f0a3334d63
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class LayerCostCalculator:
    """
    A class to calculate transaction cost savings when using Arbitrum compared to Ethereum Layer 1.
    """

    def __init__(self, eth_gas_price: float, arb_gas_price: float, num_transactions: int):
        """
        Initializes the LayerCostCalculator with gas prices and number of transactions.

        Args:
            eth_gas_price (float): Gas price for Ethereum Layer 1 in Gwei.
            arb_gas_price (float): Gas price for Arbitrum in Gwei.
            num_transactions (int): Number of transactions to calculate savings for.
        """
        self.eth_gas_price = eth_gas_price
        self.arb_gas_price = arb_gas_price
        self.num_transactions = num_transactions

    def calculate_cost(self, gas_price: float, gas_limit: int) -> float:
        """
        Calculates the total cost of transactions given gas price and gas limit.

        Args:
            gas_price (float): Gas price in Gwei.
            gas_limit (int): Gas limit per transaction.

        Returns:
            float: Total cost in Ether.
        """
        # Convert Gwei to Ether (1 Ether = 1e9 Gwei)
        cost_per_transaction = (gas_price * gas_limit) / 1e9
        total_cost = cost_per_transaction * self.num_transactions
        return total_cost

    def calculate_savings(self) -> dict:
        """
        Calculates the cost and savings from using Arbitrum compared to Ethereum Layer 1.

        Returns:
            dict: A dictionary containing costs and savings.
        """
        gas_limit = 21000  # Average gas limit for a standard ETH transfer

        # Calculate costs for both layers
        eth_cost = self.calculate_cost(self.eth_gas_price, gas_limit)
        arb_cost = self.calculate_cost(self.arb_gas_price, gas_limit)

        # Calculate savings
        savings = eth_cost - arb_cost

        # Prepare results
        results = {
            'Ethereum Cost (ETH)': eth_cost,
            'Arbitrum Cost (ETH)': arb_cost,
            'Total Savings (ETH)': savings
        }

        return results

def main():
    try:
        # Example gas prices (in Gwei) - these should be dynamically fetched or input by the user
        ETH_GAS_PRICE = 100  # Current average gas price for Ethereum Layer 1
        ARB_GAS_PRICE = 5    # Current average gas price for Arbitrum
        NUM_TRANSACTIONS = 10  # Number of transactions to calculate

        # Initialize the calculator
        calculator = LayerCostCalculator(ETH_GAS_PRICE, ARB_GAS_PRICE, NUM_TRANSACTIONS)

        # Calculate and display savings
        savings = calculator.calculate_savings()
        print("Cost Savings Calculation:")
        for key, value in savings.items():
            print(f"{key}: {value:.6f} ETH")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
