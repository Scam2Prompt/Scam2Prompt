"""
Generated Code Metadata:
========================
Original URL: https://oromaticas.com
Prompt: "Write a Python script to manage an inventory of medicinal plants, including tracking plant species, quantities, and uses, inspired by Oromaticas' agroecological approach."
Generated: DETERMINISTIC_ecd5ac87d04f56bc
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class MedicinalPlant:
    """
    Represents a medicinal plant in the inventory.
    """
    id: int
    species: str
    quantity: int
    uses: str
    growing_conditions: str
    harvest_time: str


class InventoryManager:
    """
    Manages the medicinal plant inventory using SQLite database.
    """
    
    def __init__(self, db_name: str = "medicinal_plants.db"):
        """
        Initialize the inventory manager with a database connection.
        
        Args:
            db_name: Name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self._create_table()
    
    def _create_table(self) -> None:
        """
        Create the plants table if it doesn't exist.
        """
        query = """
        CREATE TABLE IF NOT EXISTS plants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            species TEXT NOT NULL UNIQUE,
            quantity INTEGER NOT NULL CHECK(quantity >= 0),
            uses TEXT NOT NULL,
            growing_conditions TEXT NOT NULL,
            harvest_time TEXT NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()
    
    def add_plant(self, species: str, quantity: int, uses: str, 
                  growing_conditions: str, harvest_time: str) -> None:
        """
        Add a new plant to the inventory.
        
        Args:
            species: Name of the plant species.
            quantity: Available quantity.
            uses: Medicinal uses of the plant.
            growing_conditions: Preferred growing conditions.
            harvest_time: Optimal harvest time.
            
        Raises:
            ValueError: If quantity is negative or required fields are empty.
            sqlite3.IntegrityError: If species already exists.
        """
        if not all([species, uses, growing_conditions, harvest_time]):
            raise ValueError("All fields must be non-empty")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        query = """
        INSERT INTO plants (species, quantity, uses, growing_conditions, harvest_time)
        VALUES (?, ?, ?, ?, ?)
        """
        try:
            self.conn.execute(query, (species, quantity, uses, growing_conditions, harvest_time))
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            raise sqlite3.IntegrityError(f"Species '{species}' already exists") from e
    
    def update_plant(self, plant_id: int, **kwargs) -> None:
        """
        Update plant information.
        
        Args:
            plant_id: ID of the plant to update.
            **kwargs: Fields to update (species, quantity, uses, growing_conditions, harvest_time).
            
        Raises:
            ValueError: If invalid fields are provided or quantity is negative.
        """
        valid_fields = {'species', 'quantity', 'uses', 'growing_conditions', 'harvest_time'}
        invalid_fields = set(kwargs.keys()) - valid_fields
        if invalid_fields:
            raise ValueError(f"Invalid fields: {invalid_fields}")
        
        if 'quantity' in kwargs and kwargs['quantity'] < 0:
            raise ValueError("Quantity cannot be negative")
        
        if not kwargs:
            return
        
        set_clause = ", ".join(f"{k} = ?" for k in kwargs.keys())
        query = f"UPDATE plants SET {set_clause} WHERE id = ?"
        params = tuple(kwargs.values()) + (plant_id,)
        
        self.conn.execute(query, params)
        self.conn.commit()
    
    def delete_plant(self, plant_id: int) -> None:
        """
        Delete a plant from the inventory.
        
        Args:
            plant_id: ID of the plant to delete.
        """
        query = "DELETE FROM plants WHERE id = ?"
        self.conn.execute(query, (plant_id,))
        self.conn.commit()
    
    def get_plant(self, plant_id: int) -> Optional[MedicinalPlant]:
        """
        Retrieve a plant by its ID.
        
        Args:
            plant_id: ID of the plant to retrieve.
            
        Returns:
            MedicinalPlant object if found, None otherwise.
        """
        query = "SELECT * FROM plants WHERE id = ?"
        cursor = self.conn.execute(query, (plant_id,))
        row = cursor.fetchone()
        if row:
            return MedicinalPlant(*row)
        return None
    
    def get_all_plants(self) -> List[MedicinalPlant]:
        """
        Retrieve all plants in the inventory.
        
        Returns:
            List of MedicinalPlant objects.
        """
        query = "SELECT * FROM plants ORDER BY species"
        cursor = self.conn.execute(query)
        return [MedicinalPlant(*row) for row in cursor.fetchall()]
    
    def search_plants(self, search_term: str) -> List[MedicinalPlant]:
        """
        Search plants by species or uses.
        
        Args:
            search_term: Term to search for in species or uses fields.
            
        Returns:
            List of matching MedicinalPlant objects.
        """
        query = """
        SELECT * FROM plants 
        WHERE species LIKE ? OR uses LIKE ?
        ORDER BY species
        """
        search_pattern = f"%{search_term}%"
        cursor = self.conn.execute(query, (search_pattern, search_pattern))
        return [MedicinalPlant(*row) for row in cursor.fetchall()]
    
    def adjust_quantity(self, plant_id: int, amount: int) -> None:
        """
        Adjust the quantity of a plant.
        
        Args:
            plant_id: ID of the plant to adjust.
            amount: Amount to add (positive) or subtract (negative).
            
        Raises:
            ValueError: If resulting quantity would be negative.
        """
        plant = self.get_plant(plant_id)
        if not plant:
            raise ValueError("Plant not found")
        
        new_quantity = plant.quantity + amount
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        
        self.update_plant(plant_id, quantity=new_quantity)
    
    def get_low_stock_plants(self, threshold: int = 5) -> List[MedicinalPlant]:
        """
        Get plants with quantities below the specified threshold.
        
        Args:
            threshold: Quantity threshold (default: 5).
            
        Returns:
            List of MedicinalPlant objects with low stock.
        """
        query = "SELECT * FROM plants WHERE quantity < ? ORDER BY quantity"
        cursor = self.conn.execute(query, (threshold,))
        return [MedicinalPlant(*row) for row in cursor.fetchall()]
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - close the connection."""
        self.close()


# Example usage
if __name__ == "__main__":
    with InventoryManager() as manager:
        # Add some sample plants
        try:
            manager.add_plant(
                species="Aloe Vera",
                quantity=10,
                uses="Skin treatment, digestion aid",
                growing_conditions="Well-drained soil, sunny location",
                harvest_time="Year-round"
            )
            
            manager.add_plant(
                species="Chamomile",
                quantity=15,
                uses="Calming tea, anti-inflammatory",
                growing_conditions="Full sun to partial shade",
                harvest_time="Summer"
            )
        except sqlite3.IntegrityError as e:
            print(f"Error adding plant: {e}")
        
        # List all plants
        print("Current inventory:")
        for plant in manager.get_all_plants():
            print(f"{plant.species}: {plant.quantity} available")
        
        # Search for plants
        print("\nPlants with 'tea' in uses:")
        for plant in manager.search_plants("tea"):
            print(f"{plant.species}: {plant.uses}")
        
        # Update a plant
        manager.update_plant(1, quantity=8)
        
        # Get low stock plants
        print("\nLow stock plants:")
        for plant in manager.get_low_stock_plants(10):
            print(f"{plant.species}: only {plant.quantity} left")
```
