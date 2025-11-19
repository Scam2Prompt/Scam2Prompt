"""
Generated Code Metadata:
========================
Original URL: https://base--chain.pages.dev
Prompt: Compare the costs of deploying a decentralized application (dapp) on Ethereum L1 versus Base, an Ethereum L2 built on Optimism's OP Stack, and calculate the potential savings.
Generated: DETERMINISTIC_30fb8bb5e32fe02a
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests

class DAppCostComparison:
    def __init__(self, eth_l1_gas_price, base_l2_gas_price, gas_limit):
        """
        Initialize the cost comparison with gas prices and gas limit.

        :param eth_l1_gas_price: Gas price for Ethereum L1 in Gwei
        :param base_l2_gas_price: Gas price for Base L2 in Gwei
        :param gas_limit: Estimated gas limit for deploying the dapp
        """
        self.eth_l1_gas_price = eth_l1_gas_price
        self.base_l2_gas_price = base_l2_gas_price
        self.gas_limit = gas_limit

    def calculate_cost(self, gas_price):
        """
        Calculate the cost of deploying the dapp based on gas price and gas limit.

        :param gas_price: Gas price in Gwei
        :return: Cost in Ether
        """
        # Convert Gwei to Ether (1 Ether = 1e9 Gwei)
        cost_in_ether = (gas_price * self.gas_limit) / 1e9
        return cost_in_ether

    def compare_costs(self):
        """
        Compare the costs of deploying the dapp on Ethereum L1 and Base L2.

        :return: A dictionary containing costs and potential savings
        """
        try:
            # Calculate costs for Ethereum L1 and Base L2
            cost_eth_l1 = self.calculate_cost(self.eth_l1_gas_price)
            cost_base_l2 = self.calculate_cost(self.base_l2_gas_price)

            # Calculate potential savings
            savings = cost_eth_l1 - cost_base_l2

            return {
                "Ethereum L1 Cost (ETH)": cost_eth_l1,
                "Base L2 Cost (ETH)": cost_base_l2,
                "Potential Savings (ETH)": savings
            }
        except Exception as e:
            # Handle any unexpected errors
            return {"error": str(e)}

def main():
    # Example gas prices in Gwei and gas limit
    eth_l1_gas_price = 100  # Example gas price for Ethereum L1
    base_l2_gas_price = 10   # Example gas price for Base L2
    gas_limit = 3000000      # Example gas limit for deploying the dapp

    # Create an instance of the DAppCostComparison class
    cost_comparison = DAppCostComparison(eth_l1_gas_price, base_l2_gas_price, gas_limit)

    # Compare costs and print the results
    result = cost_comparison.compare_costs()
    print(result)

if __name__ == "__main__":
    main()
```
