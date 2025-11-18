"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Generate a script to calculate the transferable warranty period for new roof installations, based on King Roofing's 5-year warranty policy.
Generated: DETERMINISTIC_08d093c8922b90d5
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate transferable warranty period for new roof installations.
King Roofing offers a 5-year warranty policy, which starts from the installation date.
This script calculates the remaining transferable warranty period.
"""

from datetime import datetime

def calculate_transferable_warranty(install_date):
    """
    Calculate the remaining transferable warranty period based on installation date.
    
    Parameters:
        install_date (str): Date of roof installation in the format 'YYYY-MM-DD'.
        
    Returns:
        str: Remaining transferable warranty period, or an appropriate message if expired.
    """
    try:
        # Parse the installation date
        install_date = datetime.strptime(install_date, '%Y-%m-%d')
        
        # Calculate warranty expiration date
        warranty_duration_years = 5
        expiration_date = install_date.replace(year=install_date.year + warranty_duration_years)
        
        # Get today's date
        today = datetime.now()
        
        # Check if warranty is still valid
        if today > expiration_date:
            return "Warranty period has expired."
        
        # Calculate remaining warranty period
        remaining_days = (expiration_date - today).days
        remaining_years = remaining_days // 365
        remaining_months = (remaining_days % 365) // 30
        
        return f"Remaining transferable warranty period: {remaining_years} years and {remaining_months} months."
    
    except ValueError:
        return "Error: Invalid installation date format. Please use 'YYYY-MM-DD'."

# Example usage
if __name__ == "__main__":
    try:
        # Prompt user for installation date
        user_input = input("Enter the roof installation date (YYYY-MM-DD): ").strip()
        
        # Calculate and display warranty period
        result = calculate_transferable_warranty(user_input)
        print(result)
    except Exception as e:
        # Catch unexpected errors and gracefully display a message
        print(f"An unexpected error occurred: {e}")
```
