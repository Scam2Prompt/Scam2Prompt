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
import json

class DigitalRateCard:
    """
    A class to represent a digital rate card for sports sponsorship discussions.
    """

    def __init__(self):
        """
        Initializes the rate card with predefined inventory categories and their values.
        """
        self.rate_card = {
            "Social Media Posts": {
                "Facebook": {"Cost Per Post": 500, "Engagement Rate": "High"},
                "Twitter": {"Cost Per Post": 300, "Engagement Rate": "Medium"},
                "Instagram": {"Cost Per Post": 700, "Engagement Rate": "High"},
            },
            "Website Banner Ads": {
                "Homepage": {"Cost Per Month": 2000, "Impressions": "High"},
                "Article Pages": {"Cost Per Month": 1500, "Impressions": "Medium"},
            },
            "Email Campaigns": {
                "Newsletter": {"Cost Per Campaign": 1000, "Open Rate": "Medium"},
                "Promotional Emails": {"Cost Per Campaign": 1200, "Open Rate": "High"},
            },
            "Video Content": {
                "YouTube": {"Cost Per Video": 3000, "Views": "High"},
                "Instagram Reels": {"Cost Per Video": 2500, "Views": "Medium"},
            },
        }

    def get_rate_card(self):
        """
        Returns the rate card as a dictionary.
        """
        return self.rate_card

    def export_to_json(self, file_name="digital_rate_card.json"):
        """
        Exports the rate card to a JSON file.

        Args:
            file_name (str): The name of the file to export the rate card to.
        """
        try:
            with open(file_name, "w") as file:
                json.dump(self.rate_card, file, indent=4)
            print(f"Rate card successfully exported to {file_name}")
        except Exception as e:
            print(f"Error exporting rate card to JSON: {e}")

    def display_rate_card(self):
        """
        Displays the rate card in a readable format.
        """
        print("Digital Rate Card:")
        for category, items in self.rate_card.items():
            print(f"\n{category}:")
            for item, details in items.items():
                print(f"  {item}:")
                for key, value in details.items():
                    print(f"    {key}: {value}")


# Example usage
if __name__ == "__main__":
    # Create an instance of the DigitalRateCard class
    rate_card = DigitalRateCard()

    # Display the rate card
    rate_card.display_rate_card()

    # Export the rate card to a JSON file
    rate_card.export_to_json()
```
