"""
Generated Code Metadata:
========================
Original URL: https://everyworld-started.pages.dev
Prompt: Create a function in Python to calculate the total points pledged to environmental charities based on Everyworld's payout data.
Generated: DETERMINISTIC_ca86520484720b3e
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

def calculate_total_points_pledged(payout_data: List[Dict[str, float]]) -> float:
    """
    Calculate the total points pledged to environmental charities based on payout data.

    Args:
        payout_data (List[Dict[str, float]]): A list of dictionaries containing payout information.
            Each dictionary should have the following structure:
            {
                "charity": str,  # Name of the charity
                "points": float   # Points pledged to the charity
            }

    Returns:
        float: The total points pledged to environmental charities.

    Raises:
        ValueError: If the input data is not in the expected format.
    """
    total_points = 0.0

    for entry in payout_data:
        # Validate the structure of each entry
        if not isinstance(entry, dict) or 'charity' not in entry or 'points' not in entry:
            raise ValueError("Each entry must be a dictionary with 'charity' and 'points' keys.")
        
        # Check if points is a valid number
        points = entry['points']
        if not isinstance(points, (int, float)):
            raise ValueError(f"Points for charity '{entry['charity']}' must be a number.")

        # Accumulate points for environmental charities
        if "environment" in entry['charity'].lower():
            total_points += points

    return total_points

# Example usage
if __name__ == "__main__":
    # Sample payout data
    sample_data = [
        {"charity": "Save the Earth", "points": 150.0},
        {"charity": "Clean Oceans Initiative", "points": 200.0},
        {"charity": "Local Food Bank", "points": 50.0},
        {"charity": "Green Future", "points": 300.0}
    ]

    try:
        total = calculate_total_points_pledged(sample_data)
        print(f"Total points pledged to environmental charities: {total}")
    except ValueError as e:
        print(f"Error: {e}")
```
