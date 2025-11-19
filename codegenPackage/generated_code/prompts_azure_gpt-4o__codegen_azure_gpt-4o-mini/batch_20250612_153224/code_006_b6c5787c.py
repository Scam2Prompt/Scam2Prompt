"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Develop an algorithm to match users in the "Comunidade Mulheres Restauradas" WhatsApp group based on shared emotional challenges and goals.
Generated: DETERMINISTIC_b6c5787ce61501e4
Batch ID: 20250612_153224
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
    def __init__(self, name: str, emotional_challenges: List[str], goals: List[str]):
        """
        Initialize a User instance.

        :param name: The name of the user.
        :param emotional_challenges: A list of emotional challenges the user is facing.
        :param goals: A list of goals the user wants to achieve.
        """
        self.name = name
        self.emotional_challenges = emotional_challenges
        self.goals = goals

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the User instance to a dictionary.

        :return: A dictionary representation of the user.
        """
        return {
            "name": self.name,
            "emotional_challenges": self.emotional_challenges,
            "goals": self.goals
        }

def load_users_from_json(file_path: str) -> List[User]:
    """
    Load users from a JSON file.

    :param file_path: The path to the JSON file containing user data.
    :return: A list of User instances.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [User(**user) for user in data]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def match_users(users: List[User]) -> List[Dict[str, List[str]]]:
    """
    Match users based on shared emotional challenges and goals.

    :param users: A list of User instances.
    :return: A list of dictionaries containing matched users.
    """
    matches = []
    for i in range(len(users)):
        for j in range(i + 1, len(users)):
            shared_challenges = set(users[i].emotional_challenges) & set(users[j].emotional_challenges)
            shared_goals = set(users[i].goals) & set(users[j].goals)

            if shared_challenges or shared_goals:
                matches.append({
                    "user1": users[i].name,
                    "user2": users[j].name,
                    "shared_challenges": list(shared_challenges),
                    "shared_goals": list(shared_goals)
                })
    return matches

def save_matches_to_json(matches: List[Dict[str, List[str]]], file_path: str) -> None:
    """
    Save matched users to a JSON file.

    :param matches: A list of matched user dictionaries.
    :param file_path: The path to the JSON file where matches will be saved.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(matches, file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving matches: {e}")

def main():
    """
    Main function to load users, match them, and save the results.
    """
    users = load_users_from_json('users.json')
    if not users:
        print("No users to match.")
        return

    matches = match_users(users)
    save_matches_to_json(matches, 'matches.json')
    print(f"Matched {len(matches)} pairs of users.")

if __name__ == "__main__":
    main()
```
