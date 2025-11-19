"""
Generated Code Metadata:
========================
Original URL: https://mmogdv.com
Prompt: Write a Python script to create a simple scammer database using a dictionary, with functions to add, check, and report scammers, inspired by the services offered on mmogdv.com.
Generated: DETERMINISTIC_0bf784aa89764da0
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class ScammerDatabase:
    """
    A simple scammer database that stores scammer information in a dictionary.
    Provides functionality to add, check, and report scammers.
    """

    def __init__(self, database_file: str = "scammer_db.json"):
        """
        Initialize the scammer database.
        
        Args:
            database_file: Path to the JSON file to store the database.
        """
        self.database_file = database_file
        self.database: Dict[str, Dict[str, str]] = self._load_database()

    def _load_database(self) -> Dict[str, Dict[str, str]]:
        """
        Load the database from the JSON file. If the file doesn't exist,
        return an empty dictionary.
        
        Returns:
            Dictionary containing scammer data.
        """
        try:
            with open(self.database_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print("Error: Database file is corrupted. Starting with an empty database.")
            return {}

    def _save_database(self) -> None:
        """
        Save the current state of the database to the JSON file.
        """
        try:
            with open(self.database_file, 'w') as file:
                json.dump(self.database, file, indent=4)
        except IOError as e:
            print(f"Error saving database: {e}")

    def add_scammer(self, username: str, reason: str, evidence: str = "") -> bool:
        """
        Add a scammer to the database.
        
        Args:
            username: The scammer's username.
            reason: Reason for marking as a scammer.
            evidence: Optional evidence (e.g., chat logs, screenshots).
            
        Returns:
            True if scammer was added, False if already exists.
        """
        if username in self.database:
            return False
        
        self.database[username] = {
            'reason': reason,
            'evidence': evidence
        }
        self._save_database()
        return True

    def check_scammer(self, username: str) -> Optional[Dict[str, str]]:
        """
        Check if a username is in the scammer database.
        
        Args:
            username: The username to check.
            
        Returns:
            Scammer info if found, None otherwise.
        """
        return self.database.get(username)

    def get_all_scammers(self) -> List[Dict[str, str]]:
        """
        Get a list of all scammers in the database.
        
        Returns:
            List of dictionaries containing scammer info.
        """
        return [
            {'username': user, **info}
            for user, info in self.database.items()
        ]

    def remove_scammer(self, username: str) -> bool:
        """
        Remove a scammer from the database.
        
        Args:
            username: The username to remove.
            
        Returns:
            True if removed, False if not found.
        """
        if username in self.database:
            del self.database[username]
            self._save_database()
            return True
        return False

    def generate_report(self) -> str:
        """
        Generate a formatted report of all scammers.
        
        Returns:
            Formatted string report.
        """
        report = []
        for username, info in self.database.items():
            report.append(
                f"Username: {username}\n"
                f"Reason: {info['reason']}\n"
                f"Evidence: {info['evidence']}\n"
                "----------------------------"
            )
        return "\n".join(report) if report else "No scammers in database."


def main():
    """Example usage of the ScammerDatabase."""
    db = ScammerDatabase()

    # Example operations
    db.add_scammer("scammer1", "Fake item trade", "chat_log_123.txt")
    db.add_scammer("scammer2", "Account theft", "screenshot.jpg")

    # Check a scammer
    scammer_info = db.check_scammer("scammer1")
    if scammer_info:
        print("Scammer found:", scammer_info)

    # Generate report
    print("\nScammer Report:")
    print(db.generate_report())

    # Remove a scammer
    db.remove_scammer("scammer2")


if __name__ == "__main__":
    main()
```
