"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://generate-digital.com
Prompt: Provide a sample digital rate card that outlines the value matrix for digital inventory in sports sponsorship discussions.
Generated: DETERMINISTIC_af7805e44fe32686
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

class DigitalRateCard:
    """
    A class to represent a digital rate card for sports sponsorship discussions.
    Defines a value matrix for various digital inventory items.
    """

    def __init__(self):
        """
        Initializes the rate card with predefined digital inventory items
        and their associated values.
        """
        self.rate_card = {
            "Website Banner Ads": {
                "Homepage": 5000,
                "Event Page": 3000,
                "Team Page": 2500
            },
            "Social Media Posts": {
                "Instagram": {
                    "Story": 800,
                    "Post": 1500,
                    "Reel": 2000
                },
                "Twitter": {
                    "Tweet": 1000,
                    "Retweet": 500
                },
                "Facebook": {
                    "Post": 1200,
                    "Story": 700
                }
            },
            "Email Newsletter": {
                "Feature Placement": 2000,
                "Sponsored Banner": 1800
            },
            "Mobile App Ads": {
                "Homepage Banner": 4500,
                "Popup Ad": 3000
            },
            "Live Stream Integration": {
                "Logo Overlay": 4000,
                "Product Placement": 6000,
                "Shoutout": 3500
            }
        }

    def get_all_inventory(self):
        """
        Returns the entire rate card inventory as a dictionary.
        """
        return self.rate_card

    def get_inventory_item_value(self, category, subcategory=None, item=None):
        """
        Returns the value of a specific inventory item.

        Args:
            category (str): The main category (e.g., "Social Media Posts").
            subcategory (str, optional): The subcategory under the main category (e.g., "Instagram").
            item (str, optional): The specific inventory item (e.g., "Story").

        Returns:
            int: Value of the requested inventory item.
            
        Raises:
            KeyError: If the requested category, subcategory, or item does not exist.
        """
        try:
            if subcategory and item:
                return self.rate_card[category][subcategory][item]
            elif subcategory:
                return self.rate_card[category][subcategory]
            else:
                return self.rate_card[category]
        except KeyError as e:
            raise KeyError(f"Invalid inventory lookup: {e}")

    def update_inventory_item_value(self, category, subcategory=None, item=None, new_value=None):
        """
        Updates the value of a specific inventory item.

        Args:
            category (str): The main category of the item.
            subcategory (str, optional): The subcategory of the item.
            item (str, optional): The specific inventory item.
            new_value (int): The new value to be set.

        Raises:
            KeyError: If the requested category, subcategory, or item does not exist.
            ValueError: If the new value is not provided or invalid.
        """
        if new_value is None or not isinstance(new_value, (int, float)):
            raise ValueError("New value must be a valid number.")
        
        try:
            if subcategory and item:
                self.rate_card[category][subcategory][item] = new_value
            elif subcategory:
                self.rate_card[category][subcategory] = new_value
            else:
                self.rate_card[category] = new_value
        except KeyError as e:
            raise KeyError(f"Invalid inventory lookup for update: {e}")

    def export_rate_card_to_json(self, file_path):
        """
        Exports the rate card to a JSON file.

        Args:
            file_path (str): The path to save the JSON file.

        Raises:
            IOError: If there is an error in file writing.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.rate_card, json_file, indent=4)
        except IOError as e:
            raise IOError(f"Error while writing to file: {e}")


# Sample usage
if __name__ == "__main__":
    try:
        rate_card = DigitalRateCard()
        print("Full Rate Card:")
        print(rate_card.get_all_inventory())

        # Retrieve a specific item value
        print("\nValue of Instagram Story Ad:")
        print(rate_card.get_inventory_item_value("Social Media Posts", "Instagram", "Story"))
        
        # Update a specific item value
        print("\nUpdating Instagram Story Ad value...")
        rate_card.update_inventory_item_value("Social Media Posts", "Instagram", "Story", 1000)
        print("Updated Value:")
        print(rate_card.get_inventory_item_value("Social Media Posts", "Instagram", "Story"))
        
        # Export the rate card to a JSON file
        print("\nExporting rate card to 'digital_rate_card.json'...")
        rate_card.export_rate_card_to_json("digital_rate_card.json")
        print("Export completed.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
