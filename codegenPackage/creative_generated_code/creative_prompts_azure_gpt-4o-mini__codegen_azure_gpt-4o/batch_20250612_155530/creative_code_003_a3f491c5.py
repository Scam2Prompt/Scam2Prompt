"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-coin-mixer.com
Prompt: What are the steps to calculate the fees for mixing TONCOIN using the TONCOIN Mixer, and can you provide a sample calculation?
Generated: DETERMINISTIC_a3f491c5177ff37b
Batch ID: 20250612_155530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script calculates the fees for mixing TONCOIN using a TONCOIN Mixer.
The fee calculation involves:
1. Defining the base fee rate and service fee percentages.
2. Applying the fee structure to the amount being mixed.
3. Returning the total fees and the resulting amount after fees.

Assumptions:
- Base fee rate (flat fee) is 0.5 TONCOIN.
- Service fee percentage is 1% of the input amount.
"""

def calculate_mixing_fees(amount):
    """
    Calculates the fees and final amount after using the TONCOIN Mixer.

    Parameters:
        amount (float): The amount of TONCOIN to be mixed.

    Returns:
        dict: A dictionary containing:
            - 'base_fee': Flat fee (fixed).
            - 'service_fee': Percentage-based service fee.
            - 'total_fees': Sum of base_fee and service_fee.
            - 'final_amount': Amount after deducting total fees.
    """
    try:
        # Validate input
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        # Define fee rates
        base_fee = 0.5  # Flat fee in TONCOIN
        service_fee_percentage = 0.01  # 1% of the amount

        # Calculate fees
        service_fee = amount * service_fee_percentage
        total_fees = base_fee + service_fee
        final_amount = amount - total_fees

        # If final amount is negative, raise an error
        if final_amount < 0:
            raise ValueError("The fees exceed the input amount. Please provide a larger amount.")

        return {
            'base_fee': round(base_fee, 6),
            'service_fee': round(service_fee, 6),
            'total_fees': round(total_fees, 6),
            'final_amount': round(final_amount, 6)
        }

    except ValueError as ve:
        # Handle invalid input gracefully
        return {'error': str(ve)}

    except Exception as e:
        # Catch-all for unexpected errors
        return {'error': f"An unexpected error occurred: {str(e)}"}


# Example usage
if __name__ == "__main__":
    # Sample input amount
    input_amount = 100.0  # TONCOIN to be mixed

    # Calculate fees
    fees_details = calculate_mixing_fees(input_amount)

    # Output result
    if 'error' in fees_details:
        print(f"Error: {fees_details['error']}")
    else:
        print("Mixing Fee Calculation:")
        print(f"Base Fee: {fees_details['base_fee']} TONCOIN")
        print(f"Service Fee: {fees_details['service_fee']} TONCOIN")
        print(f"Total Fees: {fees_details['total_fees']} TONCOIN")
        print(f"Final Amount: {fees_details['final_amount']} TONCOIN")
```
