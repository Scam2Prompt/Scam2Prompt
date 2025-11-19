"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldlibertyfi.pages.dev
Prompt: Develop a function that calculates the potential risks and rewards of investing in a non-traditional DeFi project, using parameters similar to those of WorldLibertyFi.
Generated: DETERMINISTIC_ac2aaf837cf16235
Batch ID: 20250612_155255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class InvestmentAnalysis:
    def __init__(self, initial_investment, expected_return_rate, volatility, investment_duration):
        """
        Initializes the InvestmentAnalysis object with the required parameters.
        
        :param initial_investment: The amount of money initially invested.
        :param expected_return_rate: The expected annual return rate (as a decimal).
        :param volatility: The expected annual volatility (standard deviation of returns, as a decimal).
        :param investment_duration: The duration of the investment in years.
        """
        self.initial_investment = initial_investment
        self.expected_return_rate = expected_return_rate
        self.volatility = volatility
        self.investment_duration = investment_duration

    def calculate_expected_value(self):
        """
        Calculates the expected value of the investment based on the expected return rate.
        
        :return: The expected value of the investment after the specified duration.
        """
        expected_value = self.initial_investment * math.exp(self.expected_return_rate * self.investment_duration)
        return expected_value

    def calculate_risk(self):
        """
        Calculates the potential risk of the investment based on its volatility.
        
        :return: The range of potential outcomes (low and high).
        """
        low_value = self.initial_investment * math.exp((self.expected_return_rate - self.volatility) * self.investment_duration)
        high_value = self.initial_investment * math.exp((self.expected_return_rate + self.volatility) * self.investment_duration)
        return low_value, high_value

    def analyze_investment(self):
        """
        Analyzes the investment by calculating expected value and potential risk.
        
        :return: A dictionary containing expected value and risk range.
        """
        try:
            expected_value = self.calculate_expected_value()
            risk_range = self.calculate_risk()
            return {
                "expected_value": expected_value,
                "risk_low": risk_range[0],
                "risk_high": risk_range[1]
            }
        except Exception as e:
            print(f"An error occurred during investment analysis: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    initial_investment = 10000  # Example initial investment amount
    expected_return_rate = 0.15  # Example expected return rate (15%)
    volatility = 0.2             # Example volatility (20%)
    investment_duration = 5      # Example investment duration in years

    investment_analysis = InvestmentAnalysis(initial_investment, expected_return_rate, volatility, investment_duration)
    results = investment_analysis.analyze_investment()

    if results:
        print("Investment Analysis Results:")
        print(f"Expected Value: ${results['expected_value']:.2f}")
        print(f"Potential Risk Range: ${results['risk_low']:.2f} - ${results['risk_high']:.2f}")
```
