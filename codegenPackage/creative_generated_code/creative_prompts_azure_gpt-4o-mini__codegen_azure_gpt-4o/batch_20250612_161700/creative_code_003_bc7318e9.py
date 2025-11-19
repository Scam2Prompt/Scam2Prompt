"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormholesolana.web.app
Prompt: Develop a Python function that calculates the potential rewards from participating in the $WORMHOLE community initiatives based on the roadmap provided.
Generated: DETERMINISTIC_bc7318e95dc5720d
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict, Union

def calculate_rewards(roadmap: Dict[str, Union[int, float]], participation_scores: Dict[str, Union[int, float]]) -> Dict[str, float]:
    """
    Calculate potential rewards from participating in the $WORMHOLE community initiatives.

    Parameters:
        roadmap (dict): A dictionary where keys are initiative names and values are base reward values.
        participation_scores (dict): A dictionary where keys are initiative names and values are user's participation scores (0 to 1).

    Returns:
        dict: A dictionary where keys are initiative names and values are the calculated reward amounts.
    """
    # Validate inputs
    if not isinstance(roadmap, dict) or not isinstance(participation_scores, dict):
        raise ValueError("Both 'roadmap' and 'participation_scores' must be dictionaries.")

    rewards = {}
    
    # Calculate rewards for each initiative
    for initiative, base_reward in roadmap.items():
        # Ensure the initiative exists in participation scores
        if initiative not in participation_scores:
            # Skip initiatives without participation scores
            continue
        
        # Validate base reward and participation score
        if not isinstance(base_reward, (int, float)) or not isinstance(participation_scores[initiative], (int, float)):
            raise ValueError(f"Invalid data types for initiative '{initiative}'. Base reward and participation score must be numeric.")
        
        if not (0 <= participation_scores[initiative] <= 1):
            raise ValueError(f"Invalid participation score for initiative '{initiative}'. Must be between 0 and 1.")
        
        # Calculate reward
        rewards[initiative] = base_reward * participation_scores[initiative]
    
    return rewards

# Example usage
if __name__ == "__main__":
    # Example roadmap and participation data
    roadmap = {
        "initiative_1": 100,
        "initiative_2": 200,
        "initiative_3": 150
    }
    participation_scores = {
        "initiative_1": 0.8,
        "initiative_2": 0.5,
        "initiative_3": 1.0
    }

    try:
        rewards = calculate_rewards(roadmap, participation_scores)
        print("Calculated Rewards:", rewards)
    except ValueError as e:
        print("Error:", e)
```
