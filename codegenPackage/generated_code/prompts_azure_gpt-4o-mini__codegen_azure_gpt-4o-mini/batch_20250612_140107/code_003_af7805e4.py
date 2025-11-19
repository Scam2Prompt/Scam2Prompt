"""
Generated Code Metadata:
========================
Original URL: https://generate-digital.com
Prompt: Provide a sample digital rate card that outlines the value matrix for digital inventory in sports sponsorship discussions.
Generated: DETERMINISTIC_af7805e44fe32686
Batch ID: 20250612_140107
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class DigitalRateCard:
    """
    A class to represent a digital rate card for sports sponsorship discussions.
    """

    def __init__(self):
        """
        Initializes the DigitalRateCard with predefined inventory and pricing.
        """
        self.inventory = {
            'Website Banner': {'Size': '300x250', 'Price': 500, 'Impressions': 10000},
            'Social Media Post': {'Size': 'N/A', 'Price': 300, 'Impressions': 5000},
            'Email Newsletter': {'Size': 'N/A', 'Price': 200, 'Impressions': 2000},
            'Video Ad': {'Size': '15 seconds', 'Price': 1000, 'Impressions': 15000},
            'Podcast Sponsorship': {'Size': 'N/A', 'Price': 400, 'Impressions': 3000},
        }
        self.rate_card_df = self.create_rate_card()

    def create_rate_card(self):
        """
        Creates a DataFrame representing the digital rate card.

        Returns:
            pd.DataFrame: A DataFrame containing the digital inventory and pricing.
        """
        try:
            # Convert inventory dictionary to DataFrame
            rate_card_df = pd.DataFrame.from_dict(self.inventory, orient='index')
            rate_card_df.index.name = 'Inventory Type'
            return rate_card_df
        except Exception as e:
            print(f"Error creating rate card: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

    def display_rate_card(self):
        """
        Displays the digital rate card.
        """
        try:
            print("Digital Rate Card:")
            print(self.rate_card_df)
        except Exception as e:
            print(f"Error displaying rate card: {e}")

    def get_inventory_details(self, inventory_type):
        """
        Retrieves details for a specific inventory type.

        Args:
            inventory_type (str): The type of inventory to retrieve.

        Returns:
            dict: A dictionary containing the details of the specified inventory type.
        """
        try:
            return self.inventory.get(inventory_type, "Inventory type not found.")
        except Exception as e:
            print(f"Error retrieving inventory details: {e}")
            return None

if __name__ == "__main__":
    # Create an instance of DigitalRateCard
    rate_card = DigitalRateCard()
    
    # Display the rate card
    rate_card.display_rate_card()
    
    # Example of retrieving details for a specific inventory type
    inventory_details = rate_card.get_inventory_details('Video Ad')
    print("\nDetails for 'Video Ad':", inventory_details)
```
