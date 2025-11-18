"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-gains.com
Prompt: Write Python code to create a system that categorizes users based on their investment learning preferences and connects them to relevant educational firms, similar to VeltrixFin's personalized matching process.
Generated: DETERMINISTIC_5edc6575f981a8b6
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
from typing import List, Dict, Union


class User:
    """Class representing a user with investment learning preferences."""
    
    def __init__(self, name: str, preferences: List[str]):
        self.name = name
        self.preferences = preferences

    def __repr__(self):
        return f"User(name={self.name}, preferences={self.preferences})"


class EducationalFirm:
    """Class representing an educational firm offering investment courses."""
    
    def __init__(self, name: str, specialties: List[str]):
        self.name = name
        self.specialties = specialties

    def __repr__(self):
        return f"EducationalFirm(name={self.name}, specialties={self.specialties})"


class MatchingSystem:
    """Class to match users with relevant educational firms based on preferences."""

    def __init__(self):
        self.users: List[User] = []
        self.firms: List[EducationalFirm] = []

    def add_user(self, user: User):
        """Adds a user to the matching system."""
        self.users.append(user)

    def add_firm(self, firm: EducationalFirm):
        """Adds an educational firm to the matching system."""
        self.firms.append(firm)

    def match_users_to_firms(self) -> Dict[str, List[str]]:
        """Matches users to firms based on their preferences.

        Returns:
            A dictionary where keys are user names and values are lists of matching firm names.
        """
        matches = {}
        for user in self.users:
            matches[user.name] = [
                firm.name for firm in self.firms if set(user.preferences) & set(firm.specialties)
            ]
        return matches

    def load_data(self, users_file: str, firms_file: str) -> None:
        """Loads users and firms from JSON files."""
        try:
            with open(users_file, 'r') as uf:
                users_data = json.load(uf)
                self.users = [User(**user) for user in users_data]

            with open(firms_file, 'r') as ff:
                firms_data = json.load(ff)
                self.firms = [EducationalFirm(**firm) for firm in firms_data]

        except FileNotFoundError as e:
            print(f"Error: {e}. Ensure the file path is correct.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}. Check your data file format.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_matches_to_file(self, matches: Dict[str, List[str]], output_file: str) -> None:
        """Saves the matching results to a JSON file."""
        try:
            with open(output_file, 'w') as of:
                json.dump(matches, of, indent=4)
        except IOError as e:
            print(f"Error writing to file: {e}. Please check permissions and file path.")


# Example usage
if __name__ == "__main__":
    # Initialize the matching system
    matching_system = MatchingSystem()

    # Load users and firms from JSON files
    matching_system.load_data('users.json', 'firms.json')

    # Match users to educational firms
    matches = matching_system.match_users_to_firms()

    # Print matches
    print(json.dumps(matches, indent=4))

    # Save matches to a file
    matching_system.save_matches_to_file(matches, 'matches.json')
``` 

Make sure to create `users.json` and `firms.json` files with appropriate data for testing this code. The JSON structure for `users.json` could look like:
```json
[
    {"name": "Alice", "preferences": ["stocks", "bonds"]},
    {"name": "Bob", "preferences": ["real estate", "cryptocurrency"]}
]
```
And for `firms.json`:
```json
[
    {"name": "InvestSmart", "specialties": ["stocks", "bonds"]},
    {"name": "CryptoEducators", "specialties": ["cryptocurrency"]},
    {"name": "RealEstatePros", "specialties": ["real estate"]}
]
```
