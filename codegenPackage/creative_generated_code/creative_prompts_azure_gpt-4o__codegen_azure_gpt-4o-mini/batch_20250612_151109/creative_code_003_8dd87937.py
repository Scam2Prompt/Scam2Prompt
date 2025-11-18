"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itaca.in
Prompt: Generate a Python script to simulate the durability of vitrified tiles under different conditions (e.g., moisture, scratches, stains) based on the product descriptions on the ITACA Ceramic website.
Generated: DETERMINISTIC_8dd87937560f1ebf
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
import logging

# Set up logging for error tracking and debugging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class VitrifiedTile:
    """Class to simulate the durability of vitrified tiles under various conditions."""
    
    def __init__(self, product_name, moisture_resistance, scratch_resistance, stain_resistance):
        """
        Initialize the VitrifiedTile object with properties.

        :param product_name: Name of the tile product
        :param moisture_resistance: Boolean indicating moisture resistance (True/False)
        :param scratch_resistance: Numeric value (0-100) indicating scratch resistance
        :param stain_resistance: Numeric value (0-100) indicating stain resistance
        """
        self.product_name = product_name
        self.moisture_resistance = moisture_resistance
        self.scratch_resistance = scratch_resistance
        self.stain_resistance = stain_resistance

    def simulate_condition(self, condition):
        """
        Simulate the effect of a given condition on the tile.

        :param condition: A dictionary containing the condition parameters
        :return: Resulting durability after applying the condition
        """
        logging.info(f'Simulating condition: {condition["type"]} on {self.product_name}')
        
        try:
            if condition['type'] == 'moisture':
                return self.simulate_moisture(condition['impact'])
            elif condition['type'] == 'scratch':
                return self.simulate_scratch(condition['impact'])
            elif condition['type'] == 'stain':
                return self.simulate_stain(condition['impact'])
            else:
                raise ValueError("Unknown condition type")
        except Exception as e:
            logging.error(f'Error during simulation: {e}')
            return None

    def simulate_moisture(self, impact):
        """Simulate moisture impact on durability."""
        result = self.moisture_resistance and impact < 50
        return "Survived moisture impact" if result else "Failed moisture impact"

    def simulate_scratch(self, impact):
        """Simulate scratch impact on durability."""
        result = self.scratch_resistance >= impact
        return "Survived scratch impact" if result else "Failed scratch impact"

    def simulate_stain(self, impact):
        """Simulate stain impact on durability."""
        result = self.stain_resistance >= impact
        return "Survived stain impact" if result else "Failed stain impact"

def load_tiles_from_json(file_path):
    """
    Load tiles data from a JSON file.

    :param file_path: Path to the JSON file
    :return: List of VitrifiedTile objects
    """
    try:
        with open(file_path, 'r') as file:
            tiles_data = json.load(file)
        tiles = [VitrifiedTile(**tile) for tile in tiles_data]
        return tiles
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f'Error loading tiles data: {e}')
        return []

def main():
    """Main function to simulate durability tests on tiles."""
    # Example file path (ensure this path is valid in your environment)
    file_path = 'tiles_data.json'
    tiles = load_tiles_from_json(file_path)
    
    conditions = [
        {'type': 'moisture', 'impact': random.randint(0, 100)},
        {'type': 'scratch', 'impact': random.randint(0, 100)},
        {'type': 'stain', 'impact': random.randint(0, 100)},
    ]

    for tile in tiles:
        for condition in conditions:
            result = tile.simulate_condition(condition)
            print(f'Tile: {tile.product_name}, Condition: {condition}, Result: {result}')

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have a `tiles_data.json` file containing the necessary tile data structured as follows for the code to function correctly:

```json
[
    {
        "product_name": "Tile A",
        "moisture_resistance": true,
        "scratch_resistance": 85,
        "stain_resistance": 90
    },
    {
        "product_name": "Tile B",
        "moisture_resistance": false,
        "scratch_resistance": 70,
        "stain_resistance": 80
    }
]
```
