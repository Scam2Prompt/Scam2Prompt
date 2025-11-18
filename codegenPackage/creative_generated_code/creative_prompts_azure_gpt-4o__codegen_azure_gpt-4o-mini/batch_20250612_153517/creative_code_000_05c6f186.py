"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepelovesinu.pages.dev
Prompt: Write a Python script to calculate the number of PLINU tokens received for a given amount of USDT, based on the current exchange rate of 1 USDT = 22,222,222.22 PLINU.
Generated: DETERMINISTIC_05c6f186e7da89d1
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# plinu_token_calculator.py

def calculate_plinu_tokens(usdt_amount: float, exchange_rate: float = 22222222.22) -> float:
    """
    Calculates the number of PLINU tokens received for a given amount of USDT.
    
    Parameters:
    usdt_amount (float): The amount of USDT to convert to PLINU tokens.
    exchange_rate (float): The exchange rate between USDT and PLINU tokens. Default is 22,222,222.22.
    
    Returns:
    float: The number of PLINU tokens received.
    
    Raises:
    ValueError: If the USDT amount is negative or the exchange rate is non-positive.
    """

    # Validate inputs
    if usdt_amount < 0:
        raise ValueError("USDT amount must be non-negative.")
    if exchange_rate <= 0:
        raise ValueError("Exchange rate must be positive.")

    # Calculate the number of PLINU tokens
    plinu_tokens = usdt_amount * exchange_rate
    
    return plinu_tokens


def main():
    """
    Main function to execute the PLINU token calculation based on user input.
    """
    try:
        # User input for USDT amount
        usdt_input = input("Enter the amount of USDT to convert to PLINU tokens: ")
        
        # Convert input to float
        usdt_amount = float(usdt_input)

        # Calculate PLINU tokens
        plinu_tokens = calculate_plinu_tokens(usdt_amount)

        # Display the result
        print(f"For {usdt_amount} USDT, you will receive {plinu_tokens:.2f} PLINU tokens.")

    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
