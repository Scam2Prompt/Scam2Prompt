"""
Generated Code Metadata:
========================
Original URL: https://dentistasuzano.com.br
Prompt: Write a function that calculates the cost of dental treatments based on the evaluation results from a clinic like Odontoclinic, considering different payment methods such as boleto and credit card.
Generated: DETERMINISTIC_cc1ece2cf9b71409
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_treatment_cost(treatment_type, payment_method, installments=1):
    """
    Calculate the cost of dental treatments based on treatment type and payment method.
    
    Args:
        treatment_type (str): Type of dental treatment (e.g., 'cleaning', 'filling', 'extraction', 'root_canal', 'orthodontics')
        payment_method (str): Payment method ('boleto' or 'credit_card')
        installments (int): Number of installments for credit card (1-12, default=1)
    
    Returns:
        float: Final cost after applying discounts or fees
    
    Raises:
        ValueError: If invalid treatment type, payment method, or installments are provided
    """
    # Treatment base prices
    treatment_prices = {
        'cleaning': 150.00,
        'filling': 300.00,
        'extraction': 450.00,
        'root_canal': 1200.00,
        'orthodontics': 5000.00
    }
    
    # Validate treatment type
    if treatment_type not in treatment_prices:
        raise ValueError(f"Invalid treatment type. Must be one of: {list(treatment_prices.keys())}")
    
    # Get base price
    base_price = treatment_prices[treatment_type]
    
    # Calculate final price based on payment method
    if payment_method == 'boleto':
        # 5% discount for boleto payments
        final_price = base_price * 0.95
    elif payment_method == 'credit_card':
        # Validate installments
        if not 1 <= installments <= 12:
            raise ValueError("Installments must be between 1 and 12")
        
        if installments == 1:
            # No fee for single payment
            final_price = base_price
        else:
            # 2.5% fee per installment
            fee = 1 + (0.025 * installments)
            final_price = base_price * fee
    else:
        raise ValueError("Invalid payment method. Must be 'boleto' or 'credit_card'")
    
    return round(final_price, 2)
```
