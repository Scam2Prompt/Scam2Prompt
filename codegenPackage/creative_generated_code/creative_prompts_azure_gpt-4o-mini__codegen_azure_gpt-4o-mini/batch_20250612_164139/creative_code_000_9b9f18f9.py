"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beboldproperties.com
Prompt: Generate a code snippet for a property management system that integrates with financial planners and mortgage brokers, focusing on maximizing investment returns.
Generated: DETERMINISTIC_9b9f18f900b26675
Batch ID: 20250612_164139
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.financialplanners.com/v1/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.mortgagebrokers.com/v1/": {
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
import json
import requests

class Property:
    """Class representing a property in the management system."""
    
    def __init__(self, address, purchase_price, rental_income):
        self.address = address
        self.purchase_price = purchase_price
        self.rental_income = rental_income

    def calculate_roi(self):
        """Calculate the return on investment (ROI) for the property."""
        try:
            roi = (self.rental_income * 12) / self.purchase_price * 100  # Annualize rental income
            return round(roi, 2)
        except ZeroDivisionError:
            print("Error: Purchase price cannot be zero.")
            return None

class FinancialPlanner:
    """Class representing a financial planner."""
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.financialplanners.com/v1/"

    def fetch_market_data(self):
        """Fetch current market data from the financial planner API."""
        try:
            response = requests.get(f"{self.api_url}market-data", headers={"Authorization": self.api_key})
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching market data: {e}")
            return None

class MortgageBroker:
    """Class representing a mortgage broker."""
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.mortgagebrokers.com/v1/"

    def calculate_mortgage(self, property_value, down_payment_percentage):
        """Calculate estimated mortgage based on property value and down payment."""
        try:
            down_payment = property_value * (down_payment_percentage / 100)
            loan_amount = property_value - down_payment
            return {
                "down_payment": round(down_payment, 2),
                "loan_amount": round(loan_amount, 2),
                "monthly_payment": self.estimate_monthly_payment(loan_amount)
            }
        except Exception as e:
            print(f"Error calculating mortgage: {e}")
            return None

    def estimate_monthly_payment(self, loan_amount):
        """Estimate monthly payment based on standard interest rates (simplified)."""
        annual_interest_rate = 0.05  # Example interest rate
        loan_term_years = 30
        monthly_interest_rate = annual_interest_rate / 12
        number_of_payments = loan_term_years * 12
        
        if loan_amount <= 0 or number_of_payments <= 0:
            raise ValueError("Loan amount and number of payments must be positive.")

        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        return round(monthly_payment, 2)

# Example usage:
if __name__ == "__main__":
    # Create property instance
    property1 = Property(address="123 Main St", purchase_price=300000, rental_income=2000)

    # Calculate ROI
    roi = property1.calculate_roi()
    if roi is not None:
        print(f"ROI for {property1.address}: {roi}%")

    # Initialize financial planner and fetch market data
    planner = FinancialPlanner(api_key="your_financial_planner_api_key")
    market_data = planner.fetch_market_data()
    if market_data:
        print("Market data fetched successfully.")

    # Initialize mortgage broker and calculate mortgage
    broker = MortgageBroker(api_key="your_mortgage_broker_api_key")
    mortgage_details = broker.calculate_mortgage(property_value=property1.purchase_price, down_payment_percentage=20)
    if mortgage_details:
        print(f"Mortgage details: {json.dumps(mortgage_details, indent=2)}")
```
