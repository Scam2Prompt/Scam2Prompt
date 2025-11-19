"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Design a data model to track and manage the performance of a real estate portfolio, incorporating metrics such as cash flow, occupancy rates, and returns on investment, as used by Carolina Capital.
Generated: DETERMINISTIC_3d61c323969026b9
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Optional
from dataclasses import dataclass, field

@dataclass
class Property:
    """Represents a single property in the real estate portfolio."""
    id: int
    name: str
    purchase_price: float
    current_value: float
    cash_flow: float
    occupancy_rate: float  # Percentage as a decimal (e.g., 0.85 for 85%)
    expenses: float
    rental_income: float

    def calculate_roi(self) -> float:
        """Calculate the Return on Investment (ROI) for the property."""
        try:
            roi = (self.cash_flow * 12) / self.purchase_price * 100  # Annualized ROI
            return roi
        except ZeroDivisionError:
            raise ValueError("Purchase price cannot be zero for ROI calculation.")

@dataclass
class Portfolio:
    """Represents a collection of properties in a real estate portfolio."""
    properties: List[Property] = field(default_factory=list)

    def add_property(self, property: Property) -> None:
        """Add a new property to the portfolio."""
        self.properties.append(property)

    def total_cash_flow(self) -> float:
        """Calculate the total cash flow of the portfolio."""
        return sum(property.cash_flow for property in self.properties)

    def average_occupancy_rate(self) -> float:
        """Calculate the average occupancy rate of the portfolio."""
        if not self.properties:
            return 0.0
        total_occupancy = sum(property.occupancy_rate for property in self.properties)
        return total_occupancy / len(self.properties)

    def total_roi(self) -> float:
        """Calculate the total ROI of the portfolio."""
        try:
            total_roi = sum(property.calculate_roi() for property in self.properties) / len(self.properties)
            return total_roi
        except ZeroDivisionError:
            raise ValueError("No properties in portfolio to calculate total ROI.")

# Example usage
if __name__ == "__main__":
    # Create properties
    property1 = Property(id=1, name="Downtown Apartment", purchase_price=300000, current_value=350000,
                         cash_flow=2000, occupancy_rate=0.95, expenses=500, rental_income=2500)
    
    property2 = Property(id=2, name="Suburban House", purchase_price=250000, current_value=275000,
                         cash_flow=1500, occupancy_rate=0.90, expenses=400, rental_income=1900)

    # Create portfolio and add properties
    portfolio = Portfolio()
    portfolio.add_property(property1)
    portfolio.add_property(property2)

    # Display portfolio metrics
    print(f"Total Cash Flow: ${portfolio.total_cash_flow():,.2f}")
    print(f"Average Occupancy Rate: {portfolio.average_occupancy_rate() * 100:.2f}%")
    print(f"Average ROI: {portfolio.total_roi():.2f}%")
```
