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
# international_call_costs.py

class InternationalCallCostCalculator:
    def __init__(self):
        # Define rates in USD per minute for each service
        self.ziber_rates = {
            "Australia": 0.05,
            "Brazil": 0.10,
            "UK": 0.03
        }
        self.skype_rates = {
            "Australia": 0.06,
            "Brazil": 0.11,
            "UK": 0.04
        }
        self.viber_rates = {
            "Australia": 0.07,
            "Brazil": 0.12,
            "UK": 0.05
        }

    def calculate_call_cost(self, service_rates, country, duration_minutes):
        """
        Calculate the cost of an international call.

        Args:
            service_rates (dict): Rates for a specific service.
            country (str): Country of the call.
            duration_minutes (int): Duration of the call in minutes.

        Returns:
            float: Cost of the call.

        Raises:
            ValueError: If country is not found in service_rates.
        """
        if country not in service_rates:
            raise ValueError(f"Country '{country}' not found in service rates.")

        rate = service_rates[country]
        return rate * duration_minutes

    def compare_call_costs(self, country, duration_minutes):
        """
        Compare international call costs between Ziber, Skype, and Viber.

        Args:
            country (str): Country of the call.
            duration_minutes (int): Duration of the call in minutes.

        Returns:
            dict: Comparison of call costs for each service.

        Raises:
            ValueError: If country is not supported.
        """
        if country not in self.ziber_rates:
            raise ValueError(f"Country '{country}' not supported.")

        ziber_cost = self.calculate_call_cost(self.ziber_rates, country, duration_minutes)
        skype_cost = self.calculate_call_cost(self.skype_rates, country, duration_minutes)
        viber_cost = self.calculate_call_cost(self.viber_rates, country, duration_minutes)

        return {
            "Ziber": ziber_cost,
            "Skype": skype_cost,
            "Viber": viber_cost
        }


def main():
    calculator = InternationalCallCostCalculator()

    countries = ["Australia", "Brazil", "UK"]
    duration_minutes = 10

    for country in countries:
        try:
            costs = calculator.compare_call_costs(country, duration_minutes)
            print(f"Call costs for {country} ({duration_minutes} minutes):")
            for service, cost in costs.items():
                print(f"  {service}: ${cost:.2f}")
            print()
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
