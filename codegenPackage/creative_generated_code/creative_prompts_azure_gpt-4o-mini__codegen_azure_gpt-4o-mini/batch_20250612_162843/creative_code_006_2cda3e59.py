"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anywhere-adventure.com
Prompt: Write a script to automate the process of generating quotes for tailored travel packages, specifically for adventure sports and wildlife safaris in Kenya.
Generated: DETERMINISTIC_2cda3e59ad14f913
Batch ID: 20250612_162843
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TravelPackage:
    def __init__(self, package_type, duration, activities, price):
        """
        Initializes a travel package instance.

        :param package_type: Type of the travel package (e.g., 'Adventure', 'Wildlife Safari')
        :param duration: Duration of the package in days
        :param activities: List of activities included in the package
        :param price: Total price of the package
        """
        self.package_type = package_type
        self.duration = duration
        self.activities = activities
        self.price = price

    def to_dict(self):
        """Converts the travel package instance to a dictionary for easy JSON serialization."""
        return {
            'package_type': self.package_type,
            'duration': self.duration,
            'activities': self.activities,
            'price': self.price
        }

class TravelPackageGenerator:
    def __init__(self):
        self.packages = [
            TravelPackage('Adventure', 7, ['Rock Climbing', 'White Water Rafting', 'Sky Diving'], 1500),
            TravelPackage('Wildlife Safari', 5, ['Game Drive', 'Bird Watching', 'Nature Walk'], 1200),
            TravelPackage('Combined Adventure & Safari', 10, ['Bungee Jumping', 'Game Drive', 'Snorkeling'], 2200),
        ]

    def generate_quote(self):
        """
        Generates a random travel package quote.

        :return: JSON string containing the selected travel package quote
        """
        try:
            package = random.choice(self.packages)
            quote = json.dumps(package.to_dict(), indent=4)
            logging.info("Quote successfully generated.")
            return quote
        except Exception as e:
            logging.error("Failed to generate quote: %s", str(e))
            raise

def main():
    """Main function to execute the travel package quote generation."""
    try:
        generator = TravelPackageGenerator()
        quote = generator.generate_quote()
        print("Generated Travel Package Quote:\n", quote)
    except Exception as e:
        print("An error occurred while generating the travel package quote:", str(e))

if __name__ == '__main__':
    main()
```
