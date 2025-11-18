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
from typing import List, Dict, Optional

class User:
    """Class representing a user with investment preferences."""
    def __init__(self, name: str, investment_level: str, preferences: List[str]):
        self.name = name
        self.investment_level = investment_level
        self.preferences = preferences

    def to_dict(self) -> Dict:
        """Convert User object to a dictionary."""
        return {
            'name': self.name,
            'investment_level': self.investment_level,
            'preferences': self.preferences
        }

class Firm:
    """Class representing an investment education firm."""
    def __init__(self, name: str, expertise_level: str, specialties: List[str]):
        self.name = name
        self.expertise_level = expertise_level
        self.specialties = specialties

    def to_dict(self) -> Dict:
        """Convert Firm object to a dictionary."""
        return {
            'name': self.name,
            'expertise_level': self.expertise_level,
            'specialties': self.specialties
        }

class Matcher:
    """Class to match users with investment education firms based on their profiles."""
    
    def __init__(self, firms: List[Firm]):
        self.firms = firms

    def match_user(self, user: User) -> Optional[Firm]:
        """Match a user to a suitable investment education firm based on their preferences."""
        for firm in self.firms:
            if (firm.expertise_level == user.investment_level and
                any(item in firm.specialties for item in user.preferences)):
                return firm
        return None

def load_data(file_path: str) -> List[Dict]:
    """Load user or firm data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from file - {file_path}")
        return []

def save_results(results: List[Dict], file_path: str):
    """Save the matched results to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(results, file, indent=4)
    except IOError:
        print(f"Error: Could not write to file - {file_path}")

def main():
    """Main function to automate the matching process."""
    # Load users and firms from JSON files
    users_data = load_data('users.json')
    firms_data = load_data('firms.json')

    # Convert loaded data into User and Firm objects
    users = [User(**user) for user in users_data]
    firms = [Firm(**firm) for firm in firms_data]

    # Initialize the matcher
    matcher = Matcher(firms)

    # Store matched results
    matched_results = []

    # Match users to firms
    for user in users:
        matched_firm = matcher.match_user(user)
        if matched_firm:
            matched_results.append({
                'user': user.to_dict(),
                'matched_firm': matched_firm.to_dict()
            })

    # Save the matching results to a file
    save_results(matched_results, 'matched_results.json')

if __name__ == '__main__':
    main()
``` 

This code is structured to read user and firm data from JSON files, match users based on their investment level and preferences, and save the results to a new JSON file. Error handling is included for file operations and JSON decoding.
