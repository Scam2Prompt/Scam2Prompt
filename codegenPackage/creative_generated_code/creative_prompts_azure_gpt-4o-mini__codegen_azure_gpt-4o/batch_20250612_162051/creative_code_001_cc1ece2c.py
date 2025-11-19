"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dentistasuzano.com.br
Prompt: Write a function that calculates the cost of dental treatments based on the evaluation results from a clinic like Odontoclinic, considering different payment methods such as boleto and credit card.
Generated: DETERMINISTIC_cc1ece2cf9b71409
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict

def calculate_treatment_cost(evaluation: Dict[str, float], payment_method: str) -> float:
    """
    Calculate the cost of dental treatments based on evaluation results and payment method.

    Args:
        evaluation (Dict[str, float]): A dictionary containing treatment types and their base costs.
                                       Example: {'cleaning': 100.0, 'whitening': 300.0}
        payment_method (str): Payment method to be used. Options: 'boleto', 'credit_card'.

    Returns:
        float: The total cost of treatments after applying payment method adjustments.

    Raises:
        ValueError: If the payment method is invalid.
    """
    # Check if evaluation is valid
    if not evaluation or not isinstance(evaluation, dict):
        raise ValueError("Evaluation must be a dictionary with treatment types and costs.")

    # Supported payment methods and their discount/surcharge rates
    payment_adjustments = {
        'boleto': 0.9,        # 10% discount for boleto
        'credit_card': 1.05   # 5% surcharge for credit card
    }

    # Validate payment method
    if payment_method not in payment_adjustments:
        raise ValueError(f"Invalid payment method. Must be one of: {', '.join(payment_adjustments.keys())}")

    # Calculate the base cost of all treatments
    base_cost = sum(evaluation.values())
    
    # Apply the adjustment based on the payment method
    adjusted_cost = base_cost * payment_adjustments[payment_method]

    return round(adjusted_cost, 2)


# Example usage (Uncomment the lines below to test the function):
# treatments = {'cleaning': 100.0, 'whitening': 300.0, 'filling': 150.0}
# payment_type = 'credit_card'
# total_cost = calculate_treatment_cost(treatments, payment_type)
# print(f"Total cost for {payment_type}: ${total_cost}")
```
