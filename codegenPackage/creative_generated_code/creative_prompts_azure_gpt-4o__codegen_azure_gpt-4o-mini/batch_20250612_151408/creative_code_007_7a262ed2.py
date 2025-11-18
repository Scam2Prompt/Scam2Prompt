"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Generate a Python program that recommends Engel cooler accessories based on user input, such as cooler size, type (hard/soft), and intended use (camping, fishing, etc.).
Generated: DETERMINISTIC_7a262ed2911c1f46
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CoolerAccessoryRecommender:
    """
    A class to recommend Engel cooler accessories based on user input.
    """

    def __init__(self):
        """
        Initializes the recommender with predefined accessory options.
        """
        self.accessories = {
            'hard': {
                'camping': ['Insulated cooler cover', 'Dry storage basket'],
                'fishing': ['Fishing rod holder', 'Fish ruler'],
                'beach': ['Sand anchor', 'Beach umbrella holder']
            },
            'soft': {
                'camping': ['Shoulder strap', 'Insulated bottle holder'],
                'fishing': ['Cooler seat cushion', 'Fishing tackle bag'],
                'beach': ['Beach mat', 'Waterproof phone case']
            }
        }

    def get_accessories(self, cooler_type, intended_use):
        """
        Returns a list of recommended accessories based on cooler type and intended use.

        Parameters:
        cooler_type (str): The type of the cooler ('hard' or 'soft').
        intended_use (str): The intended use of the cooler ('camping', 'fishing', or 'beach').

        Returns:
        list: A list of recommended accessories.
        """
        try:
            if cooler_type not in self.accessories:
                raise ValueError("Invalid cooler type. Choose 'hard' or 'soft'.")
            if intended_use not in self.accessories[cooler_type]:
                raise ValueError("Invalid intended use. Choose 'camping', 'fishing', or 'beach'.")

            return self.accessories[cooler_type][intended_use]

        except ValueError as e:
            print(f"Error: {e}")
            return []

def main():
    """
    Main function to execute the accessory recommendation process.
    """
    print("Welcome to the Engel Cooler Accessory Recommender!")
    
    # Get user input for cooler type
    cooler_type = input("Enter cooler type (hard/soft): ").strip().lower()
    
    # Get user input for intended use
    intended_use = input("Enter intended use (camping/fishing/beach): ").strip().lower()
    
    # Initialize the recommender
    recommender = CoolerAccessoryRecommender()
    
    # Get recommendations
    recommendations = recommender.get_accessories(cooler_type, intended_use)

    if recommendations:
        print(f"\nRecommended accessories for your {cooler_type} cooler used for {intended_use}:")
        for accessory in recommendations:
            print(f"- {accessory}")
    else:
        print("No accessories found for the given inputs.")

if __name__ == "__main__":
    main()
```
