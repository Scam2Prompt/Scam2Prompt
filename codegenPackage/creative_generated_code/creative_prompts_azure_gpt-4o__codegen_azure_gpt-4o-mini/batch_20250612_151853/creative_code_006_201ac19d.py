"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-altvenusio-git-feat-optimism-venus-protocol.vercel.app
Prompt: Develop a function to calculate borrowing limits based on collateral supplied to the Venus Protocol.
Generated: DETERMINISTIC_201ac19de7049fd1
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VenusProtocol:
    def __init__(self, collateral_value: float, collateral_factor: float):
        """
        Initializes the VenusProtocol with the provided collateral value and collateral factor.
        
        :param collateral_value: The market value of the collateral provided (in USD).
        :param collateral_factor: The factor representing how much can be borrowed against the collateral (in decimal).
        """
        if collateral_value < 0:
            raise ValueError("Collateral value must be non-negative.")
        if not (0 <= collateral_factor <= 1):
            raise ValueError("Collateral factor must be between 0 and 1.")

        self.collateral_value = collateral_value
        self.collateral_factor = collateral_factor

    def calculate_borrowing_limit(self) -> float:
        """
        Calculates the borrowing limit based on the collateral value and collateral factor.
        
        :return: The maximum amount that can be borrowed (in USD).
        """
        borrowing_limit = self.collateral_value * self.collateral_factor
        return borrowing_limit

# Example usage:
try:
    collateral_value = 10000.0  # Example collateral value in USD
    collateral_factor = 0.75     # Example collateral factor

    # Initialize the Venus Protocol with collateral details
    venus_protocol = VenusProtocol(collateral_value, collateral_factor)

    # Calculate and print the borrowing limit
    limit = venus_protocol.calculate_borrowing_limit()
    print(f"The borrowing limit is: ${limit:.2f}")
except ValueError as ve:
    print(f"Input error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
