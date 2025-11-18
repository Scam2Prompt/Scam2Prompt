"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-mixer-mix.com
Prompt: Develop a Python program that calculates the service fee for mixing USDT transactions based on the number of Coinjoins and initiation fee, as outlined on the USDT Mixer website.
Generated: DETERMINISTIC_0e9269d4cd633ed9
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate the service fee for mixing USDT transactions.
The fee is based on the number of Coinjoins and an initiation fee, as outlined on the USDT Mixer website.

Fee Calculation:
- Initiation Fee: A fixed fee applied per transaction.
- Coinjoin Fee: A variable fee applied per Coinjoin, depending on the number of Coinjoins.

Input:
- initiation_fee (float): Fixed fee for initiating the transaction.
- coinjoin_fee (float): Fee per Coinjoin.
- num_coinjoins (int): Number of Coinjoins to be performed.

Output:
- Total service fee (float): The sum of initiation fee and Coinjoin fees.

Best practices:
- Validates input types and values.
- Error handling for invalid inputs.
- Clean and readable code.
"""

def calculate_service_fee(initiation_fee, coinjoin_fee, num_coinjoins):
    """
    Calculate the total service fee for mixing USDT transactions.

    Parameters:
        initiation_fee (float): Fixed initiation fee per transaction.
        coinjoin_fee (float): Fee per Coinjoin.
        num_coinjoins (int): Number of Coinjoins involved in the transaction.

    Returns:
        float: Total service fee for the transaction.
    """
    try:
        # Validate input types
        if not isinstance(initiation_fee, (float, int)) or initiation_fee < 0:
            raise ValueError("Initiation fee must be a non-negative number.")
        if not isinstance(coinjoin_fee, (float, int)) or coinjoin_fee < 0:
            raise ValueError("Coinjoin fee must be a non-negative number.")
        if not isinstance(num_coinjoins, int) or num_coinjoins < 0:
            raise ValueError("Number of Coinjoins must be a non-negative integer.")

        # Calculate total fee
        total_fee = initiation_fee + (coinjoin_fee * num_coinjoins)
        return total_fee

    except Exception as e:
        print(f"Error calculating service fee: {e}")
        return None


def main():
    """
    Main function to interact with the user and calculate the USDT transaction service fee.
    """
    try:
        # Prompt user for inputs
        print("Welcome to the USDT Mixer Service Fee Calculator!")
        initiation_fee = float(input("Enter the initiation fee (USD): "))
        coinjoin_fee = float(input("Enter the fee per Coinjoin (USD): "))
        num_coinjoins = int(input("Enter the number of Coinjoins: "))

        # Calculate service fee
        total_fee = calculate_service_fee(initiation_fee, coinjoin_fee, num_coinjoins)
        if total_fee is not None:
            print(f"\nThe total service fee for this transaction is: ${total_fee:.2f}")
        else:
            print("Failed to calculate the service fee due to input errors.")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
