"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ltc-mixer.xyz
Prompt: Generate a script that calculates the optimal mixing fee percentage based on transaction volume for using the LTC mixer.
Generated: DETERMINISTIC_904d2a7a7d412dee
Batch ID: 20250612_155803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_optimal_mixing_fee(transaction_volume):
    """
    Calculates the optimal mixing fee percentage based on transaction volume.

    Args:
        transaction_volume (float): The volume of the transaction in LTC.

    Returns:
        float: The recommended mixing fee percentage.
    """
    try:
        # Validate input
        if transaction_volume <= 0:
            raise ValueError("Transaction volume must be a positive number.")

        # Base fee percentage
        base_fee = 0.5  # 0.5% minimum fee

        # Dynamic fee adjustment based on transaction volume
        # Reduce fee percentage as the transaction volume increases
        dynamic_fee = 1 / math.sqrt(transaction_volume) * 10

        # Ensure the fee percentage does not go below the base fee
        optimal_fee = max(base_fee, dynamic_fee)

        # Cap the fee percentage at a maximum of 5%
        optimal_fee = min(optimal_fee, 5)

        return round(optimal_fee, 2)  # Return fee rounded to two decimal places

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    try:
        # Prompt user for transaction volume in LTC
        transaction_volume = float(input("Enter the transaction volume in LTC: "))
        
        # Calculate the optimal mixing fee
        optimal_fee = calculate_optimal_mixing_fee(transaction_volume)
        
        if optimal_fee is not None:
            print(f"The optimal mixing fee percentage for a transaction volume of {transaction_volume} LTC is: {optimal_fee}%")
        else:
            print("Could not calculate the optimal mixing fee due to an error.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the transaction volume.")
```
