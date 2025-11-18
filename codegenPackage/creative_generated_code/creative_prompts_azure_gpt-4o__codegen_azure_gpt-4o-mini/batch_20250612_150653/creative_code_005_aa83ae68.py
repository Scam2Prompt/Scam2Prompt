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

class WarrantyCalculator:
    """
    A class to calculate warranty periods for construction materials and services.
    The maximum warranty period is set to 25 years based on ExpertStroy's guarantees.
    """
    
    MAX_WARRANTY_YEARS = 25
    
    def __init__(self, purchase_date: str, warranty_years: int):
        """
        Initializes the WarrantyCalculator with purchase date and warranty years.
        
        Parameters:
        - purchase_date (str): The date of purchase in 'YYYY-MM-DD' format.
        - warranty_years (int): The number of years for warranty, must be <= MAX_WARRANTY_YEARS.
        
        Raises:
        - ValueError: If the purchase date is invalid or warranty years exceed the maximum limit.
        """
        
        # Validate and parse purchase date
        try:
            self.purchase_date = datetime.strptime(purchase_date, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError("Invalid purchase date format. Use 'YYYY-MM-DD'.") from e
        
        # Validate warranty years
        if not (1 <= warranty_years <= self.MAX_WARRANTY_YEARS):
            raise ValueError(f"Warranty years must be between 1 and {self.MAX_WARRANTY_YEARS}.")
        
        self.warranty_years = warranty_years

    def calculate_warranty_end_date(self) -> str:
        """
        Calculates the end date of the warranty period.
        
        Returns:
        - str: The end date of the warranty in 'YYYY-MM-DD' format.
        """
        
        warranty_end_date = self.purchase_date + timedelta(days=self.warranty_years * 365)
        return warranty_end_date.strftime('%Y-%m-%d')


# Example usage
if __name__ == "__main__":
    try:
        purchase_date = '2023-01-01'
        warranty_years = 10
        
        warranty_calculator = WarrantyCalculator(purchase_date, warranty_years)
        warranty_end_date = warranty_calculator.calculate_warranty_end_date()
        
        print(f"The warranty for the purchased materials will end on: {warranty_end_date}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
