"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld.pages.dev
Prompt: Create a function that calculates the rewards payout ratio for Everyworld participants based on their engagement activities.
Generated: DETERMINISTIC_70db9235f9d3ed0f
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

def calculate_rewards_payout_ratio(participant_data: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Calculates the rewards payout ratio for Everyworld participants based on their engagement activities.

    Args:
        participant_data (List[Dict[str, float]]): A list of dictionaries where each dictionary contains:
            - "name" (str): Name of the participant.
            - "activity_points" (float): Points earned by the participant based on engagement activities.
            - "total_contributions" (float): Total contributions made by the participant (e.g., time spent, quality contributions).

    Returns:
        Dict[str, float]: A dictionary where the keys are participant names and 
        values are their rewards payout ratios.
    """
    # Error handling: Ensure input is valid
    if not participant_data or not all(isinstance(entry, dict) for entry in participant_data):
        raise ValueError("Invalid participant data. Please provide a list of dictionaries.")

    # Error handling: Ensure each participant entry contains required keys
    required_keys = {"name", "activity_points", "total_contributions"}
    for entry in participant_data:
        if not required_keys <= entry.keys():
            raise ValueError(f"Missing required keys in participant entry: {entry}")

    # Calculate payout ratios
    payout_ratios = {}
    for entry in participant_data:
        name = entry["name"]
        activity_points = entry["activity_points"]
        total_contributions = entry["total_contributions"]

        # Error handling: Prevent division by zero
        if total_contributions <= 0:
            raise ValueError(f"Total contributions must be greater than zero for participant: {name}")

        # Calculate the payout ratio as activity points divided by total contributions
        payout_ratios[name] = activity_points / total_contributions

    return payout_ratios


# Example usage
if __name__ == "__main__":
    # Sample participant data
    participants = [
        {"name": "Alice", "activity_points": 120.5, "total_contributions": 300.0},
        {"name": "Bob", "activity_points": 95.0, "total_contributions": 200.0},
        {"name": "Charlie", "activity_points": 150.0, "total_contributions": 400.0}
    ]

    try:
        # Calculate and print rewards payout ratios
        results = calculate_rewards_payout_ratio(participants)
        for participant, ratio in results.items():
            print(f"{participant}: {ratio:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
