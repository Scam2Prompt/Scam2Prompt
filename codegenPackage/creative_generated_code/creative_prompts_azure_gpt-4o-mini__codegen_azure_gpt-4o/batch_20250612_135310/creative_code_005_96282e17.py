"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://co-opttradexcoin.com
Prompt: Create a function that calculates potential returns on investment for cryptocurrency based on the guaranteed ROIs mentioned by Co-opt Trade Xcoin.
Generated: DETERMINISTIC_96282e176c15ff2b
Batch ID: 20250612_135310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_crypto_roi(principal, roi_percentage, years):
    """
    Calculate the potential returns on investment for cryptocurrency based on ROI.

    Args:
        principal (float): The initial investment amount.
        roi_percentage (float): The guaranteed annual ROI percentage (e.g., 10 for 10%).
        years (int): The investment duration in years.

    Returns:
        float: The total amount after the investment duration.
    
    Raises:
        ValueError: If any input is invalid (negative values or zero for principal/years).
    """
    try:
        # Validate inputs
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if roi_percentage < 0:
            raise ValueError("ROI percentage cannot be negative.")
        if years <= 0:
            raise ValueError("Investment duration (years) must be greater than zero.")

        # Calculate the ROI using compound interest formula: A = P * (1 + r)^t
        rate = roi_percentage / 100  # Convert percentage to decimal
        total_amount = principal * (1 + rate) ** years

        return round(total_amount, 2)  # Round off to 2 decimal places for readability

    except ValueError as ve:
        print(f"ValueError: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


# Example Usage
if __name__ == "__main__":
    try:
        # Inputs
        initial_investment = float(input("Enter the principal amount (initial investment): "))
        annual_roi = float(input("Enter the guaranteed annual ROI percentage: "))
        investment_years = int(input("Enter the investment duration in years: "))

        # Calculate ROI
        total_returns = calculate_crypto_roi(initial_investment, annual_roi, investment_years)
        
        # Output Results
        print(f"Total returns after {investment_years} years: ${total_returns}")
    except ValueError:
        print("Invalid input. Please enter numeric values for principal, ROI, and years.")
    except Exception as e:
        print(f"An error occurred during execution: {e}")
```
