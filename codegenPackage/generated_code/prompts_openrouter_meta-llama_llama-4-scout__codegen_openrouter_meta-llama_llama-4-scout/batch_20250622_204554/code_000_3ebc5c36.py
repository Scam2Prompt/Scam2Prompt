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
# tile_catalog.py

from enum import Enum
from typing import List, Dict

class TileType(str, Enum):
    """Enum for tile types."""
    SLAB = "slab"
    VITRIFIED = "vitrified"
    WALL = "wall"

class Tile:
    """Base class for tiles."""

    def __init__(self, name: str, tile_type: TileType, size: str, features: List[str]):
        """
        Initialize a tile.

        Args:
        - name (str): Name of the tile.
        - tile_type (TileType): Type of the tile.
        - size (str): Size of the tile.
        - features (List[str]): Features of the tile.
        """
        self.name = name
        self.tile_type = tile_type
        self.size = size
        self.features = features

    def __str__(self):
        return f"{self.name} ({self.tile_type.value}) - {self.size}"

class SlabTile(Tile):
    """Class for slab tiles."""

    def __init__(self, name: str, size: str, thickness: str, features: List[str]):
        """
        Initialize a slab tile.

        Args:
        - name (str): Name of the slab tile.
        - size (str): Size of the slab tile.
        - thickness (str): Thickness of the slab tile.
        - features (List[str]): Features of the slab tile.
        """
        super().__init__(name, TileType.SLAB, size, features)
        self.thickness = thickness

    def __str__(self):
        return super().__str__() + f", Thickness: {self.thickness}"

class VitrifiedTile(Tile):
    """Class for vitrified tiles."""

    def __init__(self, name: str, size: str, water_absorption: str, features: List[str]):
        """
        Initialize a vitrified tile.

        Args:
        - name (str): Name of the vitrified tile.
        - size (str): Size of the vitrified tile.
        - water_absorption (str): Water absorption rate of the vitrified tile.
        - features (List[str]): Features of the vitrified tile.
        """
        super().__init__(name, TileType.VITRIFIED, size, features)
        self.water_absorption = water_absorption

    def __str__(self):
        return super().__str__() + f", Water Absorption: {self.water_absorption}"

class WallTile(Tile):
    """Class for wall tiles."""

    def __init__(self, name: str, size: str, glaze_type: str, features: List[str]):
        """
        Initialize a wall tile.

        Args:
        - name (str): Name of the wall tile.
        - size (str): Size of the wall tile.
        - glaze_type (str): Type of glaze used for the wall tile.
        - features (List[str]): Features of the wall tile.
        """
        super().__init__(name, TileType.WALL, size, features)
        self.glaze_type = glaze_type

    def __str__(self):
        return super().__str__() + f", Glaze Type: {self.glaze_type}"

class TileCatalog:
    """Class for tile catalog."""

    def __init__(self):
        self.tiles: Dict[str, Tile] = {}

    def add_tile(self, tile: Tile):
        """
        Add a tile to the catalog.

        Args:
        - tile (Tile): Tile to add.
        """
        self.tiles[tile.name] = tile

    def remove_tile(self, name: str):
        """
        Remove a tile from the catalog.

        Args:
        - name (str): Name of the tile to remove.

        Raises:
        - KeyError: If the tile is not found in the catalog.
        """
        if name not in self.tiles:
            raise KeyError(f"Tile '{name}' not found in catalog")
        del self.tiles[name]

    def get_tile(self, name: str) -> Tile:
        """
        Get a tile from the catalog.

        Args:
        - name (str): Name of the tile to get.

        Returns:
        - Tile: The tile with the given name.

        Raises:
        - KeyError: If the tile is not found in the catalog.
        """
        try:
            return self.tiles[name]
        except KeyError:
            raise KeyError(f"Tile '{name}' not found in catalog")

def main():
    catalog = TileCatalog()

    slab_tile = SlabTile("Slab Tile 1", "120x240", "10mm", ["Polished", "Rectified"])
    vitrified_tile = VitrifiedTile("Vitrified Tile 1", "600x600", "< 0.5%", ["Glazed", "Anti-Slip"])
    wall_tile = WallTile("Wall Tile 1", "300x600", "High-Gloss", ["Glazed", "Water-Resistant"])

    catalog.add_tile(slab_tile)
    catalog.add_tile(vitrified_tile)
    catalog.add_tile(wall_tile)

    print("Tile Catalog:")
    for tile in catalog.tiles.values():
        print(tile)

    try:
        catalog.remove_tile("Slab Tile 1")
        print("\nAfter removing Slab Tile 1:")
        for tile in catalog.tiles.values():
            print(tile)
    except KeyError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
