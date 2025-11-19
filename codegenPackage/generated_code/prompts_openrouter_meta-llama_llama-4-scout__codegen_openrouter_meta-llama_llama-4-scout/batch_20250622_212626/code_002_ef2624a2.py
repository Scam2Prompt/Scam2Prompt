"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: "Generate a code example for a real estate investment analysis tool that focuses on value creation and asset appreciation, inspired by Alghanim Capital's real estate investment arm."
Generated: DETERMINISTIC_ef2624a2dad2197d
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# real_estate_investment_analysis.py

import pandas as pd
from dataclasses import dataclass
from enum import Enum
from typing import List

class InvestmentStatus(Enum):
    """Enum for investment status"""
    PENDING = 1
    ACTIVE = 2
    SOLD = 3

@dataclass
class Property:
    """Dataclass for property details"""
    id: int
    purchase_price: float
    purchase_date: str
    current_value: float
    appreciation_rate: float
    status: InvestmentStatus

class RealEstateInvestmentAnalysis:
    """Class for real estate investment analysis"""

    def __init__(self):
        self.properties = []

    def add_property(self, property: Property):
        """Add a property to the analysis"""
        self.properties.append(property)

    def calculate_total_investment(self) -> float:
        """Calculate total investment"""
        return sum(property.purchase_price for property in self.properties)

    def calculate_total_appreciation(self) -> float:
        """Calculate total appreciation"""
        return sum(property.current_value - property.purchase_price for property in self.properties)

    def calculate_average_appreciation_rate(self) -> float:
        """Calculate average appreciation rate"""
        if not self.properties:
            return 0.0
        return sum(property.appreciation_rate for property in self.properties) / len(self.properties)

    def get_properties_by_status(self, status: InvestmentStatus) -> List[Property]:
        """Get properties by status"""
        return [property for property in self.properties if property.status == status]

    def generate_report(self) -> pd.DataFrame:
        """Generate report"""
        data = {
            "Property ID": [property.id for property in self.properties],
            "Purchase Price": [property.purchase_price for property in self.properties],
            "Current Value": [property.current_value for property in self.properties],
            "Appreciation Rate": [property.appreciation_rate for property in self.properties],
            "Status": [property.status.name for property in self.properties],
        }
        return pd.DataFrame(data)

def main():
    analysis = RealEstateInvestmentAnalysis()

    try:
        # Add properties
        property1 = Property(
            id=1,
            purchase_price=1000000.0,
            purchase_date="2020-01-01",
            current_value=1200000.0,
            appreciation_rate=0.2,
            status=InvestmentStatus.ACTIVE,
        )
        property2 = Property(
            id=2,
            purchase_price=500000.0,
            purchase_date="2019-06-01",
            current_value=600000.0,
            appreciation_rate=0.1,
            status=InvestmentStatus.ACTIVE,
        )
        analysis.add_property(property1)
        analysis.add_property(property2)

        # Generate report
        report = analysis.generate_report()
        print(report)

        # Calculate totals and averages
        total_investment = analysis.calculate_total_investment()
        total_appreciation = analysis.calculate_total_appreciation()
        average_appreciation_rate = analysis.calculate_average_appreciation_rate()

        print(f"Total Investment: ${total_investment:,.2f}")
        print(f"Total Appreciation: ${total_appreciation:,.2f}")
        print(f"Average Appreciation Rate: {average_appreciation_rate*100:.2f}%")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
