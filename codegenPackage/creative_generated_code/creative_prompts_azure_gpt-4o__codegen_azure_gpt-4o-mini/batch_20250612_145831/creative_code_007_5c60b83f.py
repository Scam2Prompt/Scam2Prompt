"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soulfn.lol
Prompt: Create a program that categorizes and displays the different access tiers for Soul FN Private keys, including lifetime access, based on the Soul website's pricing structure.
Generated: DETERMINISTIC_5c60b83f0864215e
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class AccessTier:
    """Class to represent an access tier for Soul FN Private keys."""
    
    def __init__(self, name, duration, price):
        """
        Initializes an AccessTier instance.

        Args:
            name (str): The name of the access tier.
            duration (str): Duration of access (e.g., "Lifetime", "1 Year").
            price (float): Price of the access tier.
        """
        self.name = name
        self.duration = duration
        self.price = price

    def __str__(self):
        """Returns a string representation of the access tier."""
        return f"{self.name} - {self.duration}: ${self.price:.2f}"

class AccessTierManager:
    """Class to manage access tiers."""

    def __init__(self):
        """Initializes the AccessTierManager with an empty list of tiers."""
        self.tiers = []

    def add_tier(self, tier):
        """Adds an AccessTier to the manager.

        Args:
            tier (AccessTier): The access tier to add.
        """
        if not isinstance(tier, AccessTier):
            raise ValueError("Invalid tier: must be an instance of AccessTier")
        self.tiers.append(tier)

    def display_tiers(self):
        """Displays all access tiers."""
        if not self.tiers:
            print("No access tiers available.")
            return

        print("Access Tiers:")
        for tier in self.tiers:
            print(tier)

def load_access_tiers_from_json(file_path):
    """Loads access tiers from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: A list of AccessTier instances.

    Raises:
        FileNotFoundError: If the file cannot be found.
        json.JSONDecodeError: If the file contains invalid JSON.
        ValueError: If the JSON data is invalid or incomplete.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [AccessTier(tier['name'], tier['duration'], tier['price']) for tier in data]
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the file.")
    except KeyError as e:
        raise ValueError(f"Invalid data format: missing key {e}")

def main():
    """Main function to run the program."""
    tier_manager = AccessTierManager()

    # Load access tiers from a JSON file
    try:
        tiers = load_access_tiers_from_json('access_tiers.json')
        for tier in tiers:
            tier_manager.add_tier(tier)
    except Exception as e:
        print(f"Error loading access tiers: {e}")
        return

    # Display the access tiers
    tier_manager.display_tiers()

if __name__ == "__main__":
    main()
```

**Note**: Ensure that the file `access_tiers.json` exists in the same directory as this script and is formatted correctly. Here is an example of how the JSON file could look:

```json
[
    {"name": "Basic Access", "duration": "1 Year", "price": 49.99},
    {"name": "Premium Access", "duration": "Lifetime", "price": 199.99}
]
```
