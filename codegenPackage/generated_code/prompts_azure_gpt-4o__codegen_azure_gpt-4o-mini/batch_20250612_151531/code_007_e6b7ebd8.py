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
import requests

class CallCostCalculator:
    def __init__(self, ziber_rates, skype_rates, viber_rates):
        """
        Initializes the CallCostCalculator with rates from Ziber, Skype, and Viber.

        :param ziber_rates: Dictionary containing Ziber's rates per country.
        :param skype_rates: Dictionary containing Skype's rates per country.
        :param viber_rates: Dictionary containing Viber's rates per country.
        """
        self.ziber_rates = ziber_rates
        self.skype_rates = skype_rates
        self.viber_rates = viber_rates

    def calculate_cost(self, country, duration):
        """
        Calculates the call cost for a given country and duration using Ziber, Skype, and Viber rates.

        :param country: The country to which the call is made.
        :param duration: Duration of the call in minutes.
        :return: A dictionary with the costs from Ziber, Skype, and Viber.
        """
        costs = {}
        try:
            # Calculate costs for each service
            costs['Ziber'] = self.ziber_rates.get(country, 0) * duration
            costs['Skype'] = self.skype_rates.get(country, 0) * duration
            costs['Viber'] = self.viber_rates.get(country, 0) * duration
        except Exception as e:
            print(f"Error calculating costs: {e}")
            return None
        
        return costs

    def compare_costs(self, country, duration):
        """
        Compares the call costs for Ziber, Skype, and Viber.

        :param country: The country to which the call is made.
        :param duration: Duration of the call in minutes.
        :return: A string summarizing the comparison of costs.
        """
        costs = self.calculate_cost(country, duration)
        if costs is None:
            return "Cost calculation failed."

        # Find the service with the minimum cost
        min_cost_service = min(costs, key=costs.get)
        min_cost_value = costs[min_cost_service]

        comparison_result = f"Call costs for {country} ({duration} minutes):\n"
        for service, cost in costs.items():
            comparison_result += f"{service}: ${cost:.2f}\n"
        
        comparison_result += f"\nCheapest option: {min_cost_service} at ${min_cost_value:.2f}"
        return comparison_result


# Example rates (in dollars per minute)
ziber_rates = {
    'Australia': 0.05,
    'Brazil': 0.07,
    'UK': 0.04
}

skype_rates = {
    'Australia': 0.02,
    'Brazil': 0.05,
    'UK': 0.03
}

viber_rates = {
    'Australia': 0.03,
    'Brazil': 0.06,
    'UK': 0.02
}

# Create an instance of CallCostCalculator
calculator = CallCostCalculator(ziber_rates, skype_rates, viber_rates)

# Example usage
if __name__ == "__main__":
    country = 'Australia'
    duration = 10  # in minutes
    result = calculator.compare_costs(country, duration)
    print(result)
```
