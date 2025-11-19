"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: Create a function to evaluate the total funding required for a real estate project, incorporating Appak Capital's fix-and-flip loan terms (100% purchase price, 100% rehab, and up to 75% ARV).
Generated: DETERMINISTIC_84a7bea4f5f30f51
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_funding_required(purchase_price, rehab_cost, after_repair_value):
    """
    Calculate the total funding required for a real estate project based on Appak Capital's loan terms.
    
    Args:
        purchase_price (float): The purchase price of the property.
        rehab_cost (float): The estimated cost of rehabilitation.
        after_repair_value (float): The estimated after-repair value (ARV) of the property.
    
    Returns:
        dict: A dictionary containing:
            - 'total_funding': Total funding required (purchase + rehab)
            - 'max_loan_amount': Maximum loan amount (75% of ARV)
            - 'is_approved': Boolean indicating if loan covers total funding
    
    Raises:
        ValueError: If any input is negative.
    """
    
    # Validate inputs
    if any(val < 0 for val in [purchase_price, rehab_cost, after_repair_value]):
        raise ValueError("All input values must be non-negative")
    
    # Calculate total funding needed
    total_funding = purchase_price + rehab_cost
    
    # Calculate maximum loan amount (75% of ARV)
    max_loan_amount = 0.75 * after_repair_value
    
    # Determine if loan covers total funding
    is_approved = max_loan_amount >= total_funding
    
    return {
        'total_funding': total_funding,
        'max_loan_amount': max_loan_amount,
        'is_approved': is_approved
    }
```
