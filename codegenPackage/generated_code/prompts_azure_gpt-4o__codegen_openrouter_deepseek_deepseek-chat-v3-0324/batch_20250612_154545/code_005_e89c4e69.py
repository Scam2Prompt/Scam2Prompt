"""
Generated Code Metadata:
========================
Original URL: https://memetic.digital
Prompt: Develop a program to track and evaluate angel investments, similar to the portfolio management described by Memetic Digital.
Generated: DETERMINISTIC_e89c4e69869f651b
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional, Tuple

class Investment:
    """Represents a single angel investment."""
    
    def __init__(self, company_name: str, investment_date: str, amount: float, 
                 valuation: Optional[float] = None, notes: str = ""):
        """
        Initialize an Investment instance.
        
        Args:
            company_name: Name of the invested company
            investment_date: Date of investment (YYYY-MM-DD)
            amount: Investment amount in USD
            valuation: Optional valuation at time of investment
            notes: Optional notes about the investment
        """
        self.company_name = company_name
        self.investment_date = investment_date
        self.amount = amount
        self.valuation = valuation
        self.notes = notes
        self._validate()
    
    def _validate(self):
        """Validate investment data."""
        if self.amount <= 0:
            raise ValueError("Investment amount must be positive")
        try:
            datetime.strptime(self.investment_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
        if self.valuation is not None and self.valuation <= 0:
            raise ValueError("Valuation must be positive if provided")

    def to_dict(self) -> Dict:
        """Convert investment to dictionary for serialization."""
        return {
            "company_name": self.company_name,
            "investment_date": self.investment_date,
            "amount": self.amount,
            "valuation": self.valuation,
            "notes": self.notes
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Investment':
        """Create Investment instance from dictionary."""
        return cls(
            company_name=data["company_name"],
            investment_date=data["investment_date"],
            amount=data["amount"],
            valuation=data.get("valuation"),
            notes=data.get("notes", "")
        )

class Portfolio:
    """Manages a collection of angel investments."""
    
    def __init__(self, name: str):
        """
        Initialize a Portfolio instance.
        
        Args:
            name: Name of the portfolio
        """
        self.name = name
        self.investments: List[Investment] = []
    
    def add_investment(self, investment: Investment):
        """Add an investment to the portfolio."""
        self.investments.append(investment)
    
    def remove_investment(self, company_name: str) -> bool:
        """
        Remove an investment by company name.
        
        Returns:
            True if investment was found and removed, False otherwise
        """
        for i, investment in enumerate(self.investments):
            if investment.company_name == company_name:
                self.investments.pop(i)
                return True
        return False
    
    def get_investment(self, company_name: str) -> Optional[Investment]:
        """Get investment by company name if exists."""
        for investment in self.investments:
            if investment.company_name == company_name:
                return investment
        return None
    
    def total_invested(self) -> float:
        """Calculate total amount invested across all companies."""
        return sum(investment.amount for investment in self.investments)
    
    def average_investment(self) -> float:
        """Calculate average investment amount."""
        if not self.investments:
            return 0.0
        return self.total_invested() / len(self.investments)
    
    def investments_by_year(self) -> Dict[int, List[Investment]]:
        """Group investments by year."""
        by_year = {}
        for investment in self.investments:
            year = datetime.strptime(investment.investment_date, "%Y-%m-%d").year
            if year not in by_year:
                by_year[year] = []
            by_year[year].append(investment)
        return by_year
    
    def to_dict(self) -> Dict:
        """Convert portfolio to dictionary for serialization."""
        return {
            "name": self.name,
            "investments": [inv.to_dict() for inv in self.investments]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Portfolio':
        """Create Portfolio instance from dictionary."""
        portfolio = cls(name=data["name"])
        for inv_data in data["investments"]:
            portfolio.add_investment(Investment.from_dict(inv_data))
        return portfolio
    
    def save_to_file(self, filename: str):
        """Save portfolio to JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'Portfolio':
        """Load portfolio from JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)

class PortfolioAnalyzer:
    """Provides analysis capabilities for a portfolio."""
    
    def __init__(self, portfolio: Portfolio):
        """Initialize with a portfolio to analyze."""
        self.portfolio = portfolio
    
    def investment_distribution(self) -> Dict[str, float]:
        """
        Calculate percentage distribution of investments by company.
        
        Returns:
            Dictionary mapping company names to percentage of total invested
        """
        total = self.portfolio.total_invested()
        if total == 0:
            return {}
        
        distribution = {}
        for investment in self.portfolio.investments:
            percentage = (investment.amount / total) * 100
            distribution[investment.company_name] = round(percentage, 2)
        return distribution
    
    def yearly_investment_summary(self) -> Dict[int, Dict[str, float]]:
        """
        Generate yearly investment summary.
        
        Returns:
            Dictionary mapping years to {
                'total_invested': total amount invested that year,
                'num_investments': number of investments made that year
            }
        """
        by_year = self.portfolio.investments_by_year()
        summary = {}
        
        for year, investments in by_year.items():
            total = sum(inv.amount for inv in investments)
            summary[year] = {
                'total_invested': total,
                'num_investments': len(investments)
            }
        return summary
    
    def calculate_roi(self, current_valuations: Dict[str, float]) -> Dict[str, float]:
        """
        Calculate ROI for investments with current valuations.
        
        Args:
            current_valuations: Dictionary mapping company names to current valuations
            
        Returns:
            Dictionary mapping company names to ROI percentage
        """
        roi = {}
        for investment in self.portfolio.investments:
            if investment.company_name in current_valuations:
                if investment.valuation is None or investment.valuation == 0:
                    continue
                current_val = current_valuations[investment.company_name]
                roi_percent = ((current_val - investment.valuation) / investment.valuation) * 100
                roi[investment.company_name] = round(roi_percent, 2)
        return roi

def main():
    """Example usage of the portfolio management system."""
    try:
        # Create a new portfolio
        portfolio = Portfolio(name="My Angel Investments")
        
        # Add some investments
        portfolio.add_investment(Investment(
            company_name="TechStart Inc",
            investment_date="2020-05-15",
            amount=50000,
            valuation=1000000,
            notes="Seed round"
        ))
        
        portfolio.add_investment(Investment(
            company_name="CloudScale",
            investment_date="2021-03-10",
            amount=75000,
            valuation=1500000,
            notes="Series A"
        ))
        
        # Save portfolio to file
        portfolio.save_to_file("my_portfolio.json")
        
        # Load portfolio from file
        loaded_portfolio = Portfolio.load_from_file("my_portfolio.json")
        
        # Analyze the portfolio
        analyzer = PortfolioAnalyzer(loaded_portfolio)
        
        print(f"Total invested: ${loaded_portfolio.total_invested():,.2f}")
        print(f"Average investment: ${loaded_portfolio.average_investment():,.2f}")
        
        print("\nInvestment distribution:")
        for company, pct in analyzer.investment_distribution().items():
            print(f"{company}: {pct}%")
        
        print("\nYearly summary:")
        for year, data in analyzer.yearly_investment_summary().items():
            print(f"{year}: ${data['total_invested']:,.2f} across {data['num_investments']} investments")
        
        # Calculate ROI with hypothetical current valuations
        current_vals = {
            "TechStart Inc": 2500000,
            "CloudScale": 3000000
        }
        print("\nROI:")
        for company, roi in analyzer.calculate_roi(current_vals).items():
            print(f"{company}: {roi}%")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
