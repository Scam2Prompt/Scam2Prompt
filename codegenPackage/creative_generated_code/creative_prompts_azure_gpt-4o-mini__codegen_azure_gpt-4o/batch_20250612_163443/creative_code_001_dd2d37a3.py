"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superintelligence-po6.pages.dev
Prompt: Write a code snippet to facilitate the migration of AGIX tokens to FET at the conversion rate of 1 AGIX to 0.433350 FET.
Generated: DETERMINISTIC_dd2d37a35f70f379
Batch ID: 20250612_163443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

def migrate_tokens(agix_amount):
    """
    Function to perform the migration of AGIX tokens to FET tokens.

    Args:
        agix_amount (float): The amount of AGIX tokens to be converted.

    Returns:
        float: Equivalent amount of FET tokens after conversion.
    
    Raises:
        ValueError: If the AGIX amount provided is invalid (negative or non-numeric).
    """
    try:
        # Validate input
        agix_amount = decimal.Decimal(agix_amount)
        if agix_amount < 0:
            raise ValueError("AGIX amount cannot be negative.")
        
        # Conversion rate: 1 AGIX = 0.433350 FET
        conversion_rate = decimal.Decimal('0.433350')
        
        # Perform conversion
        fet_amount = agix_amount * conversion_rate
        
        # Return the FET amount rounded to 6 decimal places
        return round(fet_amount, 6)
    
    except decimal.InvalidOperation:
        raise ValueError("Invalid AGIX amount provided. Please enter a numeric value.")


if __name__ == "__main__":
    # Example usage
    try:
        agix_amount = input("Enter the amount of AGIX tokens to migrate: ")
        fet_amount = migrate_tokens(agix_amount)
        print(f"Equivalent FET tokens: {fet_amount}")
    except ValueError as e:
        print(f"Error: {e}")
```
