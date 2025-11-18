"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syrup-drips.pages.dev
Prompt: Write a function to calculate the average yield from Syrup rewards for lenders participating in the protocol during a specific season.
Generated: DETERMINISTIC_3ba1e43650d5ed97
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Union

class InvalidDataError(Exception):
    """Custom exception for handling invalid data input."""
    pass

def calculate_average_yield(rewards: List[Dict[str, Union[str, float]]], season: str) -> float:
    """
    Calculate the average yield from Syrup rewards for lenders during a specific season.

    Args:
        rewards (List[Dict[str, Union[str, float]]]): A list of dictionaries containing reward data.
        season (str): The season for which to calculate the average yield.

    Returns:
        float: The average yield for the specified season.

    Raises:
        InvalidDataError: If the rewards data is invalid or if the season is not found in the data.
    """
    total_yield = 0.0
    count = 0

    # Iterate through each reward entry
    for reward in rewards:
        # Validate the structure of reward data
        if 'season' not in reward or 'yield' not in reward:
            raise InvalidDataError("Invalid reward data structure. Expected 'season' and 'yield' keys.")

        # Check if the current reward belongs to the specified season
        if reward['season'] == season:
            # Validate that yield value is a float
            if not isinstance(reward['yield'], (int, float)):
                raise InvalidDataError(f"Invalid yield value: {reward['yield']}. Expected a number.")
            total_yield += reward['yield']
            count += 1

    # Calculate and return the average yield
    if count == 0:
        raise InvalidDataError(f"No rewards found for the season: {season}.")
    
    average_yield = total_yield / count
    return average_yield

# Example usage
if __name__ == "__main__":
    reward_data = [
        {'season': 'Fall 2023', 'yield': 5.0},
        {'season': 'Fall 2023', 'yield': 7.5},
        {'season': 'Winter 2023', 'yield': 6.0},
        {'season': 'Fall 2023', 'yield': 4.5},
    ]

    try:
        average = calculate_average_yield(reward_data, 'Fall 2023')
        print(f"Average yield for Fall 2023: {average:.2f}")
    except InvalidDataError as e:
        print(f"Error calculating average yield: {e}")
```
