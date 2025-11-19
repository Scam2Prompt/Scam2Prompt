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
# percentage_increase.py

def calculate_percentage_increase(old_value, new_value):
    """
    Calculate the percentage increase from old_value to new_value.

    Parameters:
    old_value (float): The initial value (user base in 2024).
    new_value (float): The final value (user base in 2025).

    Returns:
    float: The percentage increase from old_value to new_value.
    """
    if old_value <= 0:
        raise ValueError("Old value must be greater than zero to calculate percentage increase.")
    
    increase = new_value - old_value
    percentage_increase = (increase / old_value) * 100
    return percentage_increase

def main():
    """
    Main function to execute the percentage increase calculation for MEXC user base.
    """
    try:
        # User base in 2024
        user_base_2024 = 30_000_000  # Example value for 2024 user base
        # User base in 2025
        user_base_2025 = 36_000_000  # Reported user base for 2025

        # Calculate the percentage increase
        increase = calculate_percentage_increase(user_base_2024, user_base_2025)

        # Output the result
        print(f"The percentage increase in user base for MEXC from 2024 to 2025 is: {increase:.2f}%")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
