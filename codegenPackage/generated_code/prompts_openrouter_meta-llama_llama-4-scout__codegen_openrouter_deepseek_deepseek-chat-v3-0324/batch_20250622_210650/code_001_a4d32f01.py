"""
Generated Code Metadata:
========================
Original URL: https://proarteasa.com
Prompt: "Write a Python script to calculate the investment returns for buying a lot in Acacias Retiro Campestre, considering a 36-month payment plan with 0% interest."
Generated: DETERMINISTIC_a4d32f011906a5fd
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_investment_returns(total_amount, months=36):
    """
    Calculate monthly payments for a 36-month payment plan with 0% interest.
    
    Args:
        total_amount (float): Total amount to be paid for the lot.
        months (int, optional): Number of months for payment plan. Defaults to 36.
    
    Returns:
        dict: Dictionary containing payment details including monthly payment amount,
              total amount, and number of months.
    """
    try:
        if not isinstance(total_amount, (int, float)) or total_amount <= 0:
            raise ValueError("Total amount must be a positive number")
        if not isinstance(months, int) or months <= 0:
            raise ValueError("Months must be a positive integer")
        
        monthly_payment = total_amount / months
        
        return {
            'total_amount': total_amount,
            'monthly_payment': round(monthly_payment, 2),
            'months': months,
            'interest_rate': '0%'
        }
    except ValueError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': f"An unexpected error occurred: {str(e)}"}


if __name__ == "__main__":
    # Example usage
    try:
        total = float(input("Enter the total amount for the lot: "))
        result = calculate_investment_returns(total)
        
        if 'error' in result:
            print(f"Error: {result['error']}")
        else:
            print("\nPayment Plan Details:")
            print(f"Total Amount: ${result['total_amount']:,.2f}")
            print(f"Monthly Payment: ${result['monthly_payment']:,.2f}")
            print(f"Number of Months: {result['months']}")
            print(f"Interest Rate: {result['interest_rate']}")
    except ValueError:
        print("Error: Please enter a valid number for the total amount.")
```
