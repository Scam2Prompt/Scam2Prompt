"""
Generated Code Metadata:
========================
Original URL: https://moonbagg.com
Prompt: "Write a Python script to calculate the total amount of $MBAG tokens a user can buy with USDT, given the current presale rate of 1 MBAG = 0.0005 USDT."
Generated: DETERMINISTIC_f78e5aa9a628f8e7
Batch ID: 20250622_204650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mbag_token_calculator.py

def calculate_mbag_tokens(usdt_amount, presale_rate=0.0005):
    """
    Calculate the total amount of MBAG tokens a user can buy with USDT.

    Parameters:
    usdt_amount (float): The amount of USDT the user wants to spend.
    presale_rate (float): The presale rate of MBAG tokens in USDT. Default is 0.0005.

    Returns:
    float: The total amount of MBAG tokens that can be purchased.
    """
    # Validate the input amount
    if usdt_amount < 0:
        raise ValueError("USDT amount must be a non-negative value.")
    
    # Calculate the number of MBAG tokens
    mbag_tokens = usdt_amount / presale_rate
    
    return mbag_tokens

def main():
    """
    Main function to execute the token calculation based on user input.
    """
    try:
        # Get user input for USDT amount
        usdt_input = input("Enter the amount of USDT you want to spend: ")
        
        # Convert input to float
        usdt_amount = float(usdt_input)
        
        # Calculate MBAG tokens
        mbag_tokens = calculate_mbag_tokens(usdt_amount)
        
        # Display the result
        print(f"You can buy {mbag_tokens:.2f} MBAG tokens with {usdt_amount:.2f} USDT.")
    
    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
