"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdcoinmixer.com
Prompt: Write a Python script to calculate transaction fees for a USDC mixing service, taking into account the amount and complexity of the mixing process, as outlined by USDC Mixer.
Generated: DETERMINISTIC_feb14f17488f76bc
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
USDC Mixing Service Fee Calculator

This script calculates transaction fees for a USDC mixing service based on
the transaction amount and complexity of the mixing process. 

The fee structure is as follows:
1. Base fee of 0.5% of the transaction amount.
2. Additional complexity fee:
   - Low complexity: 0.1% of the transaction amount.
   - Medium complexity: 0.3% of the transaction amount.
   - High complexity: 0.5% of the transaction amount.
"""

def calculate_transaction_fee(amount, complexity):
    """
    Calculate the transaction fees for the USDC mixing service.

    Args:
        amount (float): The amount of USDC being mixed. Must be > 0.
        complexity (str): The complexity of the mixing process. 
                          Can be 'low', 'medium', or 'high'.

    Returns:
        float: The total transaction fee in USDC.

    Raises:
        ValueError: If the amount is <= 0 or complexity is invalid.
    """
    # Validate input
    if amount <= 0:
        raise ValueError("Transaction amount must be greater than 0.")
    
    if complexity not in ['low', 'medium', 'high']:
        raise ValueError("Invalid complexity level. Must be 'low', 'medium', or 'high'.")

    # Base fee: 0.5% of the amount
    base_fee_rate = 0.005
    base_fee = base_fee_rate * amount

    # Complexity fee based on mixing complexity
    complexity_fee_rates = {
        'low': 0.001,   # 0.1%
        'medium': 0.003, # 0.3%
        'high': 0.005   # 0.5%
    }
    complexity_fee = complexity_fee_rates[complexity] * amount

    # Total fee
    total_fee = base_fee + complexity_fee
    return total_fee


def main():
    """
    Main function for interacting with the fee calculator.
    """
    print("Welcome to the USDC Mixing Service Fee Calculator!")
    
    try:
        # Get user input
        amount = float(input("Enter the USDC transaction amount: "))
        complexity = input("Enter the mixing complexity level ('low', 'medium', 'high'): ").strip().lower()

        # Calculate fees
        total_fee = calculate_transaction_fee(amount, complexity)

        # Display the result
        print(f"\nTransaction Amount: {amount:.2f} USDC")
        print(f"Mixing Complexity: {complexity.capitalize()}")
        print(f"Total Fee: {total_fee:.2f} USDC")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
