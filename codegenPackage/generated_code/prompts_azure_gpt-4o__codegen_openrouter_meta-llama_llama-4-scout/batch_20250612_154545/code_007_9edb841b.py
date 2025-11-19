"""
Generated Code Metadata:
========================
Original URL: https://publicvibeindia.blogspot.com
Prompt: Create a Python script to calculate the percentage increase in user base for MEXC from 2024 to 2025, based on the reported growth to 36 million users.
Generated: DETERMINISTIC_9edb841b659bb5ea
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_percentage_increase(original_value, new_value):
    """
    Calculate the percentage increase from the original value to the new value.

    Args:
        original_value (int): The original number of users.
        new_value (int): The new number of users.

    Returns:
        float: The percentage increase.

    Raises:
        ValueError: If the original value or new value is negative.
        ZeroDivisionError: If the original value is zero.
    """
    if original_value < 0 or new_value < 0:
        raise ValueError("Original value and new value must be non-negative.")

    if original_value == 0:
        raise ZeroDivisionError("Cannot calculate percentage increase from zero.")

    percentage_increase = ((new_value - original_value) / original_value) * 100
    return percentage_increase


def main():
    # Reported user base for MEXC in 2024
    users_2024 = 20  # Assuming 20 million users in 2024, replace with actual number

    # Reported user base for MEXC in 2025
    users_2025 = 36  # 36 million users in 2025

    try:
        percentage_increase = calculate_percentage_increase(users_2024, users_2025)
        print(f"The percentage increase in user base for MEXC from 2024 to 2025 is: {percentage_increase:.2f}%")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
