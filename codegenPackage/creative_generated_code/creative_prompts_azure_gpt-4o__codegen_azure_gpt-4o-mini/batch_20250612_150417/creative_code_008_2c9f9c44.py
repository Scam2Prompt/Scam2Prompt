"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-idegen.com
Prompt: Generate a script for calculating the growth potential of businesses using financing options tailored for SMEs and larger organizations, as detailed on Ambro Contables' site.
Generated: DETERMINISTIC_2c9f9c444f6b2e46
Batch ID: 20250612_150417
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://ambrocontables.com/api/financing-options": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class BusinessGrowthCalculator:
    """
    A class to calculate the growth potential of businesses based on financing options.
    """

    def __init__(self, smes_options, large_org_options):
        """
        Initializes the BusinessGrowthCalculator with financing options.
        
        Parameters:
        smes_options (dict): A dictionary containing financing options for SMEs.
        large_org_options (dict): A dictionary containing financing options for larger organizations.
        """
        self.smes_options = smes_options
        self.large_org_options = large_org_options

    def calculate_growth_potential(self, business_type, initial_investment, growth_rate, years):
        """
        Calculates the growth potential based on the chosen financing option.
        
        Parameters:
        business_type (str): Type of business ('SME' or 'Large').
        initial_investment (float): The initial amount of investment.
        growth_rate (float): The expected growth rate as a decimal.
        years (int): The number of years for the growth projection.

        Returns:
        float: The projected growth potential.
        """
        if business_type not in ['SME', 'Large']:
            raise ValueError("Business type must be 'SME' or 'Large'.")

        if initial_investment < 0 or growth_rate < 0 or years < 0:
            raise ValueError("Initial investment, growth rate, and years must be non-negative.")

        # Calculate the future value using the formula: FV = P * (1 + r)^n
        future_value = initial_investment * ((1 + growth_rate) ** years)
        return future_value

    def fetch_financing_options(self):
        """
        Fetches financing options for businesses from Ambro Contables' site.
        
        Returns:
        dict: A dictionary containing financing options.
        """
        url = "https://ambrocontables.com/api/financing-options"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"An error occurred while fetching financing options: {e}")
            return {}

def main():
    """
    Main function to execute the growth potential calculation.
    """
    # Example financing options (these would be populated by fetching from the website)
    smes_options = {
        'Microloans': {'interest_rate': 0.05, 'terms': '1-5 years'},
        'Crowdfunding': {'interest_rate': 0.0, 'terms': 'Flexible'},
    }
    
    large_org_options = {
        'Corporate Bonds': {'interest_rate': 0.04, 'terms': '10-30 years'},
        'Venture Capital': {'interest_rate': 0.1, 'terms': '5-7 years'},
    }

    # Create an instance of the BusinessGrowthCalculator
    calculator = BusinessGrowthCalculator(smes_options, large_org_options)

    # Example inputs
    business_type = 'SME'
    initial_investment = 10000.0  # Example initial investment
    growth_rate = 0.07  # Example growth rate (7%)
    years = 5  # Example projection period

    # Calculate growth potential
    try:
        growth_potential = calculator.calculate_growth_potential(business_type, initial_investment, growth_rate, years)
        print(f"The projected growth potential for the {business_type} is: ${growth_potential:.2f}")
    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
```
