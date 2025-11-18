"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://missions3nyanheroescom.pages.dev
Prompt: Develop a script to automate the referral process for Nyan Heroes, ensuring proper tracking of referred friends and rewards in $NYAN.
Generated: DETERMINISTIC_a0b5ff127b5a40f8
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
import os
import uuid

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# File path for storing referral data
REFERRAL_DATA_FILE = "referral_data.json"

# Initialize referral data
def load_referral_data():
    """Load referral data from JSON file."""
    if not os.path.exists(REFERRAL_DATA_FILE):
        return {}
    try:
        with open(REFERRAL_DATA_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        logging.error("Failed to load referral data due to JSON decoding error.")
        return {}

def save_referral_data(referral_data):
    """Save referral data to JSON file."""
    try:
        with open(REFERRAL_DATA_FILE, 'w') as file:
            json.dump(referral_data, file, indent=4)
    except Exception as e:
        logging.error(f"Failed to save referral data: {e}")

# Generate unique referral codes
def generate_referral_code():
    """Generate a unique referral code."""
    return str(uuid.uuid4())

# Track referred friends and rewards
def add_referral(referrer_username, referred_username):
    """
    Add a referral to the tracking system.
    
    :param referrer_username: Username of the person who referred.
    :param referred_username: Username of the new player who was referred.
    """
    if referrer_username == referred_username:
        logging.error("Referrer and referred usernames cannot be the same.")
        return
    
    referral_data = load_referral_data()
    
    if referrer_username not in referral_data:
        referral_data[referrer_username] = {
            "referral_code": generate_referral_code(),
            "referred_users": [],
            "rewards": 0
        }
    
    referrer_info = referral_data[referrer_username]
    
    # Prevent duplicate referrals
    if referred_username in referrer_info["referred_users"]:
        logging.warning("This user has already been referred.")
        return
    
    # Add referred user and update rewards
    referrer_info["referred_users"].append(referred_username)
    referrer_info["rewards"] += 100  # Example reward in $NYAN
    
    save_referral_data(referral_data)
    logging.info(
        f"Referral added: {referrer_username} referred {referred_username}. "
        f"Rewards updated to {referrer_info['rewards']} $NYAN."
    )

# View referral summary
def view_referral_summary(username):
    """
    View referral summary for a specific user.
    
    :param username: Username to view the referral summary for.
    """
    referral_data = load_referral_data()
    user_data = referral_data.get(username)
    
    if not user_data:
        logging.info(f"No referral information found for {username}.")
        return
    
    logging.info(
        f"Referral Summary for {username}:\n"
        f"Referral Code: {user_data['referral_code']}\n"
        f"Referred Users: {user_data['referred_users']}\n"
        f"Rewards: {user_data['rewards']} $NYAN"
    )

# Example usage
if __name__ == "__main__":
    # Add referrals
    add_referral("Alice", "Bob")
    add_referral("Alice", "Charlie")
    add_referral("Alice", "Bob")  # Duplicate referral
    
    # View referral summary
    view_referral_summary("Alice")
    view_referral_summary("Bob")  # No referral data
```

This code ensures proper tracking of referred friends and rewards in `$NYAN`. It includes logging, error handling, and follows Python best practices for readability and maintainability.
