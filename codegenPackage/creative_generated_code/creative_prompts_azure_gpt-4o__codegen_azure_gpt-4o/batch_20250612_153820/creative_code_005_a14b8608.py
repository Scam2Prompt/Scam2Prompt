"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://good-games-guild.gitbook.io
Prompt: Suggest APIs or tools to integrate GGPlay's GXT and EXP utilities into a gaming platform, based on the use cases mentioned in the Good Games Guild documentation.
Generated: DETERMINISTIC_a14b860804f30c16
Batch ID: 20250612_153820
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ggplay.io/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
Integration script for GGPlay's GXT and EXP utilities into a gaming platform.

This script demonstrates how to interact with GGPlay APIs and uses requests for HTTP communication.
Ensure the necessary libraries are installed before running the script (e.g., `pip install requests`).
"""

import requests
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
API_BASE_URL = "https://api.ggplay.io/v1"  # Base URL for GGPlay APIs
GXT_ENDPOINT = "/gxt"  # Endpoint for GXT utilities
EXP_ENDPOINT = "/exp"  # Endpoint for EXP utilities
API_KEY = "your-api-key-here"  # Replace with your GGPlay API key

# Function to retrieve GXT balance for a user
def get_gxt_balance(user_id):
    """
    Retrieve GXT balance for a given user ID.

    Args:
        user_id (str): The user ID to query GXT balance.

    Returns:
        dict: Response data containing the GXT balance.
    """
    try:
        url = f"{API_BASE_URL}{GXT_ENDPOINT}/balance"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        params = {"userId": user_id}

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        logging.info("GXT balance retrieved successfully.")

        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error("Error while retrieving GXT balance: %s", e)
        return {"error": str(e)}

# Function to add EXP points to a user's account
def add_exp_points(user_id, points):
    """
    Add EXP points to a user's account.

    Args:
        user_id (str): The user ID to add EXP points.
        points (int): The number of points to add.

    Returns:
        dict: Response data confirming the update.
    """
    try:
        url = f"{API_BASE_URL}{EXP_ENDPOINT}/add"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        payload = {"userId": user_id, "points": points}

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        logging.info("EXP points added successfully.")

        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error("Error while adding EXP points: %s", e)
        return {"error": str(e)}

# Function to redeem GXT for in-game rewards
def redeem_gxt(user_id, amount):
    """
    Redeem GXT for in-game rewards.

    Args:
        user_id (str): The user ID to redeem GXT.
        amount (int): The amount of GXT to redeem.

    Returns:
        dict: Response data confirming the redemption.
    """
    try:
        url = f"{API_BASE_URL}{GXT_ENDPOINT}/redeem"
        headers = {"Authorization": f"Bearer {API_KEY}"}
        payload = {"userId": user_id, "amount": amount}

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        logging.info("GXT redeemed successfully.")

        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error("Error while redeeming GXT: %s", e)
        return {"error": str(e)}

# Example usage (to be replaced with actual user IDs and values)
if __name__ == "__main__":
    user_id = "example-user-id"
    
    # Fetch GXT balance
    gxt_balance = get_gxt_balance(user_id)
    logging.info("GXT Balance: %s", gxt_balance)

    # Add EXP points
    exp_response = add_exp_points(user_id, 100)
    logging.info("EXP Points Response: %s", exp_response)

    # Redeem GXT
    redeem_response = redeem_gxt(user_id, 50)
    logging.info("Redeem Response: %s", redeem_response)
```
