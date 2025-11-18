"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-srunexyz.pages.dev
Prompt: Write a script in Python to calculate the amount of $SRUNE tokens received for a given amount of SOL based on the exchange rate provided on the $SRUNE pre-sale page (1 SOL = 99,500 $SRUNE).
Generated: DETERMINISTIC_5128c07e36ba045b
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the number of $SRUNE tokens received for a given amount of SOL.
Exchange rate: 1 SOL = 99,500 $SRUNE.

Requirements:
- User inputs the amount of SOL.
- Script calculates and displays the equivalent amount of $SRUNE.
- Proper error handling to manage invalid inputs.
"""

def calculate_srune(sol_amount, exchange_rate=99500):
    """
    Calculate the amount of $SRUNE tokens for the given SOL amount.
    
    Parameters:
        sol_amount (float): The amount of SOL provided.
        exchange_rate (int): The exchange rate (default is 99,500).
    
    Returns:
        float: The equivalent amount of $SRUNE tokens.
    """
    return sol_amount * exchange_rate

def main():
    """
    Main function to handle user input and display the output.
    """
    print("Welcome to the $SRUNE Pre-sale Calculator!")
    print("Exchange Rate: 1 SOL = 99,500 $SRUNE")

    try:
        # Prompt user for the amount of SOL
        sol_input = input("Please enter the amount of SOL you'd like to exchange: ")
        
        # Convert input to float and validate
        sol_amount = float(sol_input)
        if sol_amount <= 0:
            raise ValueError("The amount of SOL should be greater than zero.")
        
        # Calculate and display the equivalent $SRUNE tokens
        srune_amount = calculate_srune(sol_amount)
        print(f"For {sol_amount:.2f} SOL, you will receive {srune_amount:.2f} $SRUNE tokens.")
    
    except ValueError as e:
        # Handle invalid input (e.g., non-numeric or negative values)
        print(f"Error: {e}. Please enter a valid numeric amount greater than zero.")
    except Exception as e:
        # Handle other unexpected errors
        print(f"An unexpected error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
```
