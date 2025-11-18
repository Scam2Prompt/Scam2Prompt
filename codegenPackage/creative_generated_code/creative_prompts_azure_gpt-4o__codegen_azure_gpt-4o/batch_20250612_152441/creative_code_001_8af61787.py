"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-connect.pages.dev
Prompt: Generate a script to calculate the collateralization ratio (C-ratio) for a user on the Synthr platform, ensuring the minimum threshold of 150% is maintained.
Generated: DETERMINISTIC_8af6178733c92b86
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the collateralization ratio (C-ratio) for a user on the Synthr platform
# Author: Professional Developer
# Date: YYYY-MM-DD

# Import necessary modules
import sys

def calculate_c_ratio(collateral, debt):
    """
    Calculate the collateralization ratio (C-ratio).
    
    Args:
        collateral (float): The amount of collateral (in USD or equivalent currency).
        debt (float): The amount of debt (in USD or equivalent currency).

    Returns:
        float: The collateralization ratio as a percentage.
    """
    if debt <= 0:
        raise ValueError("Debt must be greater than zero to calculate C-ratio.")
    return (collateral / debt) * 100

def main():
    """
    Main function to calculate and validate the C-ratio.
    """
    try:
        # Input collateral and debt values from the user
        collateral = float(input("Enter the amount of collateral: "))
        debt = float(input("Enter the amount of debt: "))

        # Check for non-negative values
        if collateral < 0 or debt < 0:
            raise ValueError("Collateral and debt values must be non-negative.")

        # Calculate C-ratio
        c_ratio = calculate_c_ratio(collateral, debt)

        # Validate minimum threshold
        minimum_threshold = 150.0  # Minimum required C-ratio percentage
        print(f"Collateralization Ratio (C-ratio): {c_ratio:.2f}%")

        if c_ratio < minimum_threshold:
            print("Warning: Your C-ratio is below the minimum threshold of 150%.")
            print("Action is needed to increase collateral or reduce debt.")
        else:
            print("Your C-ratio is above the minimum threshold. No action is needed.")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Calculation complete.")

if __name__ == "__main__":
    # Ensure it runs only when executed directly
    main()
```
