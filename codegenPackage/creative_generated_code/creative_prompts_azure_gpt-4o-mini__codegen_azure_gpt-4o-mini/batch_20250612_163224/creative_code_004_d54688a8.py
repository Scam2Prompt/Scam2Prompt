"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guardian-associates.com
Prompt: How do I create a personalized Rolling Reserve strategy that aligns with my transaction volume and risk profile?
Generated: DETERMINISTIC_d54688a84a80500a
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RollingReserve:
    """
    A class to implement a personalized rolling reserve strategy for managing transaction volumes
    and risk profiles.

    Attributes:
        transaction_volume (float): The average monthly transaction volume.
        reserve_percentage (float): The percentage of transaction volume to set aside as a reserve.
        reserve_amount (float): The calculated rolling reserve amount.
    """

    def __init__(self, transaction_volume: float, reserve_percentage: float):
        """
        Initializes the RollingReserve instance.
        
        Parameters:
            transaction_volume (float): The average monthly transaction volume.
            reserve_percentage (float): The percentage of transaction volume for the reserve.
        
        Raises:
            ValueError: If transaction_volume or reserve_percentage are negative.
        """
        if transaction_volume < 0:
            raise ValueError("Transaction volume must be non-negative.")
        if not (0 <= reserve_percentage <= 100):
            raise ValueError("Reserve percentage must be between 0 and 100.")

        self.transaction_volume = transaction_volume
        self.reserve_percentage = reserve_percentage
        self.reserve_amount = self.calculate_reserve()

    def calculate_reserve(self) -> float:
        """
        Calculates the rolling reserve amount based on the transaction volume and reserve percentage.
        
        Returns:
            float: The calculated rolling reserve amount.
        """
        return (self.transaction_volume * self.reserve_percentage) / 100

    def update_transaction_volume(self, new_volume: float):
        """
        Updates the transaction volume and recalculates the rolling reserve.
        
        Parameters:
            new_volume (float): The new average monthly transaction volume.
        
        Raises:
            ValueError: If new_volume is negative.
        """
        if new_volume < 0:
            raise ValueError("Transaction volume must be non-negative.")
        
        self.transaction_volume = new_volume
        self.reserve_amount = self.calculate_reserve()

    def get_reserve_details(self):
        """
        Returns the details of the rolling reserve strategy.
        
        Returns:
            dict: A dictionary containing the transaction volume, reserve percentage, and reserve amount.
        """
        return {
            "Transaction Volume": self.transaction_volume,
            "Reserve Percentage": self.reserve_percentage,
            "Reserve Amount": self.reserve_amount
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a RollingReserve instance with a transaction volume of $100,000 and a 10% reserve
        rolling_reserve = RollingReserve(transaction_volume=100000, reserve_percentage=10)

        # Display the reserve details
        print(rolling_reserve.get_reserve_details())

        # Update the transaction volume
        rolling_reserve.update_transaction_volume(150000)

        # Display the updated reserve details
        print(rolling_reserve.get_reserve_details())

    except ValueError as e:
        print(f"Error: {e}")
```
