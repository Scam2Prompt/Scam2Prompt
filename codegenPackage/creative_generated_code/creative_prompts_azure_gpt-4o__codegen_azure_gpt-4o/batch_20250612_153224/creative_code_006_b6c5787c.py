"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabrinaalves.com
Prompt: Develop an algorithm to match users in the "Comunidade Mulheres Restauradas" WhatsApp group based on shared emotional challenges and goals.
Generated: DETERMINISTIC_b6c5787ce61501e4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Tuple

class User:
    """
    Represents a user in the WhatsApp group.
    """
    def __init__(self, user_id: int, name: str, challenges: List[str], goals: List[str]):
        self.user_id = user_id
        self.name = name
        self.challenges = set(challenges)  # Using sets for easy comparison
        self.goals = set(goals)

    def __repr__(self):
        return f"User({self.name})"

def match_users(users: List[User]) -> List[Tuple[User, User]]:
    """
    Matches users based on shared emotional challenges and goals.

    Args:
        users (List[User]): List of users in the group.

    Returns:
        List[Tuple[User, User]]: List of matched user pairs.
    """
    matches = []
    n = len(users)
    
    for i in range(n):
        for j in range(i + 1, n):
            user1, user2 = users[i], users[j]

            # Check for shared challenges and goals
            shared_challenges = user1.challenges & user2.challenges
            shared_goals = user1.goals & user2.goals

            if shared_challenges or shared_goals:
                matches.append((user1, user2))
    
    return matches

def load_users_from_file(file_path: str) -> List[User]:
    """
    Loads user data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[User]: List of User objects.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        users = []
        for user_data in data:
            user = User(
                user_id=user_data["user_id"],
                name=user_data["name"],
                challenges=user_data["challenges"],
                goals=user_data["goals"]
            )
            users.append(user)
        
        return users
    except FileNotFoundError:
        print("Error: File not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON file.")
        return []
    except KeyError as e:
        print(f"Error: Missing expected key in user data - {e}")
        return []

def save_matches_to_file(matches: List[Tuple[User, User]], file_path: str) -> None:
    """
    Saves matched user pairs to a JSON file.

    Args:
        matches (List[Tuple[User, User]]): List of matched user pairs.
        file_path (str): Path to the output JSON file.
    """
    try:
        match_data = [
            {
                "user1": {"user_id": match[0].user_id, "name": match[0].name},
                "user2": {"user_id": match[1].user_id, "name": match[1].name},
                "shared_challenges": list(match[0].challenges & match[1].challenges),
                "shared_goals": list(match[0].goals & match[1].goals)
            }
            for match in matches
        ]

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(match_data, file, ensure_ascii=False, indent=4)

        print(f"Matches successfully saved to {file_path}")
    except Exception as e:
        print(f"Error: Failed to save matches to file - {e}")

# Example usage:
if __name__ == "__main__":
    # Load users from a JSON file
    users = load_users_from_file("users.json")

    if users:
        # Find matches
        matches = match_users(users)

        # Save matches to a JSON file
        save_matches_to_file(matches, "matches.json")
```

### Example `users.json` file:
```json
[
    {
        "user_id": 1,
        "name": "Alice",
        "challenges": ["anxiety", "self-doubt"],
        "goals": ["confidence", "inner peace"]
    },
    {
        "user_id": 2,
        "name": "Maria",
        "challenges": ["stress", "self-doubt"],
        "goals": ["inner peace", "happiness"]
    },
    {
        "user_id": 3,
        "name": "Clara",
        "challenges": ["anxiety", "stress"],
        "goals": ["confidence", "happiness"]
    }
]
```
