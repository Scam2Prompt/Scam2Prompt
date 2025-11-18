"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lords.marketing
Prompt: Create a Python program that organizes and schedules tailored promotions for pubs, inspired by Lords Marketing & Promotions' expertise in delivering innovative campaigns.
Generated: DETERMINISTIC_8e9aa33df05bf754
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
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Promotion:
    """
    Class to represent a promotional campaign for a pub.
    """
    def __init__(self, name: str, start_date: str, end_date: str, details: str):
        self.name = name
        self.start_date = self.parse_date(start_date)
        self.end_date = self.parse_date(end_date)
        self.details = details

    @staticmethod
    def parse_date(date_str: str) -> datetime:
        """
        Parse a date string into a datetime object.
        :param date_str: The date string in 'YYYY-MM-DD' format.
        :return: datetime object.
        """
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format is YYYY-MM-DD.") from e

    def is_active(self) -> bool:
        """
        Check if the promotion is currently active based on the current date.
        :return: True if active, False otherwise.
        """
        today = datetime.now()
        return self.start_date <= today <= self.end_date

class PromotionScheduler:
    """
    Class to manage scheduling and organizing promotions.
    """
    def __init__(self):
        self.promotions: List[Promotion] = []

    def add_promotion(self, promotion: Promotion) -> None:
        """
        Add a new promotion to the scheduler.
        :param promotion: An instance of the Promotion class to be added.
        """
        self.promotions.append(promotion)

    def get_active_promotions(self) -> List[Dict]:
        """
        Retrieve a list of currently active promotions.
        :return: List of active promotions in dictionary format.
        """
        return [vars(promotion) for promotion in self.promotions if promotion.is_active()]

    def load_promotions_from_file(self, file_path: str) -> None:
        """
        Load promotions from a JSON file.
        :param file_path: Path to the JSON file containing promotions.
        """
        try:
            with open(file_path, 'r') as file:
                promotions_data = json.load(file)
                for promo in promotions_data:
                    promotion = Promotion(
                        name=promo['name'],
                        start_date=promo['start_date'],
                        end_date=promo['end_date'],
                        details=promo['details']
                    )
                    self.add_promotion(promotion)
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_promotions_to_file(self, file_path: str) -> None:
        """
        Save current promotions to a JSON file.
        :param file_path: Path to the JSON file to save promotions.
        """
        try:
            with open(file_path, 'w') as file:
                promotions_data = [vars(promotion) for promotion in self.promotions]
                json.dump(promotions_data, file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving promotions: {e}")

if __name__ == "__main__":
    # Create a promotion scheduler instance
    scheduler = PromotionScheduler()

    # Load promotions from a JSON file
    scheduler.load_promotions_from_file('promotions.json')

    # Display active promotions
    active_promotions = scheduler.get_active_promotions()
    print("Active Promotions:")
    for promo in active_promotions:
        print(f"Name: {promo['name']}, Start: {promo['start_date']}, End: {promo['end_date']}, Details: {promo['details']}")

    # Optionally, save the current promotions to a file
    scheduler.save_promotions_to_file('current_promotions.json')
```
