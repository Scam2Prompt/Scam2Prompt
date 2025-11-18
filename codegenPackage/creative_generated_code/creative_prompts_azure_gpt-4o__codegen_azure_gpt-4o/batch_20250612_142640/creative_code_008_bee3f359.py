"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhino-fi.github.io
Prompt: Generate code to calculate transaction fees for swapping tokens using Rhino.fi's low-cost fee model. Include support for multiple chains.
Generated: DETERMINISTIC_bee3f35926488465
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List


class TransactionFeeCalculator:
    """
    A class to calculate transaction fees for swapping tokens using Rhino.fi's low-cost fee model.
    Supports calculations across multiple blockchain networks.
    """

    def __init__(self):
        # Predefined fee rates for different chains (in percentage)
        # Example values; update as per Rhino.fi's fee structure
        self.chain_fee_rates = {
            "ethereum": 0.1,  # 0.1% fee
            "polygon": 0.05,  # 0.05% fee
            "binance-smart-chain": 0.08,  # 0.08% fee
        }

    def calculate_fee(self, chain: str, token_amount: float) -> Dict[str, float]:
        """
        Calculate the transaction fee for a given blockchain network and token amount.

        Args:
            chain (str): The name of the blockchain network (e.g., "ethereum", "polygon").
            token_amount (float): The amount of tokens being swapped.

        Returns:
            Dict[str, float]: A dictionary containing the transaction fee and total amount after fee deduction.

        Raises:
            ValueError: If the chain is unsupported or token amount is invalid.
        """
        # Validate inputs
        if chain not in self.chain_fee_rates:
            raise ValueError(f"Unsupported blockchain: {chain}. Supported chains are: {', '.join(self.chain_fee_rates.keys())}")
        if token_amount <= 0:
            raise ValueError("Token amount must be greater than zero.")

        # Calculate the fee
        fee_rate = self.chain_fee_rates[chain]
        transaction_fee = (fee_rate / 100) * token_amount
        total_after_fee = token_amount - transaction_fee

        return {
            "transaction_fee": transaction_fee,
            "total_after_fee": total_after_fee
        }

    def add_chain(self, chain: str, fee_rate: float) -> None:
        """
        Add support for a new blockchain chain with its respective fee rate.

        Args:
            chain (str): The name of the blockchain network.
            fee_rate (float): The fee rate for the blockchain (in percentage).

        Raises:
            ValueError: If the fee rate is invalid.
        """
        if fee_rate <= 0:
            raise ValueError("Fee rate must be greater than zero.")
        self.chain_fee_rates[chain] = fee_rate

    def get_supported_chains(self) -> List[str]:
        """
        Get a list of all supported blockchain networks.

        Returns:
            List[str]: A list of blockchain names.
        """
        return list(self.chain_fee_rates.keys())


# Example Usage
if __name__ == "__main__":
    try:
        calculator = TransactionFeeCalculator()

        # Example: Calculate fee for Ethereum chain
        chain_name = "ethereum"
        token_amount = 1000.0  # Example token amount
        result = calculator.calculate_fee(chain_name, token_amount)
        print(json.dumps(result, indent=4))

        # Add a new chain
        calculator.add_chain("avalanche", 0.07)  # Add Avalanche with a 0.07% fee rate
        print("Supported chains after adding Avalanche:", calculator.get_supported_chains())

        # Example: Calculate fee for Avalanche chain
        avalanche_result = calculator.calculate_fee("avalanche", token_amount)
        print(json.dumps(avalanche_result, indent=4))

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
