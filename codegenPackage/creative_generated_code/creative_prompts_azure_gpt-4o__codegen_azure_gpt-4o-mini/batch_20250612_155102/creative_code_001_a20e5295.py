"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadawards.xyz
Prompt: Create a Python function that automates the nomination process for categories such as "AISHwashers" and "Virtue Vampires," including fields for candidate examples and Discord usernames.
Generated: DETERMINISTIC_a20e529560bde604
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class NominationError(Exception):
    """Custom exception for handling nomination errors."""
    pass

def save_nominations_to_file(nominations, filename='nominations.json'):
    """Saves the nominations to a JSON file.

    Args:
        nominations (dict): A dictionary containing nominations.
        filename (str): The name of the file to save nominations to.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(nominations, file, indent=4)
    except IOError as e:
        raise NominationError(f"Failed to save nominations to file: {e}")

def load_nominations_from_file(filename='nominations.json'):
    """Loads nominations from a JSON file.

    Args:
        filename (str): The name of the file to load nominations from.

    Returns:
        dict: A dictionary containing nominations.

    Raises:
        NominationError: If file cannot be read or is invalid.
    """
    if not os.path.exists(filename):
        return {}

    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        raise NominationError(f"Failed to load nominations from file: {e}")

def nominate_candidate(category, candidate_name, discord_username):
    """Nominate a candidate in a specific category.

    Args:
        category (str): The category for the nomination.
        candidate_name (str): The name of the candidate.
        discord_username (str): The Discord username of the candidate.

    Raises:
        ValueError: If any of the inputs are invalid.
    """
    if not all([category, candidate_name, discord_username]):
        raise ValueError("All fields (category, candidate name, discord username) must be provided.")

    nominations = load_nominations_from_file()
    
    if category not in nominations:
        nominations[category] = []

    nominations[category].append({
        'candidate_name': candidate_name,
        'discord_username': discord_username
    })

    save_nominations_to_file(nominations)

def main():
    """Main function to execute the nomination process."""
    try:
        print("Welcome to the Nomination Process!")
        category = input("Enter the category (e.g., AISHwashers, Virtue Vampires): ")
        candidate_name = input("Enter the candidate's name: ")
        discord_username = input("Enter the candidate's Discord username: ")

        nominate_candidate(category, candidate_name, discord_username)
        print("Nomination successful!")
    except (ValueError, NominationError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
