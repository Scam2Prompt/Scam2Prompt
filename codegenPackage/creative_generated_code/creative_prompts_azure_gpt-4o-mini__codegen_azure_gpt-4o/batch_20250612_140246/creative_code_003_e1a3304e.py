"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanshu-migrations.pages.dev
Prompt: Generate a function that calculates the conversion amount when migrating from SANSHU v1 to SANSHU v2 based on the user's balance.
Generated: DETERMINISTIC_e1a3304e09137ad3
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Union

# Define the conversion function
def calculate_conversion_amount(balance_v1: Union[int, float], conversion_rate: Union[int, float]) -> Union[int, float]:
    """
    Calculate the conversion amount when migrating from SANSHU v1 to SANSHU v2.

    Args:
        balance_v1 (Union[int, float]): The user's balance in SANSHU v1.
        conversion_rate (Union[int, float]): The conversion rate from SANSHU v1 to SANSHU v2.

    Returns:
        Union[int, float]: The converted balance in SANSHU v2.

    Raises:
        ValueError: If balance_v1 or conversion_rate is negative.
    """
    # Validate input: balance_v1 and conversion_rate must be non-negative
    if balance_v1 < 0:
        raise ValueError("balance_v1 must be a non-negative value.")
    if conversion_rate <= 0:
        raise ValueError("conversion_rate must be a positive value.")

    # Perform conversion calculation
    converted_balance = balance_v1 * conversion_rate

    # Return the converted balance
    return converted_balance


# Example usage:
if __name__ == "__main__":
    try:
        # User inputs
        user_balance_v1 = 1000  # Replace with actual balance in SANSHU v1
        rate_v1_to_v2 = 0.1     # Replace with actual conversion rate from SANSHU v1 to SANSHU v2

        # Calculate conversion
        converted_balance = calculate_conversion_amount(user_balance_v1, rate_v1_to_v2)
        print(f"The converted balance in SANSHU v2 is: {converted_balance}")
    except ValueError as e:
        print(f"Error: {e}")
```
