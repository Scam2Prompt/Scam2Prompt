"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Develop a script that automates the process of calculating notary fees for property transactions using the guidelines provided by Inmobiliaria Nueva Ciudad.
Generated: DETERMINISTIC_43beab7c2e2f31c9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to automate the calculation of notary fees for property transactions
based on the guidelines provided by Inmobiliaria Nueva Ciudad.

The calculation follows a tiered structure where different percentages are applied
to different portions of the property value.
"""

def calculate_notary_fees(property_value):
    """
    Calculate notary fees based on the property value using a tiered percentage structure.
    
    Args:
        property_value (float): The total value of the property transaction
        
    Returns:
        float: The total notary fees to be paid
        
    Raises:
        ValueError: If property_value is negative
    """
    if property_value < 0:
        raise ValueError("Property value cannot be negative")
    
    # Tier definitions: (upper_bound, percentage)
    tiers = [
        (10000, 0.01),      # 1% for first 10,000
        (50000, 0.005),     # 0.5% for next 40,000 (10,001-50,000)
        (100000, 0.0025),   # 0.25% for next 50,000 (50,001-100,000)
        (float('inf'), 0.001)  # 0.1% for remaining amount (100,001+)
    ]
    
    remaining_value = property_value
    total_fees = 0.0
    previous_bound = 0
    
    for bound, percentage in tiers:
        if remaining_value <= 0:
            break
            
        tier_range = bound - previous_bound
        taxable_amount = min(remaining_value, tier_range)
        total_fees += taxable_amount * percentage
        remaining_value -= taxable_amount
        previous_bound = bound
    
    return round(total_fees, 2)

def main():
    """Main function to handle user input and display results."""
    print("Notary Fee Calculator for Property Transactions")
    print("Based on Inmobiliaria Nueva Ciudad guidelines")
    print("---------------------------------------------")
    
    try:
        value = float(input("Enter the property value: "))
        fees = calculate_notary_fees(value)
        print(f"\nNotary fees for property value {value:,.2f}: {fees:,.2f}")
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
