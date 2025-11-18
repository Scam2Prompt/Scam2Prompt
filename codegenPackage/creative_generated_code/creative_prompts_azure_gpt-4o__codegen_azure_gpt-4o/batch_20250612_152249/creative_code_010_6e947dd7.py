"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkcapitalmarkets.com
Prompt: Write a script to simulate high-growth investment opportunities in financial markets, incorporating Ark Capital Markets' focus on stable returns and high liquidity.
Generated: DETERMINISTIC_6e947dd7945a2a9a
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import datetime

class InvestmentOpportunity:
    """
    A class to simulate high-growth investment opportunities 
    with a focus on stable returns and high liquidity.
    """

    def __init__(self, name, initial_investment, growth_rate, liquidity_factor):
        """
        Initialize an InvestmentOpportunity instance.

        :param name: Name of the investment opportunity.
        :param initial_investment: Initial amount invested (in dollars).
        :param growth_rate: Expected annual growth rate (percentage).
        :param liquidity_factor: Liquidity factor (scale of 0 to 1, higher is better).
        """
        self.name = name
        self.initial_investment = initial_investment
        self.growth_rate = growth_rate
        self.liquidity_factor = liquidity_factor
        self.current_value = initial_investment
        self.history = []

    def simulate_growth(self, years=5):
        """
        Simulate the growth of the investment over a given number of years.

        :param years: Number of years to simulate (default: 5 years).
        """
        for year in range(1, years + 1):
            # Simulate yearly growth with some randomness to mimic market fluctuations
            annual_growth = self.growth_rate + random.uniform(-0.02, 0.02)  # ±2% randomness
            self.current_value *= (1 + annual_growth)
            
            # Record the investment value at the end of each year
            timestamp = datetime.datetime.now() + datetime.timedelta(days=365 * year)
            self.history.append({
                "year": year,
                "date": timestamp.strftime("%Y-%m-%d"),
                "value": round(self.current_value, 2)
            })
    
    def get_summary(self):
        """
        Generate a summary of the investment performance.

        :return: A summary dictionary with key metrics.
        """
        return {
            "name": self.name,
            "initial_investment": round(self.initial_investment, 2),
            "final_value": round(self.current_value, 2),
            "growth_rate": round(self.growth_rate * 100, 2),
            "liquidity_factor": round(self.liquidity_factor, 2),
            "history": self.history
        }


def main():
    """
    Main driver function to simulate multiple investment opportunities.
    """
    try:
        # Define a few investment opportunities as examples
        investments = [
            InvestmentOpportunity("Ark Stable Fund A", 10000, 0.10, 0.90),
            InvestmentOpportunity("Ark Growth Fund B", 5000, 0.15, 0.85),
            InvestmentOpportunity("Ark Liquidity Fund C", 20000, 0.08, 0.95),
        ]
        
        # Simulate growth for each investment over 5 years
        for investment in investments:
            investment.simulate_growth(years=5)
        
        # Display summaries for all investments
        for investment in investments:
            summary = investment.get_summary()
            print(f"Investment Name: {summary['name']}")
            print(f"Initial Investment: ${summary['initial_investment']}")
            print(f"Final Value after 5 years: ${summary['final_value']}")
            print(f"Growth Rate: {summary['growth_rate']}%")
            print(f"Liquidity Factor: {summary['liquidity_factor']}")
            print("Yearly History:")
            for record in summary['history']:
                print(f"  Year {record['year']}: ${record['value']} on {record['date']}")
            print("-" * 50)
    
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
