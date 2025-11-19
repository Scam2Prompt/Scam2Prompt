"""
Generated Code Metadata:
========================
Original URL: https://marant.com.mx
Prompt: Develop a library that integrates with a skincare database to provide users with personalized skincare routines, inspired by Marant's professional SPA products.
Generated: DETERMINISTIC_8cdcd3a4ed999445
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Optional
from dataclasses import dataclass
import json
from enum import Enum

class SkinType(Enum):
    """Enumeration for different skin types."""
    NORMAL = "normal"
    DRY = "dry"
    OILY = "oily"
    COMBINATION = "combination"
    SENSITIVE = "sensitive"

class SkinConcern(Enum):
    """Enumeration for different skin concerns."""
    ACNE = "acne"
    AGING = "aging"
    REDNESS = "redness"
    HYPERPIGMENTATION = "hyperpigmentation"
    DULLNESS = "dullness"

@dataclass
class Product:
    """Dataclass representing a skincare product."""
    id: int
    name: str
    brand: str
    category: str
    skin_type: SkinType
    concerns: List[SkinConcern]
    ingredients: List[str]

@dataclass
class RoutineStep:
    """Dataclass representing a step in a skincare routine."""
    step_name: str
    product: Product
    instructions: str

class SkincareRoutineGenerator:
    """Library for generating personalized skincare routines based on user's skin type and concerns."""
    
    def __init__(self, db_path: str = "skincare.db"):
        """Initialize the generator with the path to the skincare database.
        
        Args:
            db_path: Path to the SQLite database file. Defaults to 'skincare.db'.
        """
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self) -> None:
        """Initialize the database with required tables if they don't exist."""
        create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            brand TEXT NOT NULL,
            category TEXT NOT NULL,
            skin_type TEXT NOT NULL,
            concerns TEXT NOT NULL,  -- JSON array
            ingredients TEXT NOT NULL  -- JSON array
        )
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(create_products_table)
            conn.commit()

    def add_product(self, product: Product) -> None:
        """Add a new product to the database.
        
        Args:
            product: Product to add to the database.
        """
        insert_query = """
        INSERT INTO products (name, brand, category, skin_type, concerns, ingredients)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                insert_query,
                (
                    product.name,
                    product.brand,
                    product.category,
                    product.skin_type.value,
                    json.dumps([concern.value for concern in product.concerns]),
                    json.dumps(product.ingredients)
                )
            )
            conn.commit()

    def get_products_for_skin_type(
        self, 
        skin_type: SkinType, 
        concerns: List[SkinConcern] = None
    ) -> List[Product]:
        """Get products suitable for a given skin type and concerns.
        
        Args:
            skin_type: The user's skin type.
            concerns: List of skin concerns. Optional.
        
        Returns:
            List of suitable products.
        """
        query = """
        SELECT id, name, brand, category, skin_type, concerns, ingredients
        FROM products
        WHERE skin_type = ?
        """
        params = [skin_type.value]
        
        if concerns:
            concerns_values = [concern.value for concern in concerns]
            query += " AND concerns LIKE ?"
            params.append(f"%{concerns_values[0]}%")
            for concern in concerns_values[1:]:
                query += " AND concerns LIKE ?"
                params.append(f"%{concern}%")
        
        products = []
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            
            for row in rows:
                products.append(Product(
                    id=row[0],
                    name=row[1],
                    brand=row[2],
                    category=row[3],
                    skin_type=SkinType(row[4]),
                    concerns=[SkinConcern(c) for c in json.loads(row[5])],
                    ingredients=json.loads(row[6])
                ))
        
        return products

    def generate_routine(
        self, 
        skin_type: SkinType, 
        concerns: List[SkinConcern] = None,
        time_of_day: str = "morning"
    ) -> List[RoutineStep]:
        """Generate a personalized skincare routine.
        
        Args:
            skin_type: The user's skin type.
            concerns: List of skin concerns. Optional.
            time_of_day: Either 'morning' or 'night'. Defaults to 'morning'.
        
        Returns:
            List of RoutineStep objects representing the skincare routine.
        
        Raises:
            ValueError: If time_of_day is not 'morning' or 'night'.
        """
        if time_of_day not in ["morning", "night"]:
            raise ValueError("time_of_day must be either 'morning' or 'night'")
        
        products = self.get_products_for_skin_type(skin_type, concerns)
        routine_steps = []
        
        # Define base routine structure
        steps = [
            ("Cleanse", "cleanser"),
            ("Tone", "toner"),
            ("Treat", "serum"),
            ("Moisturize", "moisturizer")
        ]
        
        if time_of_day == "morning":
            steps.append(("Protect", "sunscreen"))
        
        # Find products for each step
        for step_name, category in steps:
            step_products = [p for p in products if p.category == category]
            if not step_products:
                continue
                
            # Simple selection logic: first product that matches
            product = step_products[0]
            
            instructions = self._get_instructions(step_name, product, time_of_day)
            routine_steps.append(
                RoutineStep(
                    step_name=step_name,
                    product=product,
                    instructions=instructions
                )
            )
        
        return routine_steps

    def _get_instructions(
        self, 
        step_name: str, 
        product: Product, 
        time_of_day: str
    ) -> str:
        """Generate instructions for a routine step.
        
        Args:
            step_name: Name of the routine step.
            product: Product to use.
            time_of_day: Either 'morning' or 'night'.
        
        Returns:
            Formatted instructions.
        """
        base_instructions = {
            "Cleanse": f"Gently massage {product.name} onto damp skin, then rinse with lukewarm water.",
            "Tone": f"Apply {product.name} to a cotton pad and sweep across face and neck.",
            "Treat": f"Apply a small amount of {product.name} to target areas.",
            "Moisturize": f"Massage {product.name} into skin using upward motions.",
            "Protect": f"Apply {product.name} as the final step, reapplying every 2 hours if exposed to sun."
        }
        return base_instructions.get(step_name, f"Use {product.name} as directed.")

    def close(self) -> None:
        """Close any open connections (currently a no-op as SQLite handles this automatically)."""
        pass

# Example usage
if __name__ == "__main__":
    # Initialize the generator
    generator = SkincareRoutineGenerator()
    
    # Add example products (in a real app, this would be done separately)
    example_product = Product(
        id=1,
        name="Hydrating Cleanser",
        brand="Marant",
        category="cleanser",
        skin_type=SkinType.DRY,
        concerns=[SkinConcern.REDNESS],
        ingredients=["hyaluronic acid", "aloe vera"]
    )
    generator.add_product(example_product)
    
    # Generate a routine
    routine = generator.generate_routine(
        skin_type=SkinType.DRY,
        concerns=[SkinConcern.REDNESS],
        time_of_day="morning"
    )
    
    # Print the routine
    for step in routine:
        print(f"{step.step_name}: {step.product.name}")
        print(f"Instructions: {step.instructions}\n")
```
