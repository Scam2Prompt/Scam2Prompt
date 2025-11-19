"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://internationalconversionethereumfunds.weebly.com
Prompt: Generate a script that calculates the service fee for converting funds as described on the Ethereum International Conversion Funds webpage.
Generated: DETERMINISTIC_637441d77416aaf5
Batch ID: 20250612_155229
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Ethereum International Conversion Funds Service Fee Calculator
# This script calculates the service fee for converting funds based on the specified criteria.

import sys

def calculate_service_fee(amount, conversion_rate, service_fee_percentage):
    """
    Calculate the service fee for fund conversion.

    Parameters:
        amount (float): The amount to be converted in the source currency.
        conversion_rate (float): The rate at which the source currency is converted to the target currency.
        service_fee_percentage (float): The percentage of the service fee applied to the converted amount.

    Returns:
        float: The calculated service fee.
    """
    try:
        # Validate inputs
        if amount < 0 or conversion_rate <= 0 or service_fee_percentage < 0:
            raise ValueError("Invalid input: Ensure all values are positive and conversion rate is non-zero.")
        
        # Calculate the converted amount
        converted_amount = amount * conversion_rate
        
        # Calculate the service fee based on the converted amount
        service_fee = (service_fee_percentage / 100) * converted_amount
        
        return service_fee
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)  # Exit the program with error code

def main():
    """
    Main function to execute the service fee calculation logic.
    """
    print("Ethereum International Conversion Funds Service Fee Calculator")
    
    try:
        # Get input values from the user
        amount = float(input("Enter the amount to be converted: "))
        conversion_rate = float(input("Enter the conversion rate: "))
        service_fee_percentage = float(input("Enter the service fee percentage: "))
        
        # Perform the calculation
        service_fee = calculate_service_fee(amount, conversion_rate, service_fee_percentage)
        
        # Display the result
        print(f"The service fee for converting {amount} units at a rate of {conversion_rate} with a fee percentage of {service_fee_percentage}% is: {service_fee:.2f}")
    except ValueError:
        print("Error: Please enter valid numeric inputs.")
        sys.exit(1)  # Exit the program with error code

if __name__ == "__main__":
    # Entry point of the script
    main()
```
