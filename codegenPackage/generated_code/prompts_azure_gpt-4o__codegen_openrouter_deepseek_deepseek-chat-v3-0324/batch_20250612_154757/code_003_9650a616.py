"""
Generated Code Metadata:
========================
Original URL: https://refund-me.net
Prompt: Create a Python script to calculate fees for a fraud recovery service, including a 15% success fee plus VAT, based on the recovered amount.
Generated: DETERMINISTIC_9650a6168809f6f6
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_fees(recovered_amount, vat_rate=0.2):
    """
    Calculate the total fees for fraud recovery service.
    
    Args:
        recovered_amount (float): The amount recovered from fraud.
        vat_rate (float, optional): VAT rate as decimal (e.g., 0.2 for 20%). Defaults to 0.2.
    
    Returns:
        dict: Dictionary containing:
            - success_fee: 15% of recovered amount
            - vat_amount: VAT on success fee
            - total_fees: success_fee + vat_amount
            - original_amount: input recovered_amount
    
    Raises:
        ValueError: If recovered_amount is negative or non-numeric
    """
    try:
        # Validate input
        if not isinstance(recovered_amount, (int, float)):
            raise ValueError("Recovered amount must be numeric")
        if recovered_amount < 0:
            raise ValueError("Recovered amount cannot be negative")
        
        # Calculate fees
        success_fee = recovered_amount * 0.15
        vat_amount = success_fee * vat_rate
        total_fees = success_fee + vat_amount
        
        return {
            "original_amount": recovered_amount,
            "success_fee": round(success_fee, 2),
            "vat_amount": round(vat_amount, 2),
            "total_fees": round(total_fees, 2),
            "vat_rate": vat_rate
        }
    
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise ValueError(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        recovered = float(input("Enter the recovered amount: "))
        result = calculate_fees(recovered)
        print("\nFee Calculation Results:")
        print(f"Original Amount: £{result['original_amount']:,.2f}")
        print(f"Success Fee (15%): £{result['success_fee']:,.2f}")
        print(f"VAT ({result['vat_rate']*100:.0f}%): £{result['vat_amount']:,.2f}")
        print(f"Total Fees: £{result['total_fees']:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
