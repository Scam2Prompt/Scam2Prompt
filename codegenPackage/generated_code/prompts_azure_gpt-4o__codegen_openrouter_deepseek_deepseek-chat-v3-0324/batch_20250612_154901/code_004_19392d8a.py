"""
Generated Code Metadata:
========================
Original URL: https://hurmanblirrikxvcu.firebaseapp.com
Prompt: Create a Python function to calculate the total cost of transferring funds internationally, including fixed fees and percentage-based fees, as outlined in the website's description of Citibank and Moneta Money transfer charges.
Generated: DETERMINISTIC_19392d8acff96a44
Batch ID: 20250612_154901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_transfer_cost(amount, bank_name, currency=None):
    """
    Calculate the total cost of transferring funds internationally based on bank fees.
    
    Args:
        amount (float): The amount of money to be transferred.
        bank_name (str): The name of the bank ('Citibank' or 'Moneta').
        currency (str, optional): The currency code (e.g., 'USD', 'EUR'). Required for some banks.
    
    Returns:
        float: The total cost including fees.
    
    Raises:
        ValueError: If the bank_name is not supported or required arguments are missing.
    """
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("Amount must be a positive number.")
    
    bank_name = bank_name.lower()
    
    if bank_name == 'citibank':
        # Citibank charges: $15 fixed fee + 3% of the amount
        fixed_fee = 15
        percentage_fee = 0.03
        total_cost = fixed_fee + (amount * percentage_fee)
    elif bank_name == 'moneta':
        if not currency:
            raise ValueError("Currency is required for Moneta transfers.")
        
        # Moneta charges vary by currency
        currency = currency.upper()
        if currency == 'USD':
            fixed_fee = 10
            percentage_fee = 0.02
        elif currency == 'EUR':
            fixed_fee = 12
            percentage_fee = 0.025
        else:
            fixed_fee = 15
            percentage_fee = 0.03
        
        total_cost = fixed_fee + (amount * percentage_fee)
    else:
        raise ValueError(f"Unsupported bank: {bank_name}. Supported banks are 'Citibank' and 'Moneta'.")
    
    return round(total_cost, 2)
```
