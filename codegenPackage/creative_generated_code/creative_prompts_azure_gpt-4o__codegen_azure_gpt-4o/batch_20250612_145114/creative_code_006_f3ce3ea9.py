"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shadow-exchange.com
Prompt: Write a function to customize fee splits for a specific gauge and creator fees on Shadow Exchange's intelligent fee system.
Generated: DETERMINISTIC_f3ce3ea9ed14f9d7
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FeeSplitter:
    """
    A class to handle fee split customization for Shadow Exchange's intelligent fee system.
    """

    def __init__(self):
        """
        Initialize the FeeSplitter class with default fee splits.
        """
        self.default_split = {
            'gauge': 50,   # Default gauge fee percentage
            'creator': 50  # Default creator fee percentage
        }

    def customize_fee_split(self, gauge_fee: int, creator_fee: int) -> dict:
        """
        Customizes the fee split between gauge and creator. 
        Ensures the total split equals 100% and values are within valid ranges.

        Parameters:
        - gauge_fee (int): The percentage of fees to allocate to the gauge (0-100).
        - creator_fee (int): The percentage of fees to allocate to the creator (0-100).

        Returns:
        - dict: A dictionary containing the custom fee split.

        Raises:
        - ValueError: If the total percentage does not equal 100 or if values are invalid.
        """
        # Validate inputs
        if not (0 <= gauge_fee <= 100):
            raise ValueError("Gauge fee must be between 0 and 100 inclusive.")
        if not (0 <= creator_fee <= 100):
            raise ValueError("Creator fee must be between 0 and 100 inclusive.")
        if gauge_fee + creator_fee != 100:
            raise ValueError("The total of gauge and creator fees must equal 100.")

        # Return the new fee split
        return {
            'gauge': gauge_fee,
            'creator': creator_fee
        }

# Example usage:
if __name__ == "__main__":
    fee_splitter = FeeSplitter()
    
    try:
        # Customizing the fee split
        custom_split = fee_splitter.customize_fee_split(gauge_fee=60, creator_fee=40)
        print("Custom Fee Split:", custom_split)
    except ValueError as e:
        print("Error:", e)
```
