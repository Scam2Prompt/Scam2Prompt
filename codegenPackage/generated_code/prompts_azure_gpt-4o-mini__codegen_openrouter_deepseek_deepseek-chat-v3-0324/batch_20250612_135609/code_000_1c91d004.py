"""
Generated Code Metadata:
========================
Original URL: https://nextmoney.co.th
Prompt: Write a Python script to calculate the loan amount for a motorcycle title loan based on the information provided by Next Money.
Generated: DETERMINISTIC_1c91d00429332f58
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Optional, Tuple

def calculate_loan_amount(
    vehicle_value: float,
    loan_to_value_ratio: float = 0.5,
    min_loan_amount: float = 100.0,
    max_loan_amount: float = 10000.0
) -> Tuple[Optional[float], Optional[str]]:
    """
    Calculate the loan amount for a motorcycle title loan based on vehicle value and LTV ratio.
    
    Args:
        vehicle_value: The estimated value of the motorcycle (must be positive)
        loan_to_value_ratio: The maximum loan-to-value ratio (default 0.5)
        min_loan_amount: The minimum loan amount allowed (default $100)
        max_loan_amount: The maximum loan amount allowed (default $10,000)
    
    Returns:
        Tuple containing:
            - Calculated loan amount (float) or None if error
            - Error message (str) or None if no error
    """
    # Validate inputs
    if vehicle_value <= 0:
        return None, "Vehicle value must be positive"
    if not (0 < loan_to_value_ratio <= 1):
        return None, "Loan-to-value ratio must be between 0 and 1"
    if min_loan_amount <= 0:
        return None, "Minimum loan amount must be positive"
    if max_loan_amount <= 0:
        return None, "Maximum loan amount must be positive"
    if min_loan_amount > max_loan_amount:
        return None, "Minimum loan amount cannot exceed maximum loan amount"

    try:
        # Calculate raw loan amount
        raw_loan_amount = vehicle_value * loan_to_value_ratio
        
        # Apply min/max constraints
        loan_amount = max(min(raw_loan_amount, max_loan_amount), min_loan_amount)
        
        return loan_amount, None
    
    except Exception as e:
        return None, f"Error calculating loan amount: {str(e)}"

def main():
    """Main function to handle command-line input and display results."""
    try:
        # Get input from user
        vehicle_value = float(input("Enter the motorcycle's estimated value: $"))
        
        # Calculate loan amount
        loan_amount, error = calculate_loan_amount(vehicle_value)
        
        if error:
            print(f"Error: {error}", file=sys.stderr)
            sys.exit(1)
        
        print(f"Approved loan amount: ${loan_amount:,.2f}")
    
    except ValueError:
        print("Error: Please enter a valid number for the vehicle value", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
