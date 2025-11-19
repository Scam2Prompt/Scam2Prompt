"""
Generated Code Metadata:
========================
Original URL: https://mixers.money
Prompt: Generate code to calculate the commission fees (1-1.5% + 0.00035 BTC or 4-5% + 0.0007 BTC) for transactions processed through mixers.money, and display the total cost for a given Bitcoin amount.
Generated: DETERMINISTIC_55b63940d3192e5f
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import decimal

def calculate_commission(amount_btc, is_high_risk=False):
    """
    Calculate the commission fees for transactions processed through mixers.money.
    
    Args:
        amount_btc (decimal.Decimal): Bitcoin amount to process
        is_high_risk (bool): Whether the transaction is high risk (default False)
        
    Returns:
        dict: {
            'base_percentage': decimal.Decimal,
            'fixed_fee': decimal.Decimal,
            'total_commission': decimal.Decimal,
            'total_cost': decimal.Decimal
        }
        
    Raises:
        ValueError: If amount_btc is not positive
    """
    # Validate input
    if amount_btc <= decimal.Decimal('0'):
        raise ValueError("Bitcoin amount must be positive")
    
    # Set commission parameters based on risk level
    if is_high_risk:
        base_percentage_min = decimal.Decimal('0.04')  # 4%
        base_percentage_max = decimal.Decimal('0.05')  # 5%
        fixed_fee = decimal.Decimal('0.0007')          # 0.0007 BTC
    else:
        base_percentage_min = decimal.Decimal('0.01')  # 1%
        base_percentage_max = decimal.Decimal('0.015') # 1.5%
        fixed_fee = decimal.Decimal('0.00035')         # 0.00035 BTC
    
    # Calculate average percentage for simplicity (or could make this configurable)
    base_percentage = (base_percentage_min + base_percentage_max) / 2
    
    # Calculate commission components
    percentage_fee = amount_btc * base_percentage
    total_commission = percentage_fee + fixed_fee
    total_cost = amount_btc + total_commission
    
    return {
        'base_percentage': base_percentage,
        'fixed_fee': fixed_fee,
        'total_commission': total_commission,
        'total_cost': total_cost
    }

def display_transaction_cost(amount_btc, is_high_risk=False):
    """
    Display the transaction cost breakdown for a given Bitcoin amount.
    
    Args:
        amount_btc (decimal.Decimal or str): Bitcoin amount to process
        is_high_risk (bool): Whether the transaction is high risk (default False)
    """
    try:
        # Convert to Decimal if needed
        if not isinstance(amount_btc, decimal.Decimal):
            amount_btc = decimal.Decimal(str(amount_btc))
        
        # Calculate commission
        result = calculate_commission(amount_btc, is_high_risk)
        
        # Display results
        risk_level = "High Risk" if is_high_risk else "Standard"
        print(f"\nTransaction Cost Breakdown ({risk_level})")
        print("=" * 40)
        print(f"Input Amount:        {amount_btc:.8f} BTC")
        print(f"Base Percentage:     {result['base_percentage'] * 100:.2f}%")
        print(f"Percentage Fee:      {amount_btc * result['base_percentage']:.8f} BTC")
        print(f"Fixed Fee:           {result['fixed_fee']:.8f} BTC")
        print(f"Total Commission:    {result['total_commission']:.8f} BTC")
        print("-" * 40)
        print(f"Total Cost:          {result['total_cost']:.8f} BTC")
        print("=" * 40)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Set precision for decimal operations
    decimal.getcontext().prec = 8
    
    # Test cases
    test_amounts = [
        decimal.Decimal('0.5'),
        decimal.Decimal('1.0'),
        decimal.Decimal('2.5')
    ]
    
    for amount in test_amounts:
        display_transaction_cost(amount)
        display_transaction_cost(amount, is_high_risk=True)
```
