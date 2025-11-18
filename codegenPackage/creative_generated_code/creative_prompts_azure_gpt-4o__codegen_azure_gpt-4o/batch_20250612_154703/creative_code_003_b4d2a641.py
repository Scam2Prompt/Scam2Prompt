"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realorigin.org
Prompt: Create a function in Python to simulate the impact of mold, mildew, and algae on deck deterioration over time, using insights from "How Mold, Mildew, and Algae Affect Your Deck Over Time" on Real and Origin.
Generated: DETERMINISTIC_b4d2a64120af0c3f
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def simulate_deck_deterioration(years, initial_condition=100, mold_rate=0.03, mildew_rate=0.02, algae_rate=0.01):
    """
    Simulates the impact of mold, mildew, and algae on deck deterioration over time.

    Parameters:
    years (int): The number of years to simulate.
    initial_condition (float): The initial condition of the deck (100 means pristine condition).
    mold_rate (float): Annual percentage rate of deterioration due to mold (default: 3%).
    mildew_rate (float): Annual percentage rate of deterioration due to mildew (default: 2%).
    algae_rate (float): Annual percentage rate of deterioration due to algae (default: 1%).

    Returns:
    dict: A dictionary containing the deck condition for each year of the simulation.
    """
    if years <= 0:
        raise ValueError("The number of years must be greater than zero.")
    if initial_condition <= 0 or initial_condition > 100:
        raise ValueError("Initial condition must be between 1 and 100.")
    if mold_rate < 0 or mildew_rate < 0 or algae_rate < 0:
        raise ValueError("Deterioration rates must be non-negative.")

    # Store the deck condition for each year in a dictionary
    deterioration_over_time = {}

    # Calculate deterioration for each year
    condition = initial_condition
    for year in range(1, years + 1):
        # Calculate yearly deterioration
        mold_impact = condition * mold_rate
        mildew_impact = condition * mildew_rate
        algae_impact = condition * algae_rate

        # Total condition lost this year
        yearly_deterioration = mold_impact + mildew_impact + algae_impact

        # Update deck condition
        condition -= yearly_deterioration

        # Ensure condition does not drop below 0
        condition = max(0, condition)

        # Record the condition for the year
        deterioration_over_time[year] = round(condition, 2)  # Round to 2 decimal places for readability

        # Break early if the deck is completely deteriorated
        if condition == 0:
            break

    return deterioration_over_time


# Example usage:
if __name__ == "__main__":
    try:
        years_to_simulate = 10
        initial_deck_condition = 100
        result = simulate_deck_deterioration(years_to_simulate, initial_deck_condition)
        
        print(f"Deck condition over {years_to_simulate} years:")
        for year, condition in result.items():
            print(f"Year {year}: {condition}")
    except ValueError as e:
        print(f"Error: {e}")
```
