"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-enigma.org
Prompt: Write a script to automate the pairing of users with investment education firms based on their registration details, inspired by Immediate Migna's tailored matching system.
Generated: DETERMINISTIC_c880536156bc01cc
Batch ID: 20250612_150854
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
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the structure of a user and firm for clarity
class User:
    def __init__(self, user_id: str, preferences: Dict[str, str]):
        """
        Initialize a User object.

        Args:
            user_id (str): Unique identifier for the user.
            preferences (Dict[str, str]): Dictionary of user preferences for matching.
        """
        self.user_id = user_id
        self.preferences = preferences


class InvestmentFirm:
    def __init__(self, firm_id: str, criteria: Dict[str, str]):
        """
        Initialize an InvestmentFirm object.

        Args:
            firm_id (str): Unique identifier for the firm.
            criteria (Dict[str, str]): Dictionary of criteria for matching users.
        """
        self.firm_id = firm_id
        self.criteria = criteria


def load_users(file_path: str) -> List[User]:
    """
    Load user data from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing user data.

    Returns:
        List[User]: List of User objects.
    """
    try:
        with open(file_path, 'r') as f:
            user_data = json.load(f)
        return [User(user['user_id'], user['preferences']) for user in user_data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error loading user data: {e}")
        return []


def load_firms(file_path: str) -> List[InvestmentFirm]:
    """
    Load investment firm data from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing firm data.

    Returns:
        List[InvestmentFirm]: List of InvestmentFirm objects.
    """
    try:
        with open(file_path, 'r') as f:
            firm_data = json.load(f)
        return [InvestmentFirm(firm['firm_id'], firm['criteria']) for firm in firm_data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error loading firm data: {e}")
        return []


def match_users_to_firms(users: List[User], firms: List[InvestmentFirm]) -> Dict[str, str]:
    """
    Match users to investment firms based on their preferences and criteria.

    Args:
        users (List[User]): List of User objects.
        firms (List[InvestmentFirm]): List of InvestmentFirm objects.

    Returns:
        Dict[str, str]: Dictionary mapping user IDs to firm IDs.
    """
    matches = {}

    for user in users:
        for firm in firms:
            if all(user.preferences.get(key) == firm.criteria.get(key) for key in firm.criteria.keys()):
                matches[user.user_id] = firm.firm_id
                logging.info(f"Matched user {user.user_id} with firm {firm.firm_id}")
                break

        if user.user_id not in matches:
            logging.warning(f"No matching firm found for user {user.user_id}")

    return matches


def save_matches(matches: Dict[str, str], file_path: str):
    """
    Save the user-to-firm matches to a JSON file.

    Args:
        matches (Dict[str, str]): Dictionary of matches.
        file_path (str): Path to the JSON file to save matches.
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(matches, f, indent=4)
        logging.info(f"Matches saved to {file_path}")
    except IOError as e:
        logging.error(f"Error saving matches: {e}")


def main():
    """
    Main function to execute the matching process.
    """
    user_file = "users.json"
    firm_file = "firms.json"
    output_file = "matches.json"

    logging.info("Loading user and firm data...")
    users = load_users(user_file)
    firms = load_firms(firm_file)

    if not users or not firms:
        logging.error("User or firm data is missing. Exiting...")
        return

    logging.info("Matching users to firms...")
    matches = match_users_to_firms(users, firms)

    logging.info("Saving matches...")
    save_matches(matches, output_file)


if __name__ == "__main__":
    main()
```
