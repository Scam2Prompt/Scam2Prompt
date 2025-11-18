"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync.app.allocation.claim.roclima.ro
Prompt: Write a Python program to recommend air purifiers based on room size, using product categories like "Purificatoare Aer" from RoClima.ro.
Generated: DETERMINISTIC_f98afadfb5d58e39
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class AirPurifier:
    """
    Class to represent an air purifier product.
    """
    def __init__(self, name, category, room_size_coverage):
        """
        Initialize an AirPurifier instance.

        :param name: str - The name of the air purifier
        :param category: str - The category of the air purifier
        :param room_size_coverage: float - The maximum room size (in square meters) the purifier can effectively cover
        """
        self.name = name
        self.category = category
        self.room_size_coverage = room_size_coverage

    def __repr__(self):
        return f"{self.name} ({self.category}) - Covers up to {self.room_size_coverage} m²"


class AirPurifierRecommender:
    """
    Class to recommend air purifiers based on room size.
    """
    def __init__(self, air_purifiers):
        """
        Initialize the recommender with a list of air purifiers.

        :param air_purifiers: list - List of AirPurifier instances
        """
        self.air_purifiers = air_purifiers

    def recommend(self, room_size):
        """
        Recommend air purifiers based on the given room size.

        :param room_size: float - The size of the room in square meters
        :return: list - List of recommended air purifiers
        """
        if room_size <= 0:
            raise ValueError("Room size must be a positive number.")
        
        recommendations = [
            purifier for purifier in self.air_purifiers
            if purifier.room_size_coverage >= room_size
        ]

        if not recommendations:
            raise ValueError("No air purifiers found for the specified room size.")

        return recommendations


def load_air_purifiers_from_json(file_path):
    """
    Load air purifiers from a JSON file.

    :param file_path: str - Path to the JSON file
    :return: list - List of AirPurifier instances
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            air_purifiers = [
                AirPurifier(item['name'], item['category'], item['room_size_coverage'])
                for item in data
            ]
            return air_purifiers
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the file.")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")


def main():
    """
    Main function to run the air purifier recommender program.
    """
    # Load air purifiers data from JSON file
    file_path = 'air_purifiers.json'
    try:
        air_purifiers = load_air_purifiers_from_json(file_path)
    except Exception as e:
        print(f"Error loading air purifiers: {e}")
        return

    recommender = AirPurifierRecommender(air_purifiers)

    # Example user input for room size
    room_size = float(input("Enter the room size in square meters: "))

    try:
        recommendations = recommender.recommend(room_size)
        print("Recommended air purifiers:")
        for purifier in recommendations:
            print(purifier)
    except ValueError as e:
        print(f"Recommendation error: {e}")


if __name__ == "__main__":
    main()
```

This code assumes that an input JSON file named `air_purifiers.json` exists in the same directory, containing a list of air purifiers with their respective properties. The format of the JSON should look like this:

```json
[
    {
        "name": "Purifier A",
        "category": "Purificatoare Aer",
        "room_size_coverage": 50
    },
    {
        "name": "Purifier B",
        "category": "Purificatoare Aer",
        "room_size_coverage": 30
    }
]
```
