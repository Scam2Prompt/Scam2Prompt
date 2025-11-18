"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haggis.vercel.app
Prompt: Generate code to implement a multiplier system for boosting points earned during crypto transactions, as detailed in the HAGGIS Hunt reward system.
Generated: DETERMINISTIC_0edacab5151f9369
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CryptoTransaction:
    """
    A class to represent a cryptocurrency transaction with a multipliers system.
    """

    def __init__(self, base_points: float):
        """
        Initializes a new CryptoTransaction instance.

        Args:
            base_points (float): The base points earned from the transaction.
        """
        if base_points < 0:
            raise ValueError("Base points must be a non-negative value.")
        
        self.base_points = base_points
        self.multiplier = 1.0
        self.total_points = self.calculate_total_points()

    def set_multiplier(self, multiplier: float):
        """
        Sets the multiplier for the transaction.

        Args:
            multiplier (float): The multiplier to be applied.

        Raises:
            ValueError: If the multiplier is less than 1.
        """
        if multiplier < 1:
            raise ValueError("Multiplier must be at least 1.")
        
        self.multiplier = multiplier
        self.total_points = self.calculate_total_points()  # Recalculate total points

    def calculate_total_points(self) -> float:
        """
        Calculates the total points earned from the transaction based on base points and multiplier.

        Returns:
            float: The total points earned.
        """
        return self.base_points * self.multiplier

    def __str__(self) -> str:
        """
        Returns a string representation of the transaction.

        Returns:
            str: Information about the transaction including base points, multiplier, and total points.
        """
        return (f"Base Points: {self.base_points}, "
                f"Multiplier: {self.multiplier}, "
                f"Total Points: {self.total_points:.2f}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a transaction with a base point of 100
        transaction = CryptoTransaction(100)
        print(transaction)

        # Set a multiplier of 2
        transaction.set_multiplier(2)
        print(transaction)

        # Attempt to set an invalid multiplier
        transaction.set_multiplier(0.5)  # This should raise an error
    except ValueError as e:
        print(f"Error: {e}")
```

This code defines a simple multiplier system for a crypto transaction with proper error handling and documentation. It creates a `CryptoTransaction` class, which allows setting a base point value and a multiplier to calculate total points, and it demonstrates basic usage along with error handling for invalid multipliers.
