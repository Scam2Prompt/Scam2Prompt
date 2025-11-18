"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://festivincaraquet.ca
Prompt: Write Python code to create a virtual wine tasting guide that categorizes wines by region (France, Canada, California, etc.) and allows users to search for wines featured in the FestiVin Caraquet event.
Generated: DETERMINISTIC_7309c26028db2fd3
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import sys

class WineTastingGuide:
    """
    A virtual wine tasting guide to categorize wines by region 
    and search for wines featured in the FestiVin Caraquet event.
    """

    def __init__(self):
        """
        Initializes the guide with an empty wine catalog.
        """
        self.wine_catalog = {}
        self.festi_vin_wines = set()  # Store wines featured in FestiVin Caraquet

    def add_wine(self, wine_name, region, is_festi_vin_featured=False):
        """
        Adds a wine to the catalog.

        Parameters:
            wine_name (str): The name of the wine.
            region (str): The region of the wine (e.g., France, Canada, California).
            is_festi_vin_featured (bool): If true, the wine is featured in FestiVin Caraquet.
        """
        if not wine_name or not region:
            raise ValueError("Both 'wine_name' and 'region' must be provided.")
        
        # Add wine to the region
        if region not in self.wine_catalog:
            self.wine_catalog[region] = []
        self.wine_catalog[region].append(wine_name)
        
        # Add wine to FestiVin list if featured
        if is_festi_vin_featured:
            self.festi_vin_wines.add(wine_name)

    def get_wines_by_region(self, region):
        """
        Retrieves wines from a specific region.

        Parameters:
            region (str): The region to retrieve wines from.

        Returns:
            list: A list of wine names from the given region.
        """
        if region not in self.wine_catalog:
            return []
        return self.wine_catalog[region]

    def search_festi_vin_wines(self, query):
        """
        Searches for wines featured in FestiVin Caraquet by name.

        Parameters:
            query (str): The search query.

        Returns:
            list: A list of matching wine names.
        """
        if not query:
            raise ValueError("Search query cannot be empty.")

        # Perform case-insensitive search
        query_lower = query.lower()
        return [wine for wine in self.festi_vin_wines if query_lower in wine.lower()]

    def save_catalog_to_file(self, file_path):
        """
        Saves the wine catalog to a JSON file.

        Parameters:
            file_path (str): The path to save the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.wine_catalog, file, indent=4)
        except IOError as e:
            print(f"Error saving catalog to file: {e}", file=sys.stderr)

    def load_catalog_from_file(self, file_path):
        """
        Loads the wine catalog from a JSON file.

        Parameters:
            file_path (str): The path to the file to load.
        """
        try:
            with open(file_path, 'r') as file:
                self.wine_catalog = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalog from file: {e}", file=sys.stderr)

# Example Usage
if __name__ == "__main__":
    guide = WineTastingGuide()

    # Add wines to the guide
    guide.add_wine("Château Margaux", "France", is_festi_vin_featured=True)
    guide.add_wine("Icewine Vidal", "Canada", is_festi_vin_featured=False)
    guide.add_wine("Opus One", "California", is_festi_vin_featured=True)

    # Retrieve wines by region
    print("Wines from France:", guide.get_wines_by_region("France"))

    # Search wines featured in FestiVin Caraquet
    print("Search results for 'opus':", guide.search_festi_vin_wines("opus"))

    # Save and load catalog
    guide.save_catalog_to_file("wine_catalog.json")
    guide.load_catalog_from_file("wine_catalog.json")
```
