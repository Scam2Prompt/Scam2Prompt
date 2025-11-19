"""
Generated Code Metadata:
========================
Original URL: https://www.dessc.de
Prompt: Develop a tool for tracking and managing digital progress for small businesses in the Stuttgart region, inspired by DESSC's mission statement.
Generated: DETERMINISTIC_e90db49f80197de5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_progress_tracker.py

"""
Digital Progress Tracker for small businesses in the Stuttgart region.

Inspired by DESSC's mission statement.

Author: [Your Name]
Date: [Today's Date]
"""

import datetime
import json
import logging
from typing import Dict, List

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Business:
    def __init__(self, name: str, email: str):
        """
        Initialize a Business object.

        Args:
        - name (str): Business name
        - email (str): Business email
        """
        self.name = name
        self.email = email
        self.progress = []

    def add_progress(self, description: str, achieved_on: datetime.date):
        """
        Add a progress entry for the business.

        Args:
        - description (str): Progress description
        - achieved_on (datetime.date): Date achieved
        """
        self.progress.append({"description": description, "achieved_on": achieved_on})

    def get_progress(self) -> List[Dict]:
        """
        Get all progress entries for the business.

        Returns:
        - List[Dict]: Progress entries
        """
        return self.progress


class DigitalProgressTracker:
    def __init__(self, data_file: str):
        """
        Initialize a DigitalProgressTracker object.

        Args:
        - data_file (str): File to store business data
        """
        self.data_file = data_file
        self.businesses = self.load_businesses()

    def load_businesses(self) -> Dict[str, Business]:
        """
        Load businesses from the data file.

        Returns:
        - Dict[str, Business]: Businesses
        """
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                businesses = {}
                for name, business_data in data.items():
                    business = Business(name, business_data["email"])
                    business.progress = business_data["progress"]
                    businesses[name] = business
                return businesses
        except FileNotFoundError:
            return {}

    def save_businesses(self):
        """
        Save businesses to the data file.
        """
        data = {}
        for name, business in self.businesses.items():
            data[name] = {
                "email": business.email,
                "progress": business.progress,
            }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def add_business(self, name: str, email: str):
        """
        Add a business to the tracker.

        Args:
        - name (str): Business name
        - email (str): Business email
        """
        if name not in self.businesses:
            self.businesses[name] = Business(name, email)
            self.save_businesses()
            logger.info(f"Added business: {name}")
        else:
            logger.warning(f"Business already exists: {name}")

    def add_progress(self, name: str, description: str, achieved_on: datetime.date):
        """
        Add a progress entry for a business.

        Args:
        - name (str): Business name
        - description (str): Progress description
        - achieved_on (datetime.date): Date achieved
        """
        if name in self.businesses:
            self.businesses[name].add_progress(description, achieved_on)
            self.save_businesses()
            logger.info(f"Added progress for business: {name}")
        else:
            logger.warning(f"Business not found: {name}")

    def get_progress(self, name: str) -> List[Dict]:
        """
        Get all progress entries for a business.

        Args:
        - name (str): Business name

        Returns:
        - List[Dict]: Progress entries
        """
        if name in self.businesses:
            return self.businesses[name].get_progress()
        else:
            logger.warning(f"Business not found: {name}")
            return []


def main():
    tracker = DigitalProgressTracker("business_data.json")

    while True:
        print("\nDigital Progress Tracker")
        print("1. Add business")
        print("2. Add progress")
        print("3. Get progress")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter business name: ")
            email = input("Enter business email: ")
            tracker.add_business(name, email)
        elif choice == "2":
            name = input("Enter business name: ")
            description = input("Enter progress description: ")
            achieved_on = datetime.datetime.strptime(input("Enter date achieved (YYYY-MM-DD): "), "%Y-%m-%d").date()
            tracker.add_progress(name, description, achieved_on)
        elif choice == "3":
            name = input("Enter business name: ")
            progress = tracker.get_progress(name)
            print(json.dumps(progress, indent=4))
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
