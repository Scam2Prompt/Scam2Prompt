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
import datetime
import json
from typing import List, Dict, Union

class PubPromotionScheduler:
    """
    A class to organize and schedule tailored promotions for pubs.
    Inspired by Lords Marketing & Promotions' expertise in delivering innovative campaigns.
    """

    def __init__(self):
        # Dictionary to store promotions, indexed by pub name
        self.promotions: Dict[str, List[Dict[str, Union[str, datetime.datetime]]]] = {}

    def add_promotion(self, pub_name: str, promotion_title: str, description: str, start_date: str, end_date: str):
        """
        Adds a promotion for a specific pub.

        :param pub_name: Name of the pub
        :param promotion_title: Title of the promotion
        :param description: Description of the promotion
        :param start_date: Start date of the promotion in 'YYYY-MM-DD' format
        :param end_date: End date of the promotion in 'YYYY-MM-DD' format
        :raises ValueError: If date format is invalid or end_date is before start_date
        """
        try:
            # Parse the start and end dates
            start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d')

            # Check if end_date is before start_date
            if end_date_obj < start_date_obj:
                raise ValueError("End date cannot be earlier than start date.")

            # Create the promotion dictionary
            promotion = {
                "title": promotion_title,
                "description": description,
                "start_date": start_date_obj,
                "end_date": end_date_obj
            }

            # Add the promotion to the pub's promotion list
            if pub_name not in self.promotions:
                self.promotions[pub_name] = []
            self.promotions[pub_name].append(promotion)

            print(f"Promotion '{promotion_title}' added successfully for pub '{pub_name}'.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_promotions(self, pub_name: str) -> List[Dict[str, Union[str, datetime.datetime]]]:
        """
        Retrieves all promotions for a specific pub.

        :param pub_name: Name of the pub
        :return: List of promotions for the pub
        """
        return self.promotions.get(pub_name, [])

    def save_promotions_to_file(self, file_name: str):
        """
        Saves all promotions to a JSON file.

        :param file_name: Name of the file to save the promotions
        """
        try:
            # Serialize promotions data to JSON
            serialized_promotions = {}
            for pub_name, promotions in self.promotions.items():
                serialized_promotions[pub_name] = [
                    {
                        "title": promotion["title"],
                        "description": promotion["description"],
                        "start_date": promotion["start_date"].strftime('%Y-%m-%d'),
                        "end_date": promotion["end_date"].strftime('%Y-%m-%d')
                    }
                    for promotion in promotions
                ]

            with open(file_name, 'w') as file:
                json.dump(serialized_promotions, file, indent=4)
            print(f"Promotions saved successfully to '{file_name}'.")

        except Exception as e:
            print(f"An error occurred while saving promotions to file: {e}")

    def load_promotions_from_file(self, file_name: str):
        """
        Loads promotions from a JSON file.

        :param file_name: Name of the file to load the promotions
        """
        try:
            with open(file_name, 'r') as file:
                serialized_promotions = json.load(file)

            for pub_name, promotions in serialized_promotions.items():
                self.promotions[pub_name] = [
                    {
                        "title": promotion["title"],
                        "description": promotion["description"],
                        "start_date": datetime.datetime.strptime(promotion["start_date"], '%Y-%m-%d'),
                        "end_date": datetime.datetime.strptime(promotion["end_date"], '%Y-%m-%d')
                    }
                    for promotion in promotions
                ]

            print(f"Promotions loaded successfully from '{file_name}'.")

        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{file_name}'.")
        except Exception as e:
            print(f"An unexpected error occurred while loading promotions: {e}")


# Example usage
if __name__ == "__main__":
    scheduler = PubPromotionScheduler()

    # Add promotions
    scheduler.add_promotion("The Red Lion", "Happy Hour", "50% off drinks", "2023-11-01", "2023-11-10")
    scheduler.add_promotion("The King's Arms", "Trivia Night", "Win prizes every Thursday!", "2023-11-02", "2023-11-30")

    # Retrieve promotions
    print("Promotions for The Red Lion:")
    print(scheduler.get_promotions("The Red Lion"))

    # Save promotions to file
    scheduler.save_promotions_to_file("promotions.json")

    # Load promotions from file
    scheduler.load_promotions_from_file("promotions.json")
```
