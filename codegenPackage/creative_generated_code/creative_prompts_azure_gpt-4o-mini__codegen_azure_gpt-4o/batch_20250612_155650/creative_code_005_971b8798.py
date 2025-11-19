"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://good-games-guild.gitbook.io
Prompt: Create a function to calculate the distribution schedule of the $GGG token based on the metrics provided in the Good Games documentation.
Generated: DETERMINISTIC_971b879838999f55
Batch ID: 20250612_155650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

def calculate_distribution_schedule(token_total: int, phases: List[Dict[str, float]]) -> List[Dict[str, float]]:
    """
    Calculate the distribution schedule for the $GGG token.

    Args:
        token_total (int): Total number of tokens to be distributed.
        phases (List[Dict[str, float]]): A list of phases, where each phase is a dictionary containing:
            - 'name' (str): The name of the phase (e.g., 'Seed Round').
            - 'percentage' (float): Percentage of total tokens to be allocated to this phase (in decimal form, e.g., 0.1 for 10%).

    Returns:
        List[Dict[str, float]]: A list of dictionaries containing the distribution schedule for each phase.
            - 'name' (str): Name of the phase.
            - 'allocation' (float): Number of tokens allocated to this phase.

    Raises:
        ValueError: If the sum of percentages exceeds 1 (100%) or any percentage is invalid.
    """
    # Validate input percentages
    total_percentage = sum(phase['percentage'] for phase in phases)
    if total_percentage > 1.0:
        raise ValueError("Total percentage exceeds 100%. Please check the phase percentages.")
    if any(phase['percentage'] < 0 for phase in phases):
        raise ValueError("Negative percentages are not allowed.")

    # Generate distribution schedule
    distribution_schedule = []
    for phase in phases:
        allocation = round(token_total * phase['percentage'])
        distribution_schedule.append({
            'name': phase['name'],
            'allocation': allocation
        })

    return distribution_schedule


# Example Usage
if __name__ == "__main__":
    try:
        # Define total tokens and phase details
        total_tokens = 1000000  # Example: 1,000,000 tokens
        token_phases = [
            {'name': 'Seed Round', 'percentage': 0.10},  # 10%
            {'name': 'Private Sale', 'percentage': 0.20},  # 20%
            {'name': 'Public Sale', 'percentage': 0.05},  # 5%
            {'name': 'Team Allocation', 'percentage': 0.15},  # 15%
            {'name': 'Ecosystem Fund', 'percentage': 0.30},  # 30%
            {'name': 'Liquidity Pool', 'percentage': 0.10},  # 10%
            {'name': 'Marketing & Partnerships', 'percentage': 0.10}  # 10%
        ]

        # Calculate and display the distribution schedule
        schedule = calculate_distribution_schedule(total_tokens, token_phases)
        for phase in schedule:
            print(f"{phase['name']}: {phase['allocation']} tokens")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
