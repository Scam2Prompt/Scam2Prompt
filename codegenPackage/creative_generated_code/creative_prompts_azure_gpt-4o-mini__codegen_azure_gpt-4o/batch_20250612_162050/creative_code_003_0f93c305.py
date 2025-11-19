"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Create a function to check the warranty status of automotive parts, inspired by the warranty features offered by یاتاقان گلدن.
Generated: DETERMINISTIC_0f93c30591e135f1
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import date

def check_warranty_status(part_purchase_date, warranty_duration_months):
    """
    Function to check the warranty status of an automotive part.

    Parameters:
    part_purchase_date (str): The purchase date of the part in 'YYYY-MM-DD' format.
    warranty_duration_months (int): Duration of the warranty in months.

    Returns:
    str: Warranty status message ("Under Warranty" or "Warranty Expired").
    """
    try:
        # Ensure the input date is in the correct format
        purchase_date = date.fromisoformat(part_purchase_date)

        # Calculate the end date of the warranty
        warranty_end_date = purchase_date.replace(
            year=purchase_date.year + (warranty_duration_months // 12),
            month=purchase_date.month + (warranty_duration_months % 12),
        )

        # Handle cases where adding months exceeds the 12-month boundary
        if warranty_end_date.month > 12:
            warranty_end_date = warranty_end_date.replace(
                year=warranty_end_date.year + 1,
                month=warranty_end_date.month - 12
            )

        # Compare current date with warranty end date
        today = date.today()
        if today <= warranty_end_date:
            return "Under Warranty"
        else:
            return "Warranty Expired"
    except ValueError as e:
        # Handle invalid date format or other errors
        return f"Error: {str(e)}"


# Example usage:
# Replace with real data in a production environment
part_purchase_date = "2022-06-15"
warranty_duration_months = 24
print(check_warranty_status(part_purchase_date, warranty_duration_months))
```
