"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proarteasa.com
Prompt: Write a Python script that calculates the total cost of purchasing a lot in Acacias Retiro Campestre, including financing options with 0% interest for up to 36 months.
Generated: DETERMINISTIC_c427261198ab4d19
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# acacias_retiro_cost_calculator.py

def calculate_total_cost(lot_price, down_payment_percentage, financing_months):
    """
    Calculate the total cost of purchasing a lot including financing options.

    Parameters:
    lot_price (float): The price of the lot.
    down_payment_percentage (float): The percentage of the down payment.
    financing_months (int): The number of months for financing (should not exceed 36).
    
    Returns:
    dict: A dictionary containing the down payment, financed amount, and monthly payment.
    
    Raises:
    ValueError: If the down payment percentage is not between 0 and 100 or if financing_months is not valid.
    """
    
    # Validate inputs
    if not (0 <= down_payment_percentage <= 100):
        raise ValueError("Down payment percentage must be between 0 and 100.")
    if financing_months < 1 or financing_months > 36:
        raise ValueError("Financing months must be between 1 and 36.")
    
    # Calculate down payment and financed amount
    down_payment = (down_payment_percentage / 100) * lot_price
    financed_amount = lot_price - down_payment
    
    # Calculate monthly payment
    monthly_payment = financed_amount / financing_months
    
    return {
        'down_payment': down_payment,
        'financed_amount': financed_amount,
        'monthly_payment': monthly_payment
    }

def main():
    """Main function to execute the cost calculation."""
    try:
        # User inputs
        lot_price = float(input("Enter the price of the lot ($): "))
        down_payment_percentage = float(input("Enter the down payment percentage (%): "))
        financing_months = int(input("Enter the number of months for financing (1-36): "))
        
        # Calculate costs
        result = calculate_total_cost(lot_price, down_payment_percentage, financing_months)
        
        # Output the results
        print("\n--- Purchase Summary ---")
        print(f"Down Payment: ${result['down_payment']:.2f}")
        print(f"Financed Amount: ${result['financed_amount']:.2f}")
        print(f"Monthly Payment: ${result['monthly_payment']:.2f}")
    
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
```
