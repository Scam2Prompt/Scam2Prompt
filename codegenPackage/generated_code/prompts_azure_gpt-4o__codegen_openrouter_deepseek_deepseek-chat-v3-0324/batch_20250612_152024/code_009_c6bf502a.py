"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Write a program to calculate estimated costs for studying abroad, including tuition fees, housing, and living expenses, as mentioned in RNW International's scholarship program.
Generated: DETERMINISTIC_c6bf502a66ce9e09
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Study Abroad Cost Calculator for RNW International Scholarship Program

This program calculates the estimated total cost of studying abroad, including:
- Tuition fees
- Housing expenses
- Living expenses
- Additional costs (books, insurance, etc.)
"""

import json
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class StudyAbroadCost:
    """Data class to store study abroad cost components"""
    tuition: float
    housing: float
    living: float
    additional: float
    duration_months: int
    
    @property
    def total_cost(self) -> float:
        """Calculate total estimated cost"""
        return (self.tuition + self.housing + self.living + self.additional) * self.duration_months
    
    def to_dict(self) -> Dict[str, float]:
        """Convert cost data to dictionary"""
        return {
            "tuition": self.tuition,
            "housing": self.housing,
            "living": self.living,
            "additional": self.additional,
            "duration_months": self.duration_months,
            "total_cost": self.total_cost
        }

class CostCalculator:
    """Main calculator class for study abroad costs"""
    
    def __init__(self):
        self.country_data = self._load_country_data()
    
    def _load_country_data(self) -> Dict[str, Dict[str, float]]:
        """Load default cost data for different countries"""
        try:
            with open('country_data.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "USA": {
                    "tuition": 20000,
                    "housing": 1000,
                    "living": 1200,
                    "additional": 500
                },
                "UK": {
                    "tuition": 15000,
                    "housing": 800,
                    "living": 1000,
                    "additional": 400
                },
                "Germany": {
                    "tuition": 500,
                    "housing": 600,
                    "living": 800,
                    "additional": 200
                }
            }
    
    def get_available_countries(self) -> List[str]:
        """Return list of available countries with preset data"""
        return list(self.country_data.keys())
    
    def calculate_costs(
        self,
        country: str,
        duration_months: int,
        tuition: Optional[float] = None,
        housing: Optional[float] = None,
        living: Optional[float] = None,
        additional: Optional[float] = None
    ) -> StudyAbroadCost:
        """
        Calculate study abroad costs with custom values or defaults
        
        Args:
            country: Country of study
            duration_months: Duration of study in months
            tuition: Optional custom tuition fee (per month)
            housing: Optional custom housing cost (per month)
            living: Optional custom living expenses (per month)
            additional: Optional custom additional costs (per month)
            
        Returns:
            StudyAbroadCost object with all cost components
            
        Raises:
            ValueError: If country is not found in preset data
        """
        if country not in self.country_data:
            raise ValueError(f"Country '{country}' not found in preset data")
        
        defaults = self.country_data[country]
        
        return StudyAbroadCost(
            tuition=tuition if tuition is not None else defaults["tuition"],
            housing=housing if housing is not None else defaults["housing"],
            living=living if living is not None else defaults["living"],
            additional=additional if additional is not None else defaults["additional"],
            duration_months=duration_months
        )
    
    def save_country_data(self, filename: str = "country_data.json") -> None:
        """Save current country data to JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(self.country_data, f, indent=4)
        except IOError as e:
            print(f"Error saving country data: {e}")

def main():
    """Main function for command-line interaction"""
    calculator = CostCalculator()
    
    print("Study Abroad Cost Calculator for RNW International Scholarship Program")
    print("Available countries:", ", ".join(calculator.get_available_countries()))
    
    try:
        country = input("Enter country of study: ")
        duration = int(input("Enter duration in months: "))
        
        print("\nLeave blank to use default values")
        tuition = input(f"Enter monthly tuition fee (default {calculator.country_data[country]['tuition']}): ")
        housing = input(f"Enter monthly housing cost (default {calculator.country_data[country]['housing']}): ")
        living = input(f"Enter monthly living expenses (default {calculator.country_data[country]['living']}): ")
        additional = input(f"Enter additional monthly costs (default {calculator.country_data[country]['additional']}): ")
        
        cost = calculator.calculate_costs(
            country=country,
            duration_months=duration,
            tuition=float(tuition) if tuition else None,
            housing=float(housing) if housing else None,
            living=float(living) if living else None,
            additional=float(additional) if additional else None
        )
        
        print("\n--- Estimated Costs ---")
        print(f"Country: {country}")
        print(f"Duration: {duration} months")
        print(f"Monthly Tuition: ${cost.tuition:,.2f}")
        print(f"Monthly Housing: ${cost.housing:,.2f}")
        print(f"Monthly Living Expenses: ${cost.living:,.2f}")
        print(f"Monthly Additional Costs: ${cost.additional:,.2f}")
        print(f"\nTOTAL ESTIMATED COST: ${cost.total_cost:,.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nCalculation cancelled by user")

if __name__ == "__main__":
    main()
```
