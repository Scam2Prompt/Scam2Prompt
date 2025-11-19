"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: Create a function to check the warranty status of automotive parts, inspired by the warranty features offered by یاتاقان گلدن.
Generated: DETERMINISTIC_0f93c30591e135f1
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

def check_warranty_status(part_name, purchase_date, warranty_period_months):
    """
    Function to check the warranty status of an automotive part.

    Args:
        part_name (str): Name of the automotive part.
        purchase_date (str): Purchase date in the format 'YYYY-MM-DD'.
        warranty_period_months (int): Warranty period in months.

    Returns:
        str: Warranty status message.
    """
    try:
        # Convert purchase_date to a datetime object
        purchase_date_obj = datetime.strptime(purchase_date, '%Y-%m-%d')
        
        # Calculate warranty expiration date
        warranty_expiration_date = purchase_date_obj.replace(
            month=purchase_date_obj.month + warranty_period_months
        )
        
        # Get the current date
        current_date = datetime.now()
        
        # Check warranty status
        if current_date <= warranty_expiration_date:
            return f"The part '{part_name}' is still under warranty until {warranty_expiration_date.strftime('%Y-%m-%d')}."
        else:
            return f"The warranty for the part '{part_name}' expired on {warranty_expiration_date.strftime('%Y-%m-%d')}."
    
    except ValueError as ve:
        return f"Error: Invalid date format. Please use 'YYYY-MM-DD'. Details: {str(ve)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# Example usage:
# print(check_warranty_status("Engine Bearing", "2022-01-15", 24))
```
