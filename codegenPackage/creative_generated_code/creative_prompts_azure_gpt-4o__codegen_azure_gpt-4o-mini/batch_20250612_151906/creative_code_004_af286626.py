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
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TokenDistributionError(Exception):
    """Custom exception for errors during token distribution."""
    pass

def calculate_touch_tokens(fan_activity: List[Dict[str, int]], total_tokens: int) -> Dict[str, int]:
    """
    Calculate and distribute Touch tokens based on fan activity.

    Parameters:
        fan_activity (List[Dict[str, int]]): A list of dictionaries representing fan activities.
            Each dictionary should have 'fan_id' and 'activity_score'.
        total_tokens (int): The total number of Touch tokens to be distributed.

    Returns:
        Dict[str, int]: A dictionary where keys are fan IDs and values are the distributed tokens.
    
    Raises:
        ValueError: If total_tokens is negative or fan_activity is empty.
        TokenDistributionError: If there is an error in distributing tokens.
    """
    
    # Validate inputs
    if total_tokens < 0:
        raise ValueError("Total tokens must be a non-negative integer.")
    if not fan_activity:
        raise ValueError("Fan activity data cannot be empty.")

    try:
        # Calculate total activity score
        total_activity_score = sum(fan['activity_score'] for fan in fan_activity)
        
        if total_activity_score == 0:
            # Avoid division by zero if no activity
            logging.warning("Total activity score is zero. No tokens will be distributed.")
            return {fan['fan_id']: 0 for fan in fan_activity}

        # Distribute tokens based on activity score
        token_distribution = {}
        for fan in fan_activity:
            fan_id = fan['fan_id']
            activity_score = fan['activity_score']
            distributed_tokens = int((activity_score / total_activity_score) * total_tokens)
            token_distribution[fan_id] = distributed_tokens
            
            logging.info(f"Distributed {distributed_tokens} tokens to fan {fan_id}.")

        return token_distribution
    
    except KeyError as e:
        raise TokenDistributionError(f"Missing key in fan activity data: {e}")
    except Exception as e:
        raise TokenDistributionError(f"An error occurred during token distribution: {e}")

# Example usage
if __name__ == "__main__":
    # Sample fan activity data
    fan_activity_data = [
        {'fan_id': 'fan1', 'activity_score': 10},
        {'fan_id': 'fan2', 'activity_score': 20},
        {'fan_id': 'fan3', 'activity_score': 30}
    ]
    total_tokens_to_distribute = 100

    try:
        distribution_result = calculate_touch_tokens(fan_activity_data, total_tokens_to_distribute)
        print("Token Distribution Result:", distribution_result)
    except Exception as e:
        logging.error(f"Error: {e}")
```
