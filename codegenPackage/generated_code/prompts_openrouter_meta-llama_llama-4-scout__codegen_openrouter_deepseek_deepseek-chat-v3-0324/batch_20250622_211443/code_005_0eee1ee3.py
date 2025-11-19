"""
Generated Code Metadata:
========================
Original URL: https://alphaonsol.net
Prompt: Design a simple database schema to store information about cooking oil producers, their products, and the regions they source from, inspired by Authentic Oil's approach to reliable sourcing and sustainability.
Generated: DETERMINISTIC_0eee1ee383bdab15
Batch ID: 20250622_211443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for cooking oil producers, products, and sourcing regions

import sqlite3
from typing import Optional, List
from dataclasses import dataclass

@dataclass
class Producer:
    id: int
    name: str
    location: str
    sustainability_rating: float
    certification: Optional[str] = None
    year_founded: Optional[int] = None

@dataclass
class Product:
    id: int
    producer_id: int
    name: str
    oil_type: str
    extraction_method: str
    organic: bool
    price_per_liter: float

@dataclass
class SourcingRegion:
    id: int
    producer_id: int
    region_name: str
    country: str
    sustainable_practices: str
    hectares: float

class OilDatabase:
    def __init__(self, db_path: str = "oil_database.db"):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_path)
        self._create_tables()

    def _create_tables(self):
        """Create the necessary tables in the database."""
        cursor = self.conn.cursor()

        # Producers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS producers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            sustainability_rating REAL CHECK(sustainability_rating >= 0 AND sustainability_rating <= 5),
            certification TEXT,
            year_founded INTEGER
        )
        """)

        # Products table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producer_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            oil_type TEXT NOT NULL,
            extraction_method TEXT NOT NULL,
            organic BOOLEAN NOT NULL CHECK (organic IN (0, 1)),
            price_per_liter REAL NOT NULL CHECK(price_per_liter > 0),
            FOREIGN KEY (producer_id) REFERENCES producers(id) ON DELETE CASCADE
        )
        """)

        # Sourcing regions table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sourcing_regions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producer_id INTEGER NOT NULL,
            region_name TEXT NOT NULL,
            country TEXT NOT NULL,
            sustainable_practices TEXT NOT NULL,
            hectares REAL NOT NULL CHECK(hectares > 0),
            FOREIGN KEY (producer_id) REFERENCES producers(id) ON DELETE CASCADE
        )
        """)

        self.conn.commit()

    def add_producer(self, producer: Producer) -> int:
        """Add a new producer to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO producers (name, location, sustainability_rating, certification, year_founded)
            VALUES (?, ?, ?, ?, ?)
            """, (producer.name, producer.location, producer.sustainability_rating, 
                  producer.certification, producer.year_founded))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error adding producer: {str(e)}")

    def add_product(self, product: Product) -> int:
        """Add a new product to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO products (producer_id, name, oil_type, extraction_method, organic, price_per_liter)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (product.producer_id, product.name, product.oil_type, 
                  product.extraction_method, int(product.organic), product.price_per_liter))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error adding product: {str(e)}")

    def add_sourcing_region(self, region: SourcingRegion) -> int:
        """Add a new sourcing region to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO sourcing_regions (producer_id, region_name, country, sustainable_practices, hectares)
            VALUES (?, ?, ?, ?, ?)
            """, (region.producer_id, region.region_name, region.country, 
                  region.sustainable_practices, region.hectares))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            self.conn.rollback()
            raise Exception(f"Error adding sourcing region: {str(e)}")

    def get_producer_by_id(self, producer_id: int) -> Optional[Producer]:
        """Retrieve a producer by their ID."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM producers WHERE id = ?", (producer_id,))
            row = cursor.fetchone()
            if row:
                return Producer(*row)
            return None
        except sqlite3.Error as e:
            raise Exception(f"Error retrieving producer: {str(e)}")

    def get_products_by_producer(self, producer_id: int) -> List[Product]:
        """Retrieve all products for a given producer."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM products WHERE producer_id = ?", (producer_id,))
            return [Product(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Error retrieving products: {str(e)}")

    def get_sourcing_regions_by_producer(self, producer_id: int) -> List[SourcingRegion]:
        """Retrieve all sourcing regions for a given producer."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM sourcing_regions WHERE producer_id = ?", (producer_id,))
            return [SourcingRegion(*row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise Exception(f"Error retrieving sourcing regions: {str(e)}")

    def close(self):
        """Close the database connection."""
        self.conn.close()

    def __enter__(self):
        """Support context manager protocol."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support context manager protocol."""
        self.close()
```
