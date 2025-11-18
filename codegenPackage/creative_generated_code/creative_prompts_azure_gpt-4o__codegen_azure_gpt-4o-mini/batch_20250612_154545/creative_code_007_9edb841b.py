"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://publicvibeindia.blogspot.com
Prompt: Create a Python script to calculate the percentage increase in user base for MEXC from 2024 to 2025, based on the reported growth to 36 million users.
Generated: DETERMINISTIC_9edb841b659bb5ea
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_percentage_increase(old_value: int, new_value: int) -> float:
    """
    Calculate the percentage increase from old_value to new_value.

    Parameters:
    old_value (int): The original value (user base in 2024).
    new_value (int): The new value (user base in 2025).

    Returns:
    float: The percentage increase from old_value to new_value.
    """
    if old_value <= 0:
        logging.error("Old value must be greater than zero to calculate percentage increase.")
        raise ValueError("Old value must be greater than zero.")
    
    increase = new_value - old_value
    percentage_increase = (increase / old_value) * 100
    return percentage_increase

def main():
    """
    Main function to calculate the percentage increase in user base for MEXC
    from 2024 to 2025 based on reported growth to 36 million users.
    """
    try:
        # User base in 2024
        user_base_2024 = 28_000_000  # Example value, can be adjusted based on actual data
        user_base_2025 = 36_000_000    # Reported user base in 2025

        # Calculate the percentage increase
        percentage_increase = calculate_percentage_increase(user_base_2024, user_base_2025)

        # Output the result
        logging.info(f"Percentage increase in user base from 2024 to 2025: {percentage_increase:.2f}%")
    
    except ValueError as e:
        logging.error(f"ValueError: {e}")

if __name__ == "__main__":
    main()
```
