"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tron-gifts.blogspot.com
Prompt: How can I implement a library that tracks gift trends and provides data analysis for popular gift items?
Generated: DETERMINISTIC_97e78a26c6736861
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from collections import defaultdict
from typing import Dict, List, Tuple

class GiftTracker:
    def __init__(self):
        """Initializes the GiftTracker with an empty data structure."""
        self.gift_data: defaultdict[str, List[int]] = defaultdict(list)

    def add_gift(self, gift_name: str, year: int) -> None:
        """
        Adds a gift entry to the tracker.

        Args:
            gift_name (str): The name of the gift item.
            year (int): The year the gift became popular.
        """
        if not isinstance(gift_name, str) or not isinstance(year, int):
            raise ValueError("Invalid input types for gift name or year.")
        
        self.gift_data[gift_name].append(year)

    def get_trends(self) -> Dict[str, int]:
        """
        Analyzes the gift data to find the number of times each gift was added.

        Returns:
            Dict[str, int]: A dictionary with gift names as keys and their popularity count as values.
        """
        return {gift: len(years) for gift, years in self.gift_data.items()}

    def most_popular_gifts(self) -> List[Tuple[str, int]]:
        """
        Determines the most popular gifts based on their occurrence.

        Returns:
            List[Tuple[str, int]]: A list of tuples containing gift names and their popularity counts.
        """
        trends = self.get_trends()
        sorted_trends = sorted(trends.items(), key=lambda item: item[1], reverse=True)
        return sorted_trends

    def save_to_file(self, file_path: str) -> None:
        """
        Saves the gift tracking data to a JSON file.

        Args:
            file_path (str): The path to the file where data will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.gift_data, file)
        except IOError as e:
            print(f"Error saving data to file: {e}")

    def load_from_file(self, file_path: str) -> None:
        """
        Loads gift tracking data from a JSON file.

        Args:
            file_path (str): The path to the file from which data will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                self.gift_data = defaultdict(list, json.load(file))
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data from file: {e}")

# Example usage:
if __name__ == "__main__":
    gt = GiftTracker()
    gt.add_gift("Smartphone", 2021)
    gt.add_gift("Smartphone", 2022)
    gt.add_gift("Board Game", 2021)
    
    print("Gift Trends:", gt.get_trends())
    print("Most Popular Gifts:", gt.most_popular_gifts())

    # Save and load data
    gt.save_to_file("gift_trends.json")
    gt.load_from_file("gift_trends.json")
```
