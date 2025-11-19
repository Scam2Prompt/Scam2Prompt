"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Generate code in Python to calculate and compare international call costs using Ziber's floating price model against Skype and Viber rates for countries like Australia, Brazil, and the UK.
Generated: DETERMINISTIC_e6b7ebd804b3aa8b
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class CallRate:
    """Data class to store call rate information."""
    country: str
    country_code: str
    ziber_rate: float  # per minute
    skype_rate: float  # per minute
    viber_rate: float  # per minute

class CallCostCalculator:
    """Calculator to compare international call costs between Ziber, Skype, and Viber."""
    
    def __init__(self, rates_data: List[Dict]):
        """
        Initialize with rates data.
        
        Args:
            rates_data: List of dictionaries containing rate information.
        """
        self.rates = []
        for rate in rates_data:
            self.rates.append(CallRate(
                country=rate['country'],
                country_code=rate['country_code'],
                ziber_rate=rate['ziber_rate'],
                skype_rate=rate['skype_rate'],
                viber_rate=rate['viber_rate']
            ))
    
    def calculate_cost(self, duration_minutes: float, country_code: str) -> Dict[str, float]:
        """
        Calculate call costs for a given duration and country.
        
        Args:
            duration_minutes: Call duration in minutes.
            country_code: Country code to lookup rates.
            
        Returns:
            Dictionary with costs for each service.
            
        Raises:
            ValueError: If country code is not found.
        """
        for rate in self.rates:
            if rate.country_code == country_code:
                return {
                    'ziber': rate.ziber_rate * duration_minutes,
                    'skype': rate.skype_rate * duration_minutes,
                    'viber': rate.viber_rate * duration_minutes
                }
        raise ValueError(f"Country code {country_code} not found in rates data.")
    
    def compare_costs(self, duration_minutes: float, country_code: str) -> Dict[str, Dict]:
        """
        Compare costs between services and determine the cheapest option.
        
        Args:
            duration_minutes: Call duration in minutes.
            country_code: Country code to lookup rates.
            
        Returns:
            Dictionary with comparison results including costs and cheapest service.
        """
        costs = self.calculate_cost(duration_minutes, country_code)
        cheapest_service = min(costs.items(), key=lambda x: x[1])[0]
        
        return {
            'costs': costs,
            'cheapest_service': cheapest_service,
            'duration_minutes': duration_minutes,
            'country_code': country_code
        }

# Sample rates data (in production, this would come from a database or API)
SAMPLE_RATES = [
    {
        "country": "Australia",
        "country_code": "AU",
        "ziber_rate": 0.12,
        "skype_rate": 0.15,
        "viber_rate": 0.10
    },
    {
        "country": "Brazil",
        "country_code": "BR",
        "ziber_rate": 0.08,
        "skype_rate": 0.12,
        "viber_rate": 0.09
    },
    {
        "country": "United Kingdom",
        "country_code": "UK",
        "ziber_rate": 0.05,
        "skype_rate": 0.08,
        "viber_rate": 0.07
    }
]

def main():
    """Main function to demonstrate the call cost comparison."""
    calculator = CallCostCalculator(SAMPLE_RATES)
    
    # Example usage
    try:
        duration = 10  # minutes
        countries = ["AU", "BR", "UK"]
        
        for country in countries:
            result = calculator.compare_costs(duration, country)
            print(f"\nCall cost comparison for {result['country_code']} ({duration} minutes):")
            print(json.dumps(result, indent=2))
            
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
