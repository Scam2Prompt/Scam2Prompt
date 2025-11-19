"""
Generated Code Metadata:
========================
Original URL: https://itaca.in
Prompt: "Generate a Python code snippet to create a catalog system for ITACA CERAMIC's tile products, including slab tiles, vitrified tiles, and wall tiles with their respective sizes and features."
Generated: DETERMINISTIC_3ebc5c3660777e82
Batch ID: 20250622_204554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Tile:
    """
    A class to represent a tile product.

    Attributes:
        name (str): The name of the tile.
        tile_type (str): The type of tile (e.g., slab, vitrified, wall).
        size (str): The size of the tile.
        features (list): A list of features of the tile.
    """

    def __init__(self, name, tile_type, size, features):
        """
        Initializes a new Tile instance.

        Args:
            name (str): The name of the tile.
            tile_type (str): The type of tile.
            size (str): The size of the tile.
            features (list): A list of features of the tile.
        """
        self.name = name
        self.tile_type = tile_type
        self.size = size
        self.features = features

    def __str__(self):
        """Returns a string representation of the tile."""
        return f"{self.name} ({self.tile_type}) - Size: {self.size}, Features: {', '.join(self.features)}"


class TileCatalog:
    """
    A class to represent a catalog of tile products.

    Attributes:
        tiles (list): A list of Tile objects in the catalog.
    """

    def __init__(self):
        """Initializes an empty tile catalog."""
        self.tiles = []

    def add_tile(self, tile):
        """
        Adds a tile to the catalog.

        Args:
            tile (Tile): The tile to be added to the catalog.
        """
        if not isinstance(tile, Tile):
            raise ValueError("Only Tile instances can be added to the catalog.")
        self.tiles.append(tile)

    def display_catalog(self):
        """Displays all tiles in the catalog."""
        if not self.tiles:
            print("The catalog is empty.")
            return
        
        print("Tile Catalog:")
        for tile in self.tiles:
            print(tile)

    def find_tile_by_type(self, tile_type):
        """
        Finds and returns tiles of a specific type.

        Args:
            tile_type (str): The type of tile to search for.

        Returns:
            list: A list of tiles matching the specified type.
        """
        if not isinstance(tile_type, str):
            raise ValueError("Tile type must be a string.")
        
        matching_tiles = [tile for tile in self.tiles if tile.tile_type.lower() == tile_type.lower()]
        return matching_tiles


# Example usage
if __name__ == "__main__":
    # Create a tile catalog
    catalog = TileCatalog()

    # Create some tile instances
    slab_tile = Tile("Granite Slab", "Slab", "60x60 cm", ["Durable", "Water Resistant"])
    vitrified_tile = Tile("Vitrified Tile", "Vitrified", "30x30 cm", ["Stain Resistant", "Low Maintenance"])
    wall_tile = Tile("Ceramic Wall Tile", "Wall", "20x30 cm", ["Easy to Clean", "Variety of Designs"])

    # Add tiles to the catalog
    catalog.add_tile(slab_tile)
    catalog.add_tile(vitrified_tile)
    catalog.add_tile(wall_tile)

    # Display the catalog
    catalog.display_catalog()

    # Find tiles by type
    vitrified_tiles = catalog.find_tile_by_type("Vitrified")
    print("\nVitrified Tiles:")
    for tile in vitrified_tiles:
        print(tile)
```
