"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supercore-7hg.pages.dev
Prompt: Write a script to calculate slippage tolerance for token swaps and display warnings if the tolerance exceeds 0.5%.
Generated: DETERMINISTIC_e399ac7233aeb127
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script: Calculate slippage tolerance for token swaps
# Author: Expert Programmer
# Description: This script calculates slippage tolerance for token swaps and displays warnings if the tolerance exceeds 0.5%.

# Import necessary libraries
import sys

def calculate_slippage_tolerance(expected_price, actual_price):
    """
    Calculate the percentage of slippage tolerance based on expected and actual price.
    
    :param expected_price: The price you expect per token (float)
    :param actual_price: The price you actually get per token (float)
    :return: Slippage tolerance percentage (float)
    """
    try:
        # Validate inputs
        if expected_price <= 0 or actual_price <= 0:
            raise ValueError("Expected price and actual price must be positive numbers.")
        
        # Calculate slippage tolerance as a percentage
        slippage_tolerance = abs((expected_price - actual_price) / expected_price) * 100
        return slippage_tolerance
    
    except Exception as e:
        print(f"Error calculating slippage tolerance: {e}")
        sys.exit(1)

def main():
    """
    Main function to perform token swap slippage tolerance calculation.
    """
    try:
        # Example inputs: Replace with actual values or user input
        expected_price = float(input("Enter the expected price per token: "))
        actual_price = float(input("Enter the actual price per token: "))
        
        # Calculate slippage tolerance
        slippage_tolerance = calculate_slippage_tolerance(expected_price, actual_price)
        
        # Display results
        print(f"Slippage Tolerance: {slippage_tolerance:.2f}%")
        
        # Warning if slippage exceeds 0.5%
        if slippage_tolerance > 0.5:
            print("WARNING: Slippage tolerance exceeds 0.5%. Consider reviewing your swap.")
        else:
            print("Slippage tolerance is within acceptable limits.")
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)

    except ValueError as ve:
        print(f"Input error: {ve}")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
