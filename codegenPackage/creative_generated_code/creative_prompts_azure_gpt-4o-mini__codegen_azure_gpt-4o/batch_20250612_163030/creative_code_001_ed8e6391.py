"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upshift.fi
Prompt: Write a Python script to calculate potential earnings from the 1.25x upUSDC PT Boost offered by Upshift Finance.
Generated: DETERMINISTIC_ed8e63910996ec27
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate potential earnings from the 1.25x upUSDC PT Boost offered by Upshift Finance.
This script assumes the user inputs the principal amount and duration of the boost.
"""

# Import necessary modules
import sys

def calculate_earnings(principal, duration, boost_rate=1.25):
    """
    Calculate potential earnings from the Upshift Finance boost.
    
    Args:
        principal (float): The initial principal amount in USDC.
        duration (int): Duration of the boost in days.
        boost_rate (float): The boost multiplier rate (default is 1.25).
    
    Returns:
        float: The potential earnings after applying the boost.
    """
    try:
        # Ensure principal and duration are valid values
        if principal <= 0:
            raise ValueError("Principal must be greater than 0.")
        if duration <= 0:
            raise ValueError("Duration must be greater than 0.")
        
        # Calculate the boosted amount
        boosted_amount = principal * boost_rate
        
        # Return the calculated boosted earnings
        return boosted_amount
    
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
        sys.exit(1)  # Exit the script with an error code

def main():
    """
    Main function to take user input and calculate earnings using the Upshift Finance boost.
    """
    print("Welcome to the Upshift Finance Earnings Calculator!")
    
    try:
        # Get user input
        principal = float(input("Enter the principal amount in USDC: "))
        duration = int(input("Enter the duration of the boost in days: "))
        
        # Call the calculation function
        earnings = calculate_earnings(principal, duration)
        
        # Display the result to the user
        print(f"Potential earnings after applying the 1.25x boost: {earnings:.2f} USDC")
    
    except ValueError:
        # Handle invalid input types
        print("Error: Please enter valid numerical inputs for principal and duration.")
        sys.exit(1)  # Exit the script with an error code

if __name__ == "__main__":
    # Run the main function
    main()
```
