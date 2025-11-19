"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Generate a Python program that recommends Engel cooler accessories based on user input, such as cooler size, type (hard/soft), and intended use (camping, fishing, etc.).
Generated: DETERMINISTIC_7a262ed2911c1f46
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class EngelCoolerAccessoryRecommender:
    def __init__(self):
        # Load accessory recommendations from a JSON file
        self.accessories = self.load_accessories()

    def load_accessories(self):
        """Load accessory recommendations from a JSON file."""
        try:
            with open('accessories.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: accessories.json file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from accessories.json.")
            return {}

    def recommend_accessories(self, cooler_size, cooler_type, intended_use):
        """
        Recommend accessories based on cooler size, type, and intended use.

        :param cooler_size: Size of the cooler (e.g., 'small', 'medium', 'large')
        :param cooler_type: Type of cooler ('hard' or 'soft')
        :param intended_use: Intended use of the cooler (e.g., 'camping', 'fishing')
        :return: List of recommended accessories
        """
        recommendations = []

        # Check for valid cooler type
        if cooler_type not in ['hard', 'soft']:
            raise ValueError("Invalid cooler type. Must be 'hard' or 'soft'.")

        # Gather recommendations based on user input
        for accessory in self.accessories.get(cooler_size, {}).get(cooler_type, {}).get(intended_use, []):
            recommendations.append(accessory)

        return recommendations

def main():
    recommender = EngelCoolerAccessoryRecommender()

    # User input
    try:
        cooler_size = input("Enter cooler size (small, medium, large): ").strip().lower()
        cooler_type = input("Enter cooler type (hard, soft): ").strip().lower()
        intended_use = input("Enter intended use (camping, fishing, etc.): ").strip().lower()

        # Get recommendations
        recommended_accessories = recommender.recommend_accessories(cooler_size, cooler_type, intended_use)

        # Display recommendations
        if recommended_accessories:
            print("\nRecommended Accessories:")
            for accessory in recommended_accessories:
                print(f"- {accessory}")
        else:
            print("No accessories found for the given criteria.")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have a `accessories.json` file structured appropriately for this code to work. The JSON structure should look something like this:

```json
{
    "small": {
        "hard": {
            "camping": ["Small Hard Cooler Bag", "Insulated Water Bottle"],
            "fishing": ["Fishing Rod Holder", "Bait Bucket"]
        },
        "soft": {
            "camping": ["Soft Cooler Backpack", "Portable Grill"],
            "fishing": ["Fishing Tackle Box", "Fish Measuring Board"]
        }
    },
    "medium": {
        "hard": {
            "camping": ["Medium Hard Cooler Bag", "Camping Utensil Set"],
            "fishing": ["Fishing Net", "Cooler Seat Cushion"]
        },
        "soft": {
            "camping": ["Soft Cooler Tote", "Portable Camp Stove"],
            "fishing": ["Fishing Line Spooler", "Fish Finder"]
        }
    },
    "large": {
        "hard": {
            "camping": ["Large Hard Cooler", "Camping Table"],
            "fishing": ["Large Bait Bucket", "Fishing Chair"]
        },
        "soft": {
            "camping": ["Large Soft Cooler", "Portable Folding Chair"],
            "fishing": ["Fishing Rod Holder", "Fish Cleaning Station"]
        }
    }
}
```
