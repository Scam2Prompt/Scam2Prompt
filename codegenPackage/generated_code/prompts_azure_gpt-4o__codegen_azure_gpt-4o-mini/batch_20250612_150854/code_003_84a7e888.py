"""
Generated Code Metadata:
========================
Original URL: https://immediate-crest.com
Prompt: Create a script to match users with investment education firms based on their learning preferences, inspired by Immediate Crest V2's user-matching process.
Generated: DETERMINISTIC_84a7e888822a1675
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class User:
    def __init__(self, user_id: int, learning_preferences: List[str]):
        """
        Initialize a User instance.

        :param user_id: Unique identifier for the user
        :param learning_preferences: List of learning preferences (e.g., 'video', 'text', 'interactive')
        """
        self.user_id = user_id
        self.learning_preferences = learning_preferences

class Firm:
    def __init__(self, firm_id: int, offerings: List[str]):
        """
        Initialize a Firm instance.

        :param firm_id: Unique identifier for the investment education firm
        :param offerings: List of learning offerings provided by the firm
        """
        self.firm_id = firm_id
        self.offerings = offerings

def load_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Load user and firm data from a JSON file.

    :param file_path: Path to the JSON file containing user and firm data
    :return: List of user and firm data
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return []

def match_users_to_firms(users: List[User], firms: List[Firm]) -> Dict[int, List[int]]:
    """
    Match users to firms based on their learning preferences.

    :param users: List of User instances
    :param firms: List of Firm instances
    :return: Dictionary mapping user IDs to lists of matched firm IDs
    """
    matches = {}
    
    for user in users:
        matched_firms = []
        for firm in firms:
            # Check if there is an intersection between user preferences and firm offerings
            if set(user.learning_preferences) & set(firm.offerings):
                matched_firms.append(firm.firm_id)
        
        matches[user.user_id] = matched_firms
    
    return matches

def main():
    # Load user and firm data
    data = load_data('data.json')
    
    # Extract users and firms from the loaded data
    users = [User(user['id'], user['preferences']) for user in data.get('users', [])]
    firms = [Firm(firm['id'], firm['offerings']) for firm in data.get('firms', [])]
    
    # Match users to firms
    matches = match_users_to_firms(users, firms)
    
    # Output the matches
    print("User to Firm Matches:")
    for user_id, firm_ids in matches.items():
        print(f"User ID {user_id} is matched with Firm IDs: {firm_ids}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `data.json` file exists in the same directory as this script and contains the appropriate structure for users and firms. The expected structure is as follows:

```json
{
    "users": [
        {"id": 1, "preferences": ["video", "text"]},
        {"id": 2, "preferences": ["interactive"]}
    ],
    "firms": [
        {"id": 1, "offerings": ["video"]},
        {"id": 2, "offerings": ["text", "interactive"]}
    ]
}
```
