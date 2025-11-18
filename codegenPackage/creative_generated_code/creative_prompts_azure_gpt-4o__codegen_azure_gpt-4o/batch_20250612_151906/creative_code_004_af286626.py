"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://touchfanrewards.pages.dev
Prompt: Write a function in Python to calculate and distribute Touch tokens based on fan activity data from the Touch Room.
Generated: DETERMINISTIC_af28662622f37020
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Dict, List

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def distribute_tokens(activity_data: Dict[str, int], total_tokens: int) -> Dict[str, float]:
    """
    Distribute Touch tokens based on fan activity data.

    Parameters:
    activity_data (Dict[str, int]): A dictionary where keys are fan IDs and values are activity scores.
    total_tokens (int): The total number of Touch tokens to distribute.

    Returns:
    Dict[str, float]: A dictionary where keys are fan IDs and values are the distributed token amounts.
    """
    try:
        if not activity_data:
            raise ValueError("Activity data cannot be empty.")
        if total_tokens <= 0:
            raise ValueError("Total tokens must be greater than zero.")

        # Calculate the total activity score
        total_activity_score = sum(activity_data.values())
        if total_activity_score == 0:
            raise ValueError("Total activity score cannot be zero. Ensure fan activity data is valid.")

        # Calculate and distribute tokens proportionally based on activity scores
        distributed_tokens = {}
        for fan_id, activity_score in activity_data.items():
            token_share = (activity_score / total_activity_score) * total_tokens
            distributed_tokens[fan_id] = round(token_share, 2)  # Round to 2 decimal places for precision

        return distributed_tokens

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return {}
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return {}

# Example usage:
if __name__ == "__main__":
    # Sample fan activity data (fan_id: activity_score)
    sample_activity_data = {
        "fan_1": 120,
        "fan_2": 80,
        "fan_3": 50,
        "fan_4": 150
    }
    total_touch_tokens = 1000  # Total tokens available

    # Distribute tokens
    result = distribute_tokens(sample_activity_data, total_touch_tokens)
    print("Distributed Tokens:", result)
```
