"""
Generated Code Metadata:
========================
Original URL: https://jessecoin-1sa.pages.dev
Prompt: Create a simple calculator in code that determines how many JESSE tokens can be purchased with a specified amount of BASE at the different rates provided (e.g., 25 BASE, 50 BASE, etc.).
Generated: DETERMINISTIC_35416e80b8069db5
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Simple Calculator for JESSE Token Purchase
# This script calculates how many JESSE tokens can be purchased with a specified amount of BASE
# at different rates provided.

def calculate_tokens(base_amount, rates):
    """
    Calculate the number of JESSE tokens that can be purchased for a given BASE amount.

    Parameters:
        base_amount (float): The amount of BASE available for purchasing.
        rates (list): A list of rates (BASE per JESSE token).

    Returns:
        dict: A dictionary where keys are rates and values are the number of JESSE tokens purchasable.
    """
    if base_amount <= 0:
        raise ValueError("BASE amount must be greater than zero.")
    if not rates or not all(rate > 0 for rate in rates):
        raise ValueError("Rates must be a non-empty list of positive numbers.")

    # Calculate tokens for each rate
    tokens = {}
    for rate in rates:
        tokens[rate] = base_amount / rate  # Number of JESSE tokens purchasable at the given rate
    return tokens


def main():
    """
    Main function to interact with the user and calculate JESSE tokens.
    """
    try:
        # Input: Amount of BASE available
        base_amount = float(input("Enter the amount of BASE you have: "))
        
        # Input: Rates (BASE per JESSE token)
        rates_input = input("Enter the rates (comma-separated, e.g., 25,50,100): ")
        rates = [float(rate.strip()) for rate in rates_input.split(",")]

        # Calculate tokens
        tokens = calculate_tokens(base_amount, rates)

        # Display results
        print("\nResults:")
        for rate, token_count in tokens.items():
            print(f"At rate {rate} BASE per JESSE token, you can purchase {token_count:.2f} JESSE tokens.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
