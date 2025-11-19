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
import pandas as pd

class DigitalRateCard:
    """
    A class to represent a digital rate card for sports sponsorship discussions.
    
    Attributes:
    -----------
    inventory : list
        A list of digital inventory items
    rates : list
        A list of corresponding rates for each inventory item
    """
    
    def __init__(self):
        """
        Initializes a new DigitalRateCard instance with predefined inventory and rates.
        """
        self.inventory = [
            "Website Banner Ad",
            "Social Media Post",
            "Email Newsletter Feature",
            "Video Sponsorship",
            "Podcast Sponsorship",
            "Influencer Marketing"
        ]
        
        self.rates = [
            2500,  # Website Banner Ad
            1500,  # Social Media Post
            1000,  # Email Newsletter Feature
            5000,  # Video Sponsorship
            3000,  # Podcast Sponsorship
            2000   # Influencer Marketing
        ]
        
        # Ensure the lengths of inventory and rates match
        if len(self.inventory) != len(self.rates):
            raise ValueError("Inventory and rates length mismatch.")

    def generate_rate_card(self):
        """
        Generates a DataFrame representing the digital rate card.

        Returns:
        --------
        pd.DataFrame
            A DataFrame containing the digital inventory and their corresponding rates.
        """
        try:
            # Create a DataFrame from the inventory and rates
            rate_card = pd.DataFrame({
                'Digital Inventory': self.inventory,
                'Rate ($)': self.rates
            })
            return rate_card
        except Exception as e:
            raise RuntimeError("Error generating rate card.") from e

    def display_rate_card(self):
        """
        Displays the digital rate card in a user-friendly format.
        """
        try:
            rate_card = self.generate_rate_card()
            print(rate_card)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Create a DigitalRateCard instance
    rate_card = DigitalRateCard()
    
    # Display the digital rate card
    rate_card.display_rate_card()
```
