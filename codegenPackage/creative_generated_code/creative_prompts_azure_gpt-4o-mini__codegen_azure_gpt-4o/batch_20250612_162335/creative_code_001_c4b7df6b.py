"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shdw.so
Prompt: Write a code snippet that demonstrates how to create a dynamic fee structure for liquidity providers similar to what is described in Shadow Exchange.
Generated: DETERMINISTIC_c4b7df6b6ba65c62
Batch ID: 20250612_162335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from typing import List

# Define an exception for invalid fee structure
class FeeStructureError(Exception):
    pass

# LiquidityProvider class to hold provider-specific data
class LiquidityProvider:
    def __init__(self, provider_id: str, liquidity: decimal.Decimal):
        """
        Initialize a LiquidityProvider instance.

        :param provider_id: Unique identifier for the liquidity provider.
        :param liquidity: Amount of liquidity provided by the provider.
        """
        self.provider_id = provider_id
        self.liquidity = liquidity

# DynamicFeeCalculator class to manage fee distribution
class DynamicFeeCalculator:
    def __init__(self, total_fee: decimal.Decimal):
        """
        Initialize the DynamicFeeCalculator.

        :param total_fee: Total fee collected from trades to distribute among liquidity providers.
        """
        if total_fee < decimal.Decimal("0"):
            raise FeeStructureError("Total fee cannot be negative.")
        self.total_fee = total_fee

    def calculate_fee_distribution(self, providers: List[LiquidityProvider]) -> dict:
        """
        Calculate fee distribution based on the liquidity provided by each provider.

        :param providers: List of LiquidityProvider instances.
        :return: Dictionary mapping provider_id to allocated fee.
        """
        # Validate inputs
        if not providers:
            raise FeeStructureError("Provider list cannot be empty.")

        total_liquidity = sum(provider.liquidity for provider in providers)
        if total_liquidity <= decimal.Decimal("0"):
            raise FeeStructureError("Total liquidity must be greater than zero.")

        # Distribute the fee proportionally
        fee_distribution = {}
        for provider in providers:
            proportion = provider.liquidity / total_liquidity
            allocated_fee = self.total_fee * proportion
            fee_distribution[provider.provider_id] = round(allocated_fee, 8)  # Round for precision

        return fee_distribution

# Example Usage
if __name__ == "__main__":
    # Define liquidity providers
    providers = [
        LiquidityProvider("provider1", decimal.Decimal("100.0")),
        LiquidityProvider("provider2", decimal.Decimal("200.0")),
        LiquidityProvider("provider3", decimal.Decimal("300.0")),
    ]

    # Define total fee collected
    total_fee = decimal.Decimal("1000.0")

    # Initialize the fee calculator
    calculator = DynamicFeeCalculator(total_fee)

    try:
        # Calculate fee distribution
        distribution = calculator.calculate_fee_distribution(providers)

        # Print the result
        print("Fee Distribution:")
        for provider_id, fee in distribution.items():
            print(f"{provider_id}: {fee}")
    except FeeStructureError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
