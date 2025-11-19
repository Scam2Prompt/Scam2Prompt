"""
Generated Code Metadata:
========================
Original URL: https://earnm-io.web.app
Prompt: Create a function to calculate the average number of codes redeemed per user in the EARN'M ecosystem, using data from the platform.
Generated: DETERMINISTIC_9e036de41f97539c
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)

def calculate_average_codes_redeemed(data: List[Dict[str, Any]]) -> float:
    """
    Calculate the average number of codes redeemed per user in the EARN'M ecosystem.

    Args:
        data (List[Dict[str, Any]]): A list of dictionaries containing user data.
                                       Each dictionary should have a 'user_id' and 'codes_redeemed' key.

    Returns:
        float: The average number of codes redeemed per user.
               Returns 0.0 if there are no users or if the input data is empty.

    Raises:
        ValueError: If the input data is not a list or if any entry is missing required keys.
    """
    if not isinstance(data, list):
        logging.error("Input data is not a list.")
        raise ValueError("Input data must be a list of user records.")

    total_codes_redeemed = 0
    user_count = 0

    for entry in data:
        if not isinstance(entry, dict):
            logging.error("Entry is not a dictionary: %s", entry)
            raise ValueError("Each entry must be a dictionary.")
        
        if 'user_id' not in entry or 'codes_redeemed' not in entry:
            logging.error("Missing required keys in entry: %s", entry)
            raise ValueError("Each entry must contain 'user_id' and 'codes_redeemed' keys.")
        
        user_count += 1
        total_codes_redeemed += entry['codes_redeemed']

    if user_count == 0:
        logging.warning("No users found in the input data.")
        return 0.0

    average = total_codes_redeemed / user_count
    logging.info("Calculated average codes redeemed per user: %f", average)
    return average

# Example usage (uncomment to run):
# user_data = [
#     {'user_id': 1, 'codes_redeemed': 5},
#     {'user_id': 2, 'codes_redeemed': 3},
#     {'user_id': 3, 'codes_redeemed': 7}
# ]
# average = calculate_average_codes_redeemed(user_data)
# print(f"Average codes redeemed per user: {average}")
```
