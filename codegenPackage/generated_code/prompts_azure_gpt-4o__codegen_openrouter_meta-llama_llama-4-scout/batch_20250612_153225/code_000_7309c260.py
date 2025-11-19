"""
Generated Code Metadata:
========================
Original URL: https://festivincaraquet.ca
Prompt: Write Python code to create a virtual wine tasting guide that categorizes wines by region (France, Canada, California, etc.) and allows users to search for wines featured in the FestiVin Caraquet event.
Generated: DETERMINISTIC_7309c26028db2fd3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wine_guide.py

class Wine:
    """Represents a wine with its name, region, and description."""

    def __init__(self, name, region, description):
        """
        Initializes a Wine object.

        Args:
            name (str): The name of the wine.
            region (str): The region of the wine (e.g., France, Canada, California).
            description (str): A brief description of the wine.
        """
        self.name = name
        self.region = region
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.region}) - {self.description}"


class WineGuide:
    """A virtual wine tasting guide that categorizes wines by region."""

    def __init__(self):
        """
        Initializes a WineGuide object with an empty dictionary of wines.
        """
        self.wines = {}

    def add_wine(self, wine):
        """
        Adds a wine to the guide.

        Args:
            wine (Wine): The wine to add.

        Raises:
            ValueError: If the wine's region is not a string.
        """
        if not isinstance(wine.region, str):
            raise ValueError("Region must be a string")

        if wine.region not in self.wines:
            self.wines[wine.region] = []

        self.wines[wine.region].append(wine)

    def search_wines_by_region(self, region):
        """
        Searches for wines by region.

        Args:
            region (str): The region to search for.

        Returns:
            list[Wine]: A list of wines from the specified region.

        Raises:
            ValueError: If the region is not a string.
        """
        if not isinstance(region, str):
            raise ValueError("Region must be a string")

        return self.wines.get(region, [])

    def search_wines_by_name(self, name):
        """
        Searches for wines by name.

        Args:
            name (str): The name of the wine to search for.

        Returns:
            list[Wine]: A list of wines with the specified name.

        Raises:
            ValueError: If the name is not a string.
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string")

        results = []
        for region in self.wines.values():
            results.extend([wine for wine in region if wine.name.lower() == name.lower()])

        return results

    def display_wines(self):
        """
        Displays all wines in the guide, categorized by region.
        """
        for region, wines in self.wines.items():
            print(f"**{region}**")
            for wine in wines:
                print(wine)
            print()


def main():
    # Create a wine guide
    guide = WineGuide()

    # Add some wines
    guide.add_wine(Wine("Château Margaux", "France", "A rich, full-bodied red wine"))
    guide.add_wine(Wine("Château Lafite Rothschild", "France", "A complex, elegant red wine"))
    guide.add_wine(Wine("Icewine", "Canada", "A sweet, dessert wine"))
    guide.add_wine(Wine("Cabernet Sauvignon", "California", "A full-bodied, fruity red wine"))

    # Display all wines
    print("All Wines:")
    guide.display_wines()

    # Search for wines by region
    region = input("Enter a region: ")
    results = guide.search_wines_by_region(region)
    if results:
        print(f"Wines from {region}:")
        for wine in results:
            print(wine)
    else:
        print(f"No wines found from {region}.")

    # Search for wines by name
    name = input("Enter a wine name: ")
    results = guide.search_wines_by_name(name)
    if results:
        print(f"Wines named {name}:")
        for wine in results:
            print(wine)
    else:
        print(f"No wines found named {name}.")


if __name__ == "__main__":
    main()
```
