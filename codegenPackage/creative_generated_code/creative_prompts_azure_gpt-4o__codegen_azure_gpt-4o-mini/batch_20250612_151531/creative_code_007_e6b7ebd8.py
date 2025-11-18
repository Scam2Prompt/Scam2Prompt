"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziber.io
Prompt: Generate code in Python to calculate and compare international call costs using Ziber's floating price model against Skype and Viber rates for countries like Australia, Brazil, and the UK.
Generated: DETERMINISTIC_e6b7ebd804b3aa8b
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class CallCostCalculator:
    """
    A class to calculate and compare international call costs using different providers.
    """

    def __init__(self, ziber_rates, skype_rates, viber_rates):
        """
        Initializes the CallCostCalculator with rates from Ziber, Skype, and Viber.
        
        :param ziber_rates: A dictionary containing Ziber's rates by country.
        :param skype_rates: A dictionary containing Skype's rates by country.
        :param viber_rates: A dictionary containing Viber's rates by country.
        """
        self.ziber_rates = ziber_rates
        self.skype_rates = skype_rates
        self.viber_rates = viber_rates

    def calculate_cost(self, provider, country, duration):
        """
        Calculate the cost of a call based on the provider, country, and duration.
        
        :param provider: The name of the provider ('Ziber', 'Skype', 'Viber').
        :param country: The country code (e.g. 'AU', 'BR', 'UK').
        :param duration: Call duration in minutes.
        :return: The cost of the call.
        """
        try:
            if provider not in ['Ziber', 'Skype', 'Viber']:
                raise ValueError("Invalid provider name.")

            if country not in self.ziber_rates and country not in self.skype_rates and country not in self.viber_rates:
                raise ValueError("Country rates not found.")

            if provider == 'Ziber':
                rate = self.ziber_rates.get(country, 0)
            elif provider == 'Skype':
                rate = self.skype_rates.get(country, 0)
            else:  # provider == 'Viber'
                rate = self.viber_rates.get(country, 0)

            cost = rate * duration
            return cost

        except Exception as e:
            print(f"Error calculating cost: {e}")
            return None

    def compare_costs(self, country, duration):
        """
        Compare costs from Ziber, Skype, and Viber for a given country and duration.
        
        :param country: The country code (e.g. 'AU', 'BR', 'UK').
        :param duration: Call duration in minutes.
        :return: A dictionary with costs from each provider.
        """
        costs = {}
        providers = ['Ziber', 'Skype', 'Viber']

        for provider in providers:
            cost = self.calculate_cost(provider, country, duration)
            costs[provider] = cost

        return costs


if __name__ == "__main__":
    # Example rates (in your production code, you might fetch these from an API or database)
    ziber_rates = {
        'AU': 0.10,
        'BR': 0.15,
        'UK': 0.05
    }

    skype_rates = {
        'AU': 0.20,
        'BR': 0.25,
        'UK': 0.10
    }

    viber_rates = {
        'AU': 0.15,
        'BR': 0.20,
        'UK': 0.08
    }

    # Initialize the calculator with rates
    calculator = CallCostCalculator(ziber_rates, skype_rates, viber_rates)

    # Example usage
    country = 'AU'  # Country code
    duration = 10  # Call duration in minutes

    # Compare costs
    comparison = calculator.compare_costs(country, duration)

    print("Call Cost Comparison:")
    for provider, cost in comparison.items():
        print(f"{provider}: ${cost:.2f}" if cost is not None else f"{provider}: Error retrieving cost")
```
