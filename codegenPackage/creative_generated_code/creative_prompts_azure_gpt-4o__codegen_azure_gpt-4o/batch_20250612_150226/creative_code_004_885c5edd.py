"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiavwskgiww3elpabxoxlcv3n46mhlr4fohrwq3gyojtkwmivmo2bu.ipfs.dweb.link
Prompt: Write code to calculate the number of $BCKR tokens received for different ETH deposit amounts during the presale, referencing the conversion rate of 0.1 ETH = 99,500 BCKR.
Generated: DETERMINISTIC_885c5edd8833d9d6
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the number of BCKR tokens received for ETH deposits during the presale.

def calculate_bckr_tokens(eth_amount):
    """
    Calculates the number of BCKR tokens based on the ETH deposit amount.

    Conversion rate:
    0.1 ETH = 99,500 BCKR
    Thus, 1 ETH = 995,000 BCKR.

    Args:
        eth_amount (float): The amount of ETH deposited.

    Returns:
        float: The number of BCKR tokens received.
    """
    try:
        # Conversion rate: 1 ETH = 995,000 BCKR
        conversion_rate = 995_000
        
        # Validate the input is a positive number
        if eth_amount <= 0:
            raise ValueError("ETH deposit amount must be greater than 0.")

        # Calculate and return the BCKR tokens
        bckr_tokens = eth_amount * conversion_rate
        return bckr_tokens

    except TypeError:
        raise TypeError("ETH deposit amount must be a numeric value.")
    except ValueError as ve:
        raise ve


def main():
    """
    Main function to demonstrate the calculation of BCKR tokens for ETH deposits.
    """
    print("Welcome to the BCKR Token Presale Calculator!")
    print("Conversion rate: 0.1 ETH = 99,500 BCKR (1 ETH = 995,000 BCKR)\n")

    try:
        # Input: ETH deposit amount
        eth_amount = float(input("Enter the amount of ETH you wish to deposit: "))

        # Calculate BCKR tokens
        bckr_tokens = calculate_bckr_tokens(eth_amount)

        # Display the result
        print(f"\nFor {eth_amount} ETH, you will receive {bckr_tokens:,.2f} BCKR tokens.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
