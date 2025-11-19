"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dresale.pages.dev
Prompt: Write a Python script to calculate the number of DRE tokens received for a given amount of FTM during the presale.
Generated: DETERMINISTIC_a4fcc87d0467fe12
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for error handling
import sys

def calculate_dre_tokens(ftm_amount, exchange_rate):
    """
    Function to calculate the number of DRE tokens received during the presale.

    Parameters:
    ftm_amount (float): The amount of FTM tokens provided by the user.
    exchange_rate (float): The exchange rate of FTM to DRE tokens.

    Returns:
    float: The number of DRE tokens received.
    """
    try:
        # Validate input types
        if not isinstance(ftm_amount, (float, int)) or not isinstance(exchange_rate, (float, int)):
            raise ValueError("Both FTM amount and the exchange rate must be numeric values.")
        
        if ftm_amount <= 0 or exchange_rate <= 0:
            raise ValueError("Both FTM amount and exchange rate must be positive numbers.")
        
        # Calculate the number of DRE tokens
        dre_tokens = ftm_amount * exchange_rate
        return dre_tokens
    except Exception as e:
        # Handle unexpected errors
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to handle user input and call the calculation function.
    """
    print("Welcome to the DRE Token Presale Calculator!")

    try:
        # Prompt user for input
        ftm_amount = float(input("Enter the amount of FTM you want to contribute: "))
        exchange_rate = float(input("Enter the exchange rate (FTM -> DRE): "))
        
        # Calculate DRE tokens
        dre_tokens = calculate_dre_tokens(ftm_amount, exchange_rate)
        
        # Display the result
        print(f"You will receive {dre_tokens:.2f} DRE tokens for your {ftm_amount:.2f} FTM contribution.")
    except ValueError:
        # Handle invalid input
        print("Invalid input. Please enter numeric values for FTM amount and exchange rate.")
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Execute the script
    main()
```
