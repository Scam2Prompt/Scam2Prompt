"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://festivincaraquet.ca
Prompt: Generate a code snippet to create a virtual wine tasting guide for an event like FestiVin Caraquet, highlighting wines from France, Italy, and Spain.
Generated: DETERMINISTIC_ba560a8131a65948
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class WineTastingGuide:
    """A class to create and manage a virtual wine tasting guide."""

    def __init__(self):
        # Initialize wine list categorized by country
        self.wines = {
            "France": [],
            "Italy": [],
            "Spain": []
        }

    def add_wine(self, country, name, description, pairing):
        """
        Adds a wine to the guide.

        :param country: A string representing the wine's country of origin (France, Italy, Spain)
        :param name: A string for the wine name
        :param description: A string describing the wine
        :param pairing: A string suggesting food pairing for the wine
        """
        if country not in self.wines:
            raise ValueError("Invalid country. Must be one of: France, Italy, Spain.")

        wine_info = {
            "name": name,
            "description": description,
            "pairing": pairing
        }
        self.wines[country].append(wine_info)

    def get_guide(self):
        """
        Returns the complete wine tasting guide as a JSON-formatted string.

        :return: JSON string representing the wine tasting guide
        """
        return json.dumps(self.wines, indent=4)

    def display_guide(self):
        """
        Prints the wine tasting guide in a readable format.
        """
        print("Virtual Wine Tasting Guide:")
        for country, wines in self.wines.items():
            print(f"\n{country}:")
            for wine in wines:
                print(f"  - Name: {wine['name']}")
                print(f"    Description: {wine['description']}")
                print(f"    Pairing: {wine['pairing']}")


# Main function to demonstrate usage
def main():
    try:
        # Create a new wine tasting guide instance
        guide = WineTastingGuide()

        # Add wines to the guide
        guide.add_wine(
            "France",
            "Châteauneuf-du-Pape",
            "A robust red wine with notes of dark fruit and spice.",
            "Pairs well with roasted meats and aged cheeses."
        )
        guide.add_wine(
            "Italy",
            "Barolo",
            "A full-bodied red wine with aromas of cherry, truffle, and rose.",
            "Complements risotto, mushroom dishes, and red meats."
        )
        guide.add_wine(
            "Spain",
            "Albariño",
            "A crisp white wine with flavors of citrus, peach, and mineral.",
            "Excellent with seafood, especially shellfish."
        )

        # Display the guide
        guide.display_guide()

        # Export the guide as JSON (if needed)
        # print(guide.get_guide())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
