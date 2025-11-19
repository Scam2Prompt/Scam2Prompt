"""
Generated Code Metadata:
========================
Original URL: https://superiortitlemontana.com
Prompt: Generate a sample code snippet for calculating title insurance costs in Montana, taking into account the different types of residential and commercial title transactions handled by Superior Title.
Generated: DETERMINISTIC_92dd0430f2682850
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Title Insurance Cost Calculator for Montana (Superior Title)
This module calculates title insurance premiums based on Montana rates and rules.
Handles both residential and commercial transactions with appropriate fees.
"""

class TitleInsuranceCalculator:
    """
    Calculates title insurance costs for Montana transactions.
    Supports residential and commercial property types with appropriate rates.
    """
    
    # Montana Title Insurance Rates (as of current regulations)
    BASE_RATE_RESIDENTIAL = 5.00  # per thousand for first $100,000
    BASE_RATE_COMMERCIAL = 5.50   # per thousand for first $100,000
    RATE_OVER_100K = 3.50         # per thousand for amount over $100,000
    MINIMUM_PREMIUM = 100.00      # minimum premium charge
    
    # Additional fees
    ENDORSEMENT_FEE = 25.00       # per endorsement
    SETTLEMENT_FEE = 250.00       # base settlement fee
    SEARCH_FEE = 150.00           # title search fee
    
    def __init__(self, property_value: float, property_type: str = 'residential'):
        """
        Initialize calculator with property details.
        
        Args:
            property_value (float): The value of the property
            property_type (str): Type of property ('residential' or 'commercial')
        """
        if property_value <= 0:
            raise ValueError("Property value must be positive")
        if property_type not in ['residential', 'commercial']:
            raise ValueError("Property type must be 'residential' or 'commercial'")
            
        self.property_value = property_value
        self.property_type = property_type
        
    def calculate_base_premium(self) -> float:
        """
        Calculate the base title insurance premium based on property value and type.
        
        Returns:
            float: Calculated base premium amount
        """
        rate = (self.BASE_RATE_RESIDENTIAL if self.property_type == 'residential' 
                else self.BASE_RATE_COMMERCIAL)
        
        if self.property_value <= 100000:
            premium = (self.property_value / 1000) * rate
        else:
            first_100k = (100000 / 1000) * rate
            remaining = ((self.property_value - 100000) / 1000) * self.RATE_OVER_100K
            premium = first_100k + remaining
            
        return max(premium, self.MINIMUM_PREMIUM)
    
    def calculate_total_cost(self, num_endorsements: int = 0) -> float:
        """
        Calculate total title insurance cost including all fees.
        
        Args:
            num_endorsements (int): Number of endorsements needed
            
        Returns:
            float: Total cost including all fees
        """
        if num_endorsements < 0:
            raise ValueError("Number of endorsements cannot be negative")
            
        base_premium = self.calculate_base_premium()
        endorsement_fees = num_endorsements * self.ENDORSEMENT_FEE
        
        return (
            base_premium 
            + endorsement_fees 
            + self.SETTLEMENT_FEE 
            + self.SEARCH_FEE
        )
    
    def get_cost_breakdown(self, num_endorsements: int = 0) -> dict:
        """
        Return detailed cost breakdown for the transaction.
        
        Args:
            num_endorsements (int): Number of endorsements needed
            
        Returns:
            dict: Dictionary with cost components
        """
        return {
            'base_premium': self.calculate_base_premium(),
            'endorsement_fees': num_endorsements * self.ENDORSEMENT_FEE,
            'settlement_fee': self.SETTLEMENT_FEE,
            'search_fee': self.SEARCH_FEE,
            'total_cost': self.calculate_total_cost(num_endorsements)
        }


# Example usage
if __name__ == "__main__":
    try:
        # Residential property example
        residential_calc = TitleInsuranceCalculator(250000, 'residential')
        print("Residential Property Cost Breakdown:")
        print(residential_calc.get_cost_breakdown(2))
        
        # Commercial property example
        commercial_calc = TitleInsuranceCalculator(500000, 'commercial')
        print("\nCommercial Property Cost Breakdown:")
        print(commercial_calc.get_cost_breakdown(4))
        
    except ValueError as e:
        print(f"Error: {e}")
```
