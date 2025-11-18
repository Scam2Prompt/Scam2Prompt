"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clearpool.pages.dev
Prompt: Generate code to calculate the total voting power percentage for each Clearpool oracle based on the provided CPOOL staking data.
Generated: DETERMINISTIC_ef84c655d9a4712d
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the total voting power percentage for each Clearpool oracle based on CPOOL staking data

# Import necessary libraries
import json

def calculate_voting_power_percentage(staking_data):
    """
    Function to calculate total voting power percentage for each oracle
    based on CPOOL staking data.

    Args:
        staking_data (list): A list of dictionaries containing oracle staking data.
                             Each dictionary should have 'oracle' and 'stake' fields.

    Returns:
        dict: A dictionary with oracle names as keys and their voting power percentages as values.
    """
    try:
        # Validate input data
        if not isinstance(staking_data, list):
            raise ValueError("Staking data must be a list of dictionaries.")

        # Calculate total stake
        total_stake = sum(item['stake'] for item in staking_data if 'stake' in item and isinstance(item['stake'], (int, float)))

        if total_stake == 0:
            raise ValueError("Total stake cannot be zero.")

        # Calculate voting power percentages
        voting_power_percentages = {
            item['oracle']: round((item['stake'] / total_stake) * 100, 2)
            for item in staking_data
            if 'oracle' in item and 'stake' in item and isinstance(item['stake'], (int, float))
        }

        return voting_power_percentages

    except (TypeError, ValueError) as e:
        # Handle errors gracefully
        print(f"Error: {e}")
        return {}

# Example staking data (replace this with actual data from Clearpool)
example_staking_data = [
    {"oracle": "Oracle1", "stake": 5000},
    {"oracle": "Oracle2", "stake": 3000},
    {"oracle": "Oracle3", "stake": 2000},
]

# Calculate voting power percentages
result = calculate_voting_power_percentage(example_staking_data)

# Output the result as JSON for readability
print(json.dumps(result, indent=4))
```
