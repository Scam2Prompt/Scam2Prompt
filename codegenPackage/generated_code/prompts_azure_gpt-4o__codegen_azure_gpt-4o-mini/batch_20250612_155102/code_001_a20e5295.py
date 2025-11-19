"""
Generated Code Metadata:
========================
Original URL: https://monadawards.xyz
Prompt: Create a Python function that automates the nomination process for categories such as "AISHwashers" and "Virtue Vampires," including fields for candidate examples and Discord usernames.
Generated: DETERMINISTIC_a20e529560bde604
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict

# Configure logging for better error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NominationError(Exception):
    """Custom exception for nomination errors."""
    pass

def nominate_candidates(category: str, candidates: List[Dict[str, str]]) -> None:
    """
    Automates the nomination process for specified categories.

    Args:
        category (str): The category for which candidates are being nominated.
        candidates (List[Dict[str, str]]): A list of dictionaries containing candidate examples and Discord usernames.

    Raises:
        NominationError: If the category is invalid or if there are issues with the candidates.
    """
    # Validate category
    valid_categories = ["AISHwashers", "Virtue Vampires"]
    if category not in valid_categories:
        logging.error(f"Invalid category: {category}")
        raise NominationError(f"Invalid category: {category}. Valid categories are: {valid_categories}")

    # Validate candidates
    if not candidates:
        logging.error("No candidates provided for nomination.")
        raise NominationError("No candidates provided for nomination.")

    for candidate in candidates:
        if 'example' not in candidate or 'discord_username' not in candidate:
            logging.error("Candidate must include 'example' and 'discord_username'.")
            raise NominationError("Each candidate must include 'example' and 'discord_username'.")

    # Process nominations
    nominations = {
        "category": category,
        "nominations": candidates
    }

    # Save nominations to a JSON file
    try:
        with open(f"{category}_nominations.json", "w") as file:
            json.dump(nominations, file, indent=4)
        logging.info(f"Nominations for {category} have been successfully saved.")
    except IOError as e:
        logging.error(f"Failed to write nominations to file: {e}")
        raise NominationError("Failed to save nominations due to an IOError.")

# Example usage
if __name__ == "__main__":
    try:
        nominees = [
            {"example": "Candidate 1", "discord_username": "User1#1234"},
            {"example": "Candidate 2", "discord_username": "User2#5678"}
        ]
        nominate_candidates("AISHwashers", nominees)
    except NominationError as e:
        logging.error(f"Nomination process failed: {e}")
```
