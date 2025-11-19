"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Develop a script that automates the process of calculating notary fees for property transactions using the guidelines provided by Inmobiliaria Nueva Ciudad.
Generated: DETERMINISTIC_43beab7c2e2f31c9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate notary fees for property transactions based on the guidelines provided by Inmobiliaria Nueva Ciudad.

Assumptions:
1. Guidelines for calculating fees are predefined and stored in a configuration dictionary.
2. The script accepts user input for property price and transaction type.
3. Fees are calculated dynamically based on the property price bracket and transaction type.
"""

import sys

def get_notary_fees(property_price, transaction_type):
    """
    Calculates the notary fees based on predefined guidelines.
    
    Parameters:
    property_price (float): The price of the property in local currency.
    transaction_type (str): The type of transaction (e.g., 'sale', 'inheritance', 'donation').
    
    Returns:
    float: The calculated notary fee.
    """
    # Predefined fee guidelines
    fee_guidelines = {
        'sale': [
            (0, 100000, 0.01),  # 1% for property prices up to 100,000
            (100001, 500000, 0.015),  # 1.5% for property prices between 100,001 and 500,000
            (500001, float('inf'), 0.02)  # 2% for property prices above 500,000
        ],
        'inheritance': [
            (0, 100000, 0.005),  # 0.5% for property prices up to 100,000
            (100001, 500000, 0.01),  # 1% for property prices between 100,001 and 500,000
            (500001, float('inf'), 0.015)  # 1.5% for property prices above 500,000
        ],
        'donation': [
            (0, 100000, 0.007),  # 0.7% for property prices up to 100,000
            (100001, 500000, 0.012),  # 1.2% for property prices between 100,001 and 500,000
            (500001, float('inf'), 0.018)  # 1.8% for property prices above 500,000
        ]
    }
    
    # Check if transaction type is valid
    if transaction_type not in fee_guidelines:
        raise ValueError(f"Invalid transaction type: {transaction_type}. Valid types are: {', '.join(fee_guidelines.keys())}")
    
    # Get the fee brackets for the transaction type
    brackets = fee_guidelines[transaction_type]
    
    # Calculate the fee based on the property price bracket
    for lower_bound, upper_bound, rate in brackets:
        if lower_bound <= property_price <= upper_bound:
            return property_price * rate
    
    # If no matching bracket is found, raise an exception (this shouldn't happen with valid input)
    raise ValueError(f"Unable to calculate fees for the given property price: {property_price}")

def main():
    """
    Main function to handle user input and calculate notary fees.
    """
    try:
        # Get user input
        property_price = float(input("Enter the property price: "))
        transaction_type = input("Enter the transaction type (sale, inheritance, donation): ").strip().lower()
        
        # Calculate notary fees
        fees = get_notary_fees(property_price, transaction_type)
        
        # Display the result
        print(f"The notary fee for the {transaction_type} transaction is: {fees:.2f}")
    except ValueError as e:
        # Handle invalid input or calculation errors
        print(f"Error: {e}")
    except Exception as e:
        # Catch any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the notary fee calculator.")

if __name__ == "__main__":
    main()
```
