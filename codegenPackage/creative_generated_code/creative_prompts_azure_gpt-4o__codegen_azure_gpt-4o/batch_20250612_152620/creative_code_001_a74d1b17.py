"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trustpad-link.pages.dev
Prompt: Generate code to calculate the total number of O4DX tokens a user can purchase during the OrangeDX IDO on TrustPad, given a specific amount of USDT and the swap rate of 1 USDT = 11.7646 O4DX.
Generated: DETERMINISTIC_a74d1b176197c6c8
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the total number of O4DX tokens a user can purchase
# during the OrangeDX IDO on TrustPad, given a specific amount of USDT
# and the swap rate of 1 USDT = 11.7646 O4DX.

def calculate_tokens(usdt_amount, swap_rate):
    """
    Calculate the total number of O4DX tokens a user can purchase.

    Args:
        usdt_amount (float): The amount of USDT the user wants to spend.
        swap_rate (float): The rate of O4DX tokens per 1 USDT.

    Returns:
        float: The total number of O4DX tokens the user can purchase.
    """
    try:
        # Validate input data
        if usdt_amount < 0:
            raise ValueError("USDT amount must be non-negative.")
        if swap_rate <= 0:
            raise ValueError("Swap rate must be greater than zero.")

        # Calculate the total number of O4DX tokens
        o4dx_tokens = usdt_amount * swap_rate
        return o4dx_tokens
    
    except ValueError as e:
        # Handle invalid input and return an error message
        print(f"Error: {e}")
        return None


def main():
    """
    Main function to interact with the user and calculate O4DX token purchases.
    """
    try:
        # Prompt user input for USDT amount
        usdt_amount = float(input("Enter the amount of USDT you want to spend: "))

        # Define the fixed swap rate
        SWAP_RATE = 11.7646  # 1 USDT = 11.7646 O4DX

        # Calculate the total tokens
        tokens = calculate_tokens(usdt_amount, SWAP_RATE)

        if tokens is not None:
            # Display the result to the user
            print(f"With {usdt_amount} USDT, you can purchase {tokens:.6f} O4DX tokens.")
        else:
            print("Failed to calculate tokens due to invalid input.")
    
    except ValueError:
        # Handle invalid user input
        print("Error: Please enter a valid numeric value for USDT.")

    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
