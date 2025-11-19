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
# wine_tasting_guide.py

class Wine:
    """Represents a wine with its characteristics."""

    def __init__(self, name, country, region, grape_variety, description):
        """
        Initializes a Wine object.

        Args:
            name (str): The name of the wine.
            country (str): The country of origin.
            region (str): The region of origin.
            grape_variety (str): The grape variety used.
            description (str): A brief description of the wine.
        """
        self.name = name
        self.country = country
        self.region = region
        self.grape_variety = grape_variety
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.country}, {self.region}) - {self.grape_variety}"


class WineTastingGuide:
    """A guide for a virtual wine tasting event."""

    def __init__(self):
        self.wines = []

    def add_wine(self, wine):
        """
        Adds a wine to the guide.

        Args:
            wine (Wine): The wine to add.
        """
        self.wines.append(wine)

    def display_wines(self):
        """Displays all wines in the guide."""
        for i, wine in enumerate(self.wines, start=1):
            print(f"\nWine {i}:")
            print(wine)
            print(f"Description: {wine.description}")

    def filter_wines_by_country(self, country):
        """
        Filters wines by country.

        Args:
            country (str): The country to filter by.

        Returns:
            list[Wine]: A list of wines from the specified country.
        """
        return [wine for wine in self.wines if wine.country.lower() == country.lower()]


def main():
    guide = WineTastingGuide()

    # Add wines from France
    guide.add_wine(Wine(
        "Château Margaux",
        "France",
        "Bordeaux",
        "Cabernet Sauvignon, Merlot, Cabernet Franc",
        "A full-bodied red wine with complex flavors of blackcurrant, blackberry, and spices."
    ))
    guide.add_wine(Wine(
        "Chablis",
        "France",
        "Burgundy",
        "Chardonnay",
        "A crisp and mineral-driven white wine with flavors of green apple and citrus."
    ))

    # Add wines from Italy
    guide.add_wine(Wine(
        "Barolo",
        "Italy",
        "Piedmont",
        "Nebbiolo",
        "A full-bodied red wine with intense flavors of dark fruit, leather, and spices."
    ))
    guide.add_wine(Wine(
        "Chianti",
        "Italy",
        "Tuscany",
        "Sangiovese",
        "A medium-bodied red wine with bright acidity and flavors of cherry, plum, and violet."
    ))

    # Add wines from Spain
    guide.add_wine(Wine(
        "Rioja Reserva",
        "Spain",
        "La Rioja",
        "Tempranillo",
        "A complex and aged red wine with flavors of dark fruit, vanilla, and tobacco."
    ))
    guide.add_wine(Wine(
        "Cava",
        "Spain",
        "Catalonia",
        "Macabeo, Parellada, Xarello",
        "A sparkling white wine with flavors of apple, citrus, and toast."
    ))

    print("Virtual Wine Tasting Guide")
    print("---------------------------")

    while True:
        print("\nOptions:")
        print("1. Display all wines")
        print("2. Filter wines by country")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            guide.display_wines()
        elif choice == "2":
            country = input("Enter a country (France, Italy, Spain): ")
            filtered_wines = guide.filter_wines_by_country(country)
            if filtered_wines:
                for wine in filtered_wines:
                    print(wine)
                    print(f"Description: {wine.description}\n")
            else:
                print("No wines found from that country.")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
