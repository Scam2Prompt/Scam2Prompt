"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aceprogaming.co.ke
Prompt: Develop a program to track partnerships between esports organizations, similar to Ace Pro Sports Technologies' collaboration with Ma Esto and Don Bashrah Gaming.
Generated: DETERMINISTIC_847bc52b29a9d20b
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime

class PartnershipTracker:
    """
    A class to track partnerships between esports organizations.
    """

    def __init__(self):
        """
        Initializes the partnership tracker with an empty list to store partnership data.
        """
        self.partnerships = []

    def add_partnership(self, organization1, organization2, partnership_date=None, details=None):
        """
        Adds a new partnership to the tracker.

        Args:
            organization1 (str): Name of the first organization.
            organization2 (str): Name of the second organization.
            partnership_date (str, optional): Date of the partnership in 'YYYY-MM-DD' format. Defaults to today's date.
            details (str, optional): Additional details about the partnership. Defaults to None.

        Raises:
            ValueError: If partnership_date is not in a valid format.
        """
        if partnership_date is None:
            # Default to today's date if no date is provided
            partnership_date = datetime.date.today().strftime('%Y-%m-%d')
        else:
            try:
                # Validate the date format
                datetime.datetime.strptime(partnership_date, '%Y-%m-%d')
            except ValueError:
                raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

        # Add partnership to the tracker
        partnership = {
            'organization1': organization1,
            'organization2': organization2,
            'partnership_date': partnership_date,
            'details': details
        }
        self.partnerships.append(partnership)

    def list_partnerships(self):
        """
        Lists all tracked partnerships.

        Returns:
            list: A list of all partnerships.
        """
        return self.partnerships

    def save_to_file(self, filename):
        """
        Saves the partnership data to a file in JSON format.

        Args:
            filename (str): Name of the file to save the data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.partnerships, file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """
        Loads partnership data from a file in JSON format.

        Args:
            filename (str): Name of the file to load the data.

        Raises:
            IOError: If the file cannot be read.
        """
        try:
            with open(filename, 'r') as file:
                self.partnerships = json.load(file)
        except IOError as e:
            print(f"Error loading from file: {e}")
        except json.JSONDecodeError:
            print("Error decoding JSON data. Please check the file format.")

if __name__ == "__main__":
    # Example usage of PartnershipTracker
    tracker = PartnershipTracker()

    # Adding partnerships
    tracker.add_partnership("Ace Pro Sports Technologies", "Ma Esto", partnership_date="2023-01-15", details="Strategic collaboration in content creation.")
    tracker.add_partnership("Ace Pro Sports Technologies", "Don Bashrah Gaming", details="Joint venture in esports tournament organization.")

    # Listing partnerships
    print("Current Partnerships:")
    for partnership in tracker.list_partnerships():
        print(partnership)

    # Saving partnerships to a file
    tracker.save_to_file("partnerships.json")
    print("Partnerships saved to 'partnerships.json'.")

    # Loading partnerships from a file
    tracker.load_from_file("partnerships.json")
    print("Partnerships loaded from 'partnerships.json':")
    for partnership in tracker.list_partnerships():
        print(partnership)
```
