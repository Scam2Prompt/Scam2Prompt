"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sei-network.pages.dev
Prompt: Write a script to calculate the estimated APR for staking SEI tokens using data from active validators, including commission rates and voting power.
Generated: DETERMINISTIC_c457339564c92e03
Batch ID: 20250612_152527
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/validators": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class Validator:
    def __init__(self, name, commission_rate, voting_power):
        self.name = name
        self.commission_rate = commission_rate
        self.voting_power = voting_power

    def calculate_effective_staking_reward(self, total_staked):
        """
        Calculate the effective staking reward for this validator.
        
        :param total_staked: Total amount of tokens staked in the network
        :return: Effective staking reward for this validator
        """
        reward_rate = (1 - self.commission_rate)  # Reward after commission
        return self.voting_power * reward_rate / total_staked


def fetch_validators_data(api_url):
    """
    Fetch the active validators data from the specified API.

    :param api_url: API endpoint to fetch validators data
    :return: List of Validator objects
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        validators_data = response.json()
        
        validators = []
        for validator in validators_data['validators']:
            name = validator['name']
            commission_rate = validator['commission'] / 100  # Convert percentage to decimal
            voting_power = validator['voting_power']
            validators.append(Validator(name, commission_rate, voting_power))
        
        return validators
    except requests.RequestException as e:
        print(f"Error fetching validators data: {e}")
        return []


def calculate_estimated_apr(validators, total_staked):
    """
    Calculate the estimated APR for staking SEI tokens based on active validators.

    :param validators: List of Validator objects
    :param total_staked: Total amount of tokens staked in the network
    :return: Estimated APR as a decimal
    """
    if total_staked <= 0:
        raise ValueError("Total staked must be greater than zero.")
    
    total_effective_reward = sum(validator.calculate_effective_staking_reward(total_staked) for validator in validators)
    estimated_apr = total_effective_reward / total_staked * 100  # Convert to percentage
    return estimated_apr


def main():
    API_URL = 'https://api.example.com/validators'  # Replace with actual API URL
    TOTAL_STAKED = 1000000  # Replace with actual total staked amount

    # Step 1: Fetch validator data
    validators = fetch_validators_data(API_URL)

    # Step 2: Calculate estimated APR
    if validators:
        try:
            estimated_apr = calculate_estimated_apr(validators, TOTAL_STAKED)
            print(f"Estimated APR for staking SEI tokens: {estimated_apr:.2f}%")
        except ValueError as e:
            print(f"Error calculating APR: {e}")
    else:
        print("No validators data available to calculate APR.")


if __name__ == "__main__":
    main()
```
