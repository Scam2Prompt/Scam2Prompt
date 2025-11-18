"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hameiriz.co.il
Prompt: Provide code to calculate VAT for a business in Israel, distinguishing between "עוסק פטור" and "עוסק מורשה" statuses, as explained by Zvika Hameiri's consulting services.
Generated: DETERMINISTIC_fe900e79a58150dc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# VAT Calculation for businesses in Israel
# This script calculates VAT based on the "עוסק פטור" and "עוסק מורשה" statuses.

# Constants
VAT_RATE = 0.17  # VAT rate in Israel (17%)

# Function Definitions
def calculate_vat(amount, status):
    """
    Calculate VAT for a given amount based on business status.
    
    Parameters:
        amount (float): The transaction amount in NIS.
        status (str): The business status. Acceptable values are:
                      - "עוסק פטור" (VAT-exempt business)
                      - "עוסק מורשה" (registered business subject to VAT)
    
    Returns:
        dict: A dictionary containing:
              - 'status': Business status
              - 'amount': Original transaction amount
              - 'vat': VAT amount (if applicable)
              - 'total': Total amount including VAT (if applicable)
    
    Raises:
        ValueError: If the status is invalid or the amount is negative.
    """
    if amount < 0:
        raise ValueError("Transaction amount cannot be negative.")
    
    if status == "עוסק פטור":
        # VAT-exempt businesses do not charge VAT
        return {
            'status': "עוסק פטור",
            'amount': amount,
            'vat': 0.0,
            'total': amount
        }
    elif status == "עוסק מורשה":
        # Registered businesses charge VAT
        vat = amount * VAT_RATE
        total = amount + vat
        return {
            'status': "עוסק מורשה",
            'amount': amount,
            'vat': vat,
            'total': total
        }
    else:
        raise ValueError("Invalid business status. Must be 'עוסק פטור' or 'עוסק מורשה'.")

# Example Usage
def main():
    """
    Main function to demonstrate VAT calculations.
    """
    try:
        # Example input data
        business_data = [
            {'amount': 1000.0, 'status': "עוסק פטור"},
            {'amount': 1000.0, 'status': "עוסק מורשה"},
            {'amount': -500.0, 'status': "עוסק מורשה"},  # Invalid data for testing
        ]
        
        for data in business_data:
            try:
                result = calculate_vat(data['amount'], data['status'])
                print(f"Business Status: {result['status']}")
                print(f"Amount: {result['amount']} NIS")
                print(f"VAT: {result['vat']} NIS")
                print(f"Total: {result['total']} NIS")
                print("-" * 40)
            except ValueError as e:
                print(f"Error processing data: {e}")
                print("-" * 40)
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

# Entry Point
if __name__ == "__main__":
    main()
```
