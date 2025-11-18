"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinmixer.cx
Prompt: Write a program that calculates the service fee for a Bitcoin mixer transaction based on the percentage model described on bitcoinmixer.cx, and outputs the amount of Bitcoin to be received after mixing.
Generated: DETERMINISTIC_9d7f697727e935b8
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate service fee for a Bitcoin mixer transaction based on a percentage model
# and outputs the amount of Bitcoin to be received after mixing.

def calculate_bitcoin_received(amount_btc, fee_percentage):
    """
    Calculate the amount of Bitcoin received after mixing.

    :param amount_btc: float - The total amount of Bitcoin sent for mixing.
    :param fee_percentage: float - The service fee percentage charged by the mixer.
    :return: float - The amount of Bitcoin received after deducting the service fee.
    """
    try:
        # Validate input values
        if amount_btc <= 0:
            raise ValueError("Bitcoin amount must be greater than 0.")
        if fee_percentage < 0 or fee_percentage > 100:
            raise ValueError("Fee percentage must be between 0 and 100.")

        # Calculate the service fee in Bitcoin
        service_fee = (fee_percentage / 100) * amount_btc

        # Calculate the amount to be received after mixing
        amount_received = amount_btc - service_fee

        return amount_received

    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error: {e}")
        return None


def main():
    """
    Main function to run the Bitcoin mixer fee calculation program.
    """
    # Prompt user for input
    try:
        amount_btc = float(input("Enter the amount of Bitcoin sent for mixing: "))
        fee_percentage = float(input("Enter the service fee percentage: "))

        # Calculate the amount received
        amount_received = calculate_bitcoin_received(amount_btc, fee_percentage)

        # Output the result if calculation is successful
        if amount_received is not None:
            print(f"Amount of Bitcoin to be received after mixing: {amount_received:.8f} BTC")
    except ValueError:
        print("Error: Please enter valid numeric values for Bitcoin amount and fee percentage.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


if __name__ == "__main__":
    # Execute the program
    main()
```
