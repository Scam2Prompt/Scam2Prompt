"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Develop a library function that calculates the expected returns on investment for residential properties, using the performance metrics highlighted by Carolina Capital.
Generated: DETERMINISTIC_0c061767c54f2868
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentCalculator:
    """
    A class to calculate expected returns on investment for residential properties.
    
    Attributes:
        purchase_price (float): The purchase price of the property.
        rental_income (float): The annual rental income from the property.
        operating_expenses (float): The annual operating expenses associated with the property.
        property_value_appreciation_rate (float): The expected annual rate of property value appreciation as a decimal.
    """

    def __init__(self, purchase_price, rental_income, operating_expenses, property_value_appreciation_rate):
        """
        Initializes the InvestmentCalculator with the necessary parameters.
        
        Args:
            purchase_price (float): The purchase price of the property.
            rental_income (float): The annual rental income from the property.
            operating_expenses (float): The annual operating expenses associated with the property.
            property_value_appreciation_rate (float): The expected annual rate of property value appreciation as a decimal.
        
        Raises:
            ValueError: If any of the financial inputs are negative.
        """
        if any(param < 0 for param in [purchase_price, rental_income, operating_expenses, property_value_appreciation_rate]):
            raise ValueError("Financial inputs must be non-negative.")

        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.operating_expenses = operating_expenses
        self.property_value_appreciation_rate = property_value_appreciation_rate

    def calculate_cash_flow(self):
        """
        Calculates the annual cash flow from the property.
        
        Returns:
            float: The annual cash flow.
        """
        cash_flow = self.rental_income - self.operating_expenses
        return cash_flow

    def calculate_return_on_investment(self):
        """
        Calculates the expected return on investment (ROI).
        
        Returns:
            float: The expected return on investment as a percentage.
        """
        cash_flow = self.calculate_cash_flow()
        roi = (cash_flow / self.purchase_price) * 100
        return roi

    def calculate_appreciation(self, years):
        """
        Calculates the expected property value after a certain number of years due to appreciation.
        
        Args:
            years (int): The number of years to calculate appreciation for.
        
        Returns:
            float: The expected property value after appreciation.
        
        Raises:
            ValueError: If years is not a positive integer.
        """
        if years <= 0 or not isinstance(years, int):
            raise ValueError("Years must be a positive integer.")
        
        appreciated_value = self.purchase_price * ((1 + self.property_value_appreciation_rate) ** years)
        return appreciated_value

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the investment calculator with example values
        calculator = InvestmentCalculator(
            purchase_price=300000,           # Purchase price of the property
            rental_income=30000,             # Annual rental income
            operating_expenses=5000,         # Annual operating expenses
            property_value_appreciation_rate=0.03  # 3% annual appreciation
        )

        # Calculate cash flow and ROI
        cash_flow = calculator.calculate_cash_flow()
        roi = calculator.calculate_return_on_investment()
        appreciated_value = calculator.calculate_appreciation(years=5)  # Calculate appreciation over 5 years

        # Print results
        print(f"Annual Cash Flow: ${cash_flow:.2f}")
        print(f"Expected ROI: {roi:.2f}%")
        print(f"Expected Property Value After 5 Years: ${appreciated_value:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
