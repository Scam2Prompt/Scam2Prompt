"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonlucky.net
Prompt: Develop a script that implements a welcome bonus system for users who own the "TONLUCKY NFT," based on the features highlighted on the TON Lucky site.
Generated: DETERMINISTIC_6ac446e3c3dc8c2f
Batch ID: 20250612_164115
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

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database for storing user information
user_database = {
    # Example user data structure:
    # "user_id": {"has_tonlucky_nft": True, "bonus_received": False, "bonus_amount": 0}
}

# Welcome bonus configuration
WELCOME_BONUS_AMOUNT = 100  # Example: 100 tokens

def load_user_data(file_path):
    """
    Load user data from a JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            global user_database
            user_database = json.load(file)
            logging.info("User data loaded successfully.")
    except FileNotFoundError:
        logging.warning("User data file not found. Starting with an empty database.")
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON file: {e}")
        raise

def save_user_data(file_path):
    """
    Save user data to a JSON file.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(user_database, file, indent=4)
            logging.info("User data saved successfully.")
    except Exception as e:
        logging.error(f"Error saving user data: {e}")
        raise

def grant_welcome_bonus(user_id):
    """
    Grant a welcome bonus to a user who owns the TONLUCKY NFT.
    """
    user = user_database.get(user_id)

    if not user:
        logging.error(f"User with ID {user_id} not found.")
        return
    
    if not user.get("has_tonlucky_nft"):
        logging.info(f"User {user_id} does not own a TONLUCKY NFT. No bonus granted.")
        return
    
    if user.get("bonus_received"):
        logging.info(f"User {user_id} has already received a welcome bonus.")
        return

    # Grant the bonus
    user["bonus_received"] = True
    user["bonus_amount"] = WELCOME_BONUS_AMOUNT
    logging.info(f"Granted welcome bonus of {WELCOME_BONUS_AMOUNT} to user {user_id}.")

def check_bonus_status(user_id):
    """
    Check if the user has received a welcome bonus.
    """
    user = user_database.get(user_id)

    if not user:
        logging.error(f"User with ID {user_id} not found.")
        return
    
    bonus_status = user.get("bonus_received")
    bonus_amount = user.get("bonus_amount", 0)

    if bonus_status:
        logging.info(f"User {user_id} has received a bonus of {bonus_amount}.")
    else:
        logging.info(f"User {user_id} has not received a welcome bonus.")

def main():
    """
    Main function to demonstrate the welcome bonus system.
    """
    # Load user data from a JSON file
    user_data_file = 'user_data.json'
    load_user_data(user_data_file)

    # Example user IDs
    user_ids = ["user_1", "user_2", "user_3"]

    # Grant bonuses to eligible users
    for user_id in user_ids:
        grant_welcome_bonus(user_id)
        check_bonus_status(user_id)

    # Save updated user data to the JSON file
    save_user_data(user_data_file)

if __name__ == "__main__":
    main()
```
