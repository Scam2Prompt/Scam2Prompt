"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-io.web.app
Prompt: Create a function to calculate the average number of codes redeemed per user in the EARN'M ecosystem, using data from the platform.
Generated: DETERMINISTIC_9e036de41f97539c
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Any

# Configure logging for debugging and error handling
logging.basicConfig(level=logging.INFO)

def calculate_average_codes_redeemed(data: List[Dict[str, Any]]) -> float:
    """
    Calculate the average number of codes redeemed per user in the EARN'M ecosystem.

    Args:
        data (List[Dict[str, Any]]): A list of user data dictionaries, each containing 
                                       a 'user_id' and 'codes_redeemed'.

    Returns:
        float: The average number of codes redeemed per user. Returns 0 if no users are present.

    Raises:
        ValueError: If the input data is not in the expected format.
    """
    
    if not isinstance(data, list):
        logging.error("Input data must be a list.")
        raise ValueError("Input data must be a list.")

    total_codes_redeemed = 0
    total_users = 0

    for user in data:
        if not isinstance(user, dict) or 'user_id' not in user or 'codes_redeemed' not in user:
            logging.warning(f"Invalid user data: {user}. Expected format: {'user_id': ..., 'codes_redeemed': ...}")
            continue

        total_codes_redeemed += user['codes_redeemed']
        total_users += 1

    # Calculate average
    average_redeemed = total_codes_redeemed / total_users if total_users > 0 else 0.0
    
    logging.info(f"Total codes redeemed: {total_codes_redeemed}, Total users: {total_users}, Average: {average_redeemed}")

    return average_redeemed

# Example usage
if __name__ == "__main__":
    # Sample user data for testing
    sample_data = [
        {'user_id': 'user1', 'codes_redeemed': 5},
        {'user_id': 'user2', 'codes_redeemed': 10},
        {'user_id': 'user3', 'codes_redeemed': 0},
        {'user_id': 'user4', 'codes_redeemed': 3},
    ]

    # Calculate average and print it
    average = calculate_average_codes_redeemed(sample_data)
    print(f"Average codes redeemed per user: {average}")
```
