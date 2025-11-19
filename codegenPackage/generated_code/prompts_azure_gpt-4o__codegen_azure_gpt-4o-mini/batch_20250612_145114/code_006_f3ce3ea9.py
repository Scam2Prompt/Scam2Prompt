"""
Generated Code Metadata:
========================
Original URL: https://shadow-exchange.com
Prompt: Write a function to customize fee splits for a specific gauge and creator fees on Shadow Exchange's intelligent fee system.
Generated: DETERMINISTIC_f3ce3ea9ed14f9d7
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FeeSplitError(Exception):
    """Custom exception for errors related to fee splits."""
    pass

class ShadowExchange:
    def __init__(self):
        # Initialize a dictionary to hold fee splits for each gauge
        self.fee_splits = {}

    def set_fee_split(self, gauge_id: str, creator_fee: float, split_percentage: float):
        """
        Set the fee split for a specific gauge.

        Parameters:
        gauge_id (str): The unique identifier for the gauge.
        creator_fee (float): The fee percentage allocated to the creator (0-100).
        split_percentage (float): The percentage of the remaining fees to be split (0-100).

        Raises:
        FeeSplitError: If the fee percentages are not valid.
        """
        # Validate input parameters
        if not (0 <= creator_fee <= 100):
            raise FeeSplitError("Creator fee must be between 0 and 100.")
        if not (0 <= split_percentage <= 100):
            raise FeeSplitError("Split percentage must be between 0 and 100.")

        # Store the fee split configuration
        self.fee_splits[gauge_id] = {
            'creator_fee': creator_fee,
            'split_percentage': split_percentage
        }

    def get_fee_split(self, gauge_id: str):
        """
        Retrieve the fee split configuration for a specific gauge.

        Parameters:
        gauge_id (str): The unique identifier for the gauge.

        Returns:
        dict: A dictionary containing the creator fee and split percentage.

        Raises:
        FeeSplitError: If the gauge_id does not exist.
        """
        if gauge_id not in self.fee_splits:
            raise FeeSplitError(f"No fee split configuration found for gauge ID: {gauge_id}")

        return self.fee_splits[gauge_id]

# Example usage
if __name__ == "__main__":
    exchange = ShadowExchange()
    
    try:
        # Set fee splits for a specific gauge
        exchange.set_fee_split("gauge_1", 10.0, 90.0)
        
        # Retrieve and print the fee split configuration
        fee_split = exchange.get_fee_split("gauge_1")
        print(f"Fee split for gauge_1: {fee_split}")
        
    except FeeSplitError as e:
        print(f"Error: {e}")
```
