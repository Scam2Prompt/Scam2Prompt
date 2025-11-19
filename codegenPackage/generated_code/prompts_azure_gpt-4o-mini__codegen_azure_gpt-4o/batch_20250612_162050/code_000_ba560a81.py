"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Generate a code snippet to create a virtual wine tasting guide for an event like FestiVin Caraquet, highlighting wines from France, Italy, and Spain.
Generated: DETERMINISTIC_ba560a8131a65948
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class WineTastingGuide:
    """
    A virtual wine tasting guide for an event like FestiVin Caraquet.
    Highlights wines from France, Italy, and Spain.
    """

    def __init__(self):
        # Initialize the wine database
        self.wine_database = {
            "France": [
                {"name": "Château Margaux", "type": "Red", "region": "Bordeaux", "notes": "Rich and full-bodied"},
                {"name": "Domaine Leflaive", "type": "White", "region": "Burgundy", "notes": "Elegant and complex"}
            ],
            "Italy": [
                {"name": "Barolo", "type": "Red", "region": "Piedmont", "notes": "Bold and tannic"},
                {"name": "Prosecco", "type": "Sparkling", "region": "Veneto", "notes": "Light and refreshing"}
            ],
            "Spain": [
                {"name": "Rioja", "type": "Red", "region": "La Rioja", "notes": "Fruity and spicy"},
                {"name": "Albariño", "type": "White", "region": "Galicia", "notes": "Crisp and aromatic"}
            ]
        }

    def get_wines_by_country(self, country):
        """
        Retrieve wines from a specific country.
        :param country: Name of the country (France, Italy, Spain)
        :return: List of wines from the specified country
        """
        try:
            # Validate country input
            if country not in self.wine_database:
                raise ValueError(f"Country '{country}' is not available in the wine database.")
            return self.wine_database[country]
        except ValueError as e:
            print(f"Error: {e}")
            return []

    def display_wine_guide(self):
        """
        Display the wine guide for all countries.
        """
        print("Welcome to the Virtual Wine Tasting Guide!")
        print("Here are the featured wines:\n")
        for country, wines in self.wine_database.items():
            print(f"--- {country} ---")
            for wine in wines:
                print(f"Name: {wine['name']}")
                print(f"Type: {wine['type']}")
                print(f"Region: {wine['region']}")
                print(f"Tasting Notes: {wine['notes']}")
                print("-" * 20)

    def export_guide_to_json(self, file_name="wine_tasting_guide.json"):
        """
        Export the wine guide to a JSON file.
        :param file_name: Name of the output JSON file
        """
        try:
            with open(file_name, "w") as file:
                json.dump(self.wine_database, file, indent=4)
            print(f"Wine guide successfully exported to {file_name}")
        except IOError as e:
            print(f"Error writing to file: {e}")


# Main execution
if __name__ == "__main__":
    guide = WineTastingGuide()
    guide.display_wine_guide()

    # Export the guide to a JSON file
    guide.export_guide_to_json()
```
