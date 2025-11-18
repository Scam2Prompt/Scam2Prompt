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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define call rates per minute for each service provider
CALL_RATES = {
    "Skype": {"Australia": 0.023, "Brazil": 0.019, "UK": 0.025},
    "Viber": {"Australia": 0.017, "Brazil": 0.015, "UK": 0.022},
    "Ziber": {"Australia": lambda minutes: 0.02 + (0.001 * minutes),
              "Brazil": lambda minutes: 0.018 + (0.0005 * minutes),
              "UK": lambda minutes: 0.024 + (0.0008 * minutes)}
}

def calculate_cost(provider, country, minutes):
    """
    Calculate the cost of an international call.

    :param provider: Name of the service provider (e.g., "Skype", "Viber", "Ziber").
    :param country: Name of the destination country (e.g., "Australia", "Brazil", "UK").
    :param minutes: Duration of the call in minutes.
    :return: Cost of the call.
    """
    try:
        if provider not in CALL_RATES:
            raise ValueError(f"Unknown provider: {provider}")
        if country not in CALL_RATES[provider]:
            raise ValueError(f"Unknown country for {provider}: {country}")
        
        # Ziber uses a dynamic pricing model based on call duration
        if provider == "Ziber":
            cost = CALL_RATES[provider][country](minutes)
        else:
            cost = CALL_RATES[provider][country] * minutes
        
        return round(cost, 2)
    except ValueError as e:
        logging.error(e)
        return None

def compare_call_costs(country, minutes):
    """
    Compare the call costs between different service providers.

    :param country: Name of the destination country.
    :param minutes: Duration of the call in minutes.
    :return: Dictionary containing the cost for each provider.
    """
    costs = {}
    for provider in CALL_RATES.keys():
        cost = calculate_cost(provider, country, minutes)
        if cost is not None:
            costs[provider] = cost
    return costs

def main():
    """
    Main function to compare call costs for given countries and minutes.
    """
    # List of countries to compare rates
    countries = ["Australia", "Brazil", "UK"]
    # Example call duration in minutes
    call_duration = 10
    
    for country in countries:
        logging.info(f"Comparing call costs for {country}, Duration: {call_duration} minutes")
        costs = compare_call_costs(country, call_duration)
        for provider, cost in costs.items():
            print(f"{provider} call cost to {country} for {call_duration} minutes: ${cost}")

if __name__ == "__main__":
    main()
```
