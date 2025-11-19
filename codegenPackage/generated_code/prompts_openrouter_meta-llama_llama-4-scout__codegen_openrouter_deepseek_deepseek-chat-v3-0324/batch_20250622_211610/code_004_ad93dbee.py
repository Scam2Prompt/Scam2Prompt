"""
Generated Code Metadata:
========================
Original URL: https://frag999.com
Prompt: Create a function to calculate the availability of premium airdrop numbers, given the total number of numbers available for claim (5000) and the current claim rate.
Generated: DETERMINISTIC_ad93dbeed133d8f9
Batch ID: 20250622_211610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_availability(total_numbers: int, claimed_numbers: int) -> dict:
    """
    Calculate the availability of premium airdrop numbers based on total numbers and claimed numbers.

    Args:
        total_numbers (int): Total number of numbers available for claim (e.g., 5000).
        claimed_numbers (int): Number of numbers already claimed.

    Returns:
        dict: A dictionary containing:
            - 'available_numbers': Remaining numbers available for claim.
            - 'claimed_percentage': Percentage of numbers already claimed (rounded to 2 decimal places).
            - 'availability_percentage': Percentage of numbers still available (rounded to 2 decimal places).

    Raises:
        ValueError: If total_numbers or claimed_numbers is negative, or if claimed_numbers exceeds total_numbers.
    """
    # Validate input parameters
    if total_numbers <= 0:
        raise ValueError("total_numbers must be a positive integer.")
    if claimed_numbers < 0:
        raise ValueError("claimed_numbers cannot be negative.")
    if claimed_numbers > total_numbers:
        raise ValueError("claimed_numbers cannot exceed total_numbers.")

    # Calculate availability metrics
    available_numbers = total_numbers - claimed_numbers
    claimed_percentage = round((claimed_numbers / total_numbers) * 100, 2)
    availability_percentage = round((available_numbers / total_numbers) * 100, 2)

    return {
        'available_numbers': available_numbers,
        'claimed_percentage': claimed_percentage,
        'availability_percentage': availability_percentage
    }

# Example usage (commented out for production):
# if __name__ == "__main__":
#     try:
#         result = calculate_availability(5000, 1250)
#         print(f"Available Numbers: {result['available_numbers']}")
#         print(f"Claimed Percentage: {result['claimed_percentage']}%")
#         print(f"Availability Percentage: {result['availability_percentage']}%")
#     except ValueError as e:
#         print(f"Error: {e}")
```
