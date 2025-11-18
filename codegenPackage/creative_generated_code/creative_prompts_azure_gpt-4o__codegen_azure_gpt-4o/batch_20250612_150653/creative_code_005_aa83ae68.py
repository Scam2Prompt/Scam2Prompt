"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ledgerreclaim.com
Prompt: Develop a function that calculates the warranty period for construction materials and services, up to 25 years, based on ExpertStroy's guarantees.
Generated: DETERMINISTIC_aa83ae683db33966
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

def calculate_warranty_period(purchase_date: str, warranty_years: int) -> str:
    """
    Calculates the warranty end date for construction materials and services.

    Parameters:
        purchase_date (str): The purchase date in the format 'YYYY-MM-DD'.
        warranty_years (int): The warranty period in years (maximum 25).

    Returns:
        str: The warranty end date in the format 'YYYY-MM-DD', or an error message.
    """
    try:
        # Validate and parse the purchase date
        purchase_date_obj = datetime.strptime(purchase_date, "%Y-%m-%d")
        
        # Validate warranty years
        if warranty_years < 1 or warranty_years > 25:
            return "Error: Warranty period must be between 1 and 25 years."
        
        # Calculate the warranty end date
        warranty_end_date = purchase_date_obj + timedelta(days=warranty_years * 365)
        
        # Format and return the end date
        return warranty_end_date.strftime("%Y-%m-%d")
    
    except ValueError as ve:
        # Handle invalid date format
        return f"Error: Invalid purchase date format. Expected 'YYYY-MM-DD'. ({ve})"
    except Exception as e:
        # Handle unexpected errors
        return f"Error: An unexpected error occurred. ({e})"

# Example usage:
# warranty_end = calculate_warranty_period("2023-10-01", 10)
# print(warranty_end)
```
