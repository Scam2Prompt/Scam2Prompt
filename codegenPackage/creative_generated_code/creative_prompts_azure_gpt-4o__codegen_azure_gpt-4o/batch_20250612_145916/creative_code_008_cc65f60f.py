"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonminingpool.xyz
Prompt: Create a script to calculate the ROI (Return on Investment) for Toncoin deposits based on the 300% ROI model described on TONMININGPOOL.
Generated: DETERMINISTIC_cc65f60fcf506826
Batch ID: 20250612_145916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_roi(deposit_amount: float, roi_percentage: float = 300.0) -> float:
    """
    Calculate the ROI (Return on Investment) for a given deposit amount and ROI percentage.
    
    Args:
        deposit_amount (float): The initial deposit amount in Toncoin.
        roi_percentage (float): The ROI percentage to be applied. Defaults to 300%.
        
    Returns:
        float: The calculated ROI amount.
    """
    try:
        # Ensure the deposit amount is a positive number
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        # Calculate ROI
        roi_amount = deposit_amount * (roi_percentage / 100)
        return roi_amount
    
    except TypeError:
        raise TypeError("Invalid input type. Deposit amount should be a numeric value.")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to run the ROI calculation script.
    Prompts the user for input and calculates the ROI.
    """
    try:
        print("Welcome to the Toncoin ROI Calculator!")
        
        # Prompt the user for deposit amount
        deposit_input = input("Please enter the deposit amount in Toncoin: ")
        
        # Convert input to float, and validate
        deposit_amount = float(deposit_input)
        
        # Calculate ROI using the default 300% model
        roi_amount = calculate_roi(deposit_amount)
        
        # Display the calculated ROI
        print(f"Based on a 300% ROI model, the return on your deposit of {deposit_amount} Toncoin is: {roi_amount} Toncoin.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
