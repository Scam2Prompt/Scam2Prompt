"""
Generated Code Metadata:
========================
Original URL: https://bitdegree.pages.dev
Prompt: Write a function to calculate the total Bits earned based on the number of blockchain transactions tracked, adhering to Blockpit's daily or monthly limits.
Generated: DETERMINISTIC_3e51c24910a96150
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class TrackingPeriod(Enum):
    """Enum for tracking period"""
    DAILY = "daily"
    MONTHLY = "monthly"

class BlockpitConfig:
    """Class to hold Blockpit configuration"""
    def __init__(self, daily_limit: int, monthly_limit: int, bits_per_transaction: int):
        """
        Initialize Blockpit configuration

        Args:
        - daily_limit (int): Daily limit of transactions
        - monthly_limit (int): Monthly limit of transactions
        - bits_per_transaction (int): Bits earned per transaction
        """
        self.daily_limit = daily_limit
        self.monthly_limit = monthly_limit
        self.bits_per_transaction = bits_per_transaction

def calculate_bits_earned(transactions: int, tracking_period: TrackingPeriod, config: BlockpitConfig) -> int:
    """
    Calculate total Bits earned based on the number of blockchain transactions tracked

    Args:
    - transactions (int): Number of transactions
    - tracking_period (TrackingPeriod): Tracking period (daily or monthly)
    - config (BlockpitConfig): Blockpit configuration

    Returns:
    - int: Total Bits earned

    Raises:
    - ValueError: If tracking period is invalid
    - ValueError: If transactions is negative
    """
    if tracking_period not in [TrackingPeriod.DAILY, TrackingPeriod.MONTHLY]:
        raise ValueError("Invalid tracking period")

    if transactions < 0:
        raise ValueError("Transactions cannot be negative")

    if tracking_period == TrackingPeriod.DAILY:
        limit = config.daily_limit
    else:
        limit = config.monthly_limit

    # Calculate the effective transactions, considering the limit
    effective_transactions = min(transactions, limit)

    # Calculate the total Bits earned
    total_bits = effective_transactions * config.bits_per_transaction

    return total_bits

def main():
    # Example usage
    config: Dict[str, int] = {
        "daily_limit": 100,
        "monthly_limit": 1000,
        "bits_per_transaction": 10
    }

    blockpit_config = BlockpitConfig(**config)

    transactions = 150
    tracking_period = TrackingPeriod.DAILY

    try:
        bits_earned = calculate_bits_earned(transactions, tracking_period, blockpit_config)
        print(f"Total Bits earned: {bits_earned}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
