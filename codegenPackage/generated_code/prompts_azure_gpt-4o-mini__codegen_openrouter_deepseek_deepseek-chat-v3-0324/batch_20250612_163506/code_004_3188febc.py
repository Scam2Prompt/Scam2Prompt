"""
Generated Code Metadata:
========================
Original URL: https://itaca.in
Prompt: Design a database schema for storing information about ceramic tiles, including attributes like size, type, and mood-enhancing features, inspired by the offerings on Itaca's site.
Generated: DETERMINISTIC_3188febc30095b8f
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Ceramic Tiles Information

```python
import sqlite3
from enum import Enum
from typing import Optional
from datetime import datetime

class TileType(Enum):
    """Enumeration of ceramic tile types"""
    PORCELAIN = 'porcelain'
    CERAMIC = 'ceramic'
    STONEWARE = 'stoneware'
    TERRA_COTTA = 'terra_cotta'
    MOSAIC = 'mosaic'
    SUBWAY = 'subway'
    QUARRY = 'quarry'
    CEMENT = 'cement'

class MoodFeature(Enum):
    """Enumeration of mood-enhancing features"""
    CALMING = 'calming'
    ENERGETIC = 'energetic'
    WARM = 'warm'
    COOL = 'cool'
    NATURAL = 'natural'
    MODERN = 'modern'
    RUSTIC = 'rustic'
    MINIMALIST = 'minimalist'

def create_database(db_name: str = 'ceramic_tiles.db') -> sqlite3.Connection:
    """
    Create and initialize the ceramic tiles database.
    
    Args:
        db_name: Name of the SQLite database file
        
    Returns:
        Connection to the created database
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Enable foreign key constraints
    cursor.execute("PRAGMA foreign_keys = ON")
    
    # Create tables
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS collections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        launch_date DATE,
        is_active BOOLEAN DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE TABLE IF NOT EXISTS tiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        collection_id INTEGER,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        description TEXT,
        length_mm REAL NOT NULL,
        width_mm REAL NOT NULL,
        thickness_mm REAL NOT NULL,
        weight_kg REAL,
        price_per_unit REAL NOT NULL,
        units_per_box INTEGER NOT NULL,
        is_water_resistant BOOLEAN DEFAULT 0,
        is_frost_resistant BOOLEAN DEFAULT 0,
        is_stain_resistant BOOLEAN DEFAULT 0,
        is_slip_resistant BOOLEAN DEFAULT 0,
        is_active BOOLEAN DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (collection_id) REFERENCES collections(id),
        CHECK (length_mm > 0 AND width_mm > 0 AND thickness_mm > 0),
        CHECK (price_per_unit > 0 AND units_per_box > 0)
    );
    
    CREATE TABLE IF NOT EXISTS tile_mood_features (
        tile_id INTEGER NOT NULL,
        mood_feature TEXT NOT NULL,
        PRIMARY KEY (tile_id, mood_feature),
        FOREIGN KEY (tile_id) REFERENCES tiles(id) ON DELETE CASCADE
    );
    
    CREATE TABLE IF NOT EXISTS colors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        hex_code TEXT NOT NULL,
        is_active BOOLEAN DEFAULT 1
    );
    
    CREATE TABLE IF NOT EXISTS tile_colors (
        tile_id INTEGER NOT NULL,
        color_id INTEGER NOT NULL,
        is_primary BOOLEAN DEFAULT 0,
        PRIMARY KEY (tile_id, color_id),
        FOREIGN KEY (tile_id) REFERENCES tiles(id) ON DELETE CASCADE,
        FOREIGN KEY (color_id) REFERENCES colors(id)
    );
    
    CREATE TABLE IF NOT EXISTS textures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        is_active BOOLEAN DEFAULT 1
    );
    
    CREATE TABLE IF NOT EXISTS tile_textures (
        tile_id INTEGER NOT NULL,
        texture_id INTEGER NOT NULL,
        PRIMARY KEY (tile_id, texture_id),
        FOREIGN KEY (tile_id) REFERENCES tiles(id) ON DELETE CASCADE,
        FOREIGN KEY (texture_id) REFERENCES textures(id)
    );
    
    CREATE TABLE IF NOT EXISTS images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tile_id INTEGER NOT NULL,
        url TEXT NOT NULL,
        alt_text TEXT,
        is_primary BOOLEAN DEFAULT 0,
        display_order INTEGER DEFAULT 0,
        FOREIGN KEY (tile_id) REFERENCES tiles(id) ON DELETE CASCADE
    );
    
    CREATE TABLE IF NOT EXISTS inventory (
        tile_id INTEGER PRIMARY KEY,
        quantity_in_stock INTEGER NOT NULL DEFAULT 0,
        quantity_reserved INTEGER NOT NULL DEFAULT 0,
        last_restock_date DATE,
        FOREIGN KEY (tile_id) REFERENCES tiles(id) ON DELETE CASCADE,
        CHECK (quantity_in_stock >= 0 AND quantity_reserved >= 0)
    );
    
    CREATE TRIGGER IF NOT EXISTS update_tile_timestamp
    AFTER UPDATE ON tiles
    FOR EACH ROW
    BEGIN
        UPDATE tiles SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
    END;
    
    CREATE TRIGGER IF NOT EXISTS update_collection_timestamp
    AFTER UPDATE ON collections
    FOR EACH ROW
    BEGIN
        UPDATE collections SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
    END;
    """)
    
    conn.commit()
    return conn

def initialize_sample_data(conn: sqlite3.Connection) -> None:
    """Initialize the database with sample data for demonstration"""
    cursor = conn.cursor()
    
    try:
        # Insert sample collections
        cursor.executemany(
            "INSERT INTO collections (name, description, launch_date) VALUES (?, ?, ?)",
            [
                ("Mediterranean Dream", "Inspired by the colors of the Mediterranean coast", "2023-03-15"),
                ("Urban Minimal", "Clean lines and contemporary aesthetics", "2023-01-10"),
                ("Nature's Palette", "Earthy tones and organic textures", "2022-11-20")
            ]
        )
        
        # Insert sample colors
        cursor.executemany(
            "INSERT INTO colors (name, hex_code) VALUES (?, ?)",
            [
                ("Ocean Blue", "#4A89DC"),
                ("Sunset Orange", "#E9573F"),
                ("Sand Beige", "#F5F7FA"),
                ("Slate Grey", "#656D78"),
                ("Forest Green", "#8CC152"),
                ("Terracotta", "#D87059"),
                ("Pure White", "#FFFFFF"),
                ("Charcoal Black", "#434A54")
            ]
        )
        
        # Insert sample textures
        cursor.executemany(
            "INSERT INTO textures (name, description) VALUES (?, ?)",
            [
                ("Smooth", "Polished, glossy finish"),
                ("Matte", "Non-reflective, flat finish"),
                ("Textured", "Tactile surface with relief patterns"),
                ("Wood Grain", "Simulates natural wood texture"),
                ("Stone", "Natural stone appearance"),
                ("Handmade", "Artisanal, irregular surface")
            ]
        )
        
        # Insert sample tiles
        cursor.execute(
            "INSERT INTO tiles (collection_id, name, type, description, length_mm, width_mm, thickness_mm, weight_kg, price_per_unit, units_per_box, is_water_resistant, is_frost_resistant) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (1, "Aegean Blue", TileType.PORCELAIN.value, "Deep blue porcelain tile inspired by the Aegean Sea", 600, 600, 9, 14.5, 32.99, 6, 1, 1)
        )
        tile1_id = cursor.lastrowid
        
        cursor.execute(
            "INSERT INTO tiles (collection_id, name, type, description, length_mm, width_mm, thickness_mm, weight_kg, price_per_unit, units_per_box, is_water_resistant, is_slip_resistant) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (2, "Concrete Slate", TileType.CEMENT.value, "Industrial-style cement tiles with minimalist appeal", 300, 600, 8, 10.2, 28.50, 8, 1, 1)
        )
        tile2_id = cursor.lastrowid
        
        cursor.execute(
            "INSERT INTO tiles (collection_id, name, type, description, length_mm, width_mm, thickness_mm, weight_kg, price_per_unit, units_per_box, is_water_resistant, is_stain_resistant) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (3, "Forest Green", TileType.STONEWARE.value, "Earthy green stoneware tiles with natural texture", 450, 450, 10, 12.8, 24.75, 8, 1, 1)
        )
        tile3_id = cursor.lastrowid
        
        # Insert mood features
        cursor.executemany(
            "INSERT INTO tile_mood_features (tile_id, mood_feature) VALUES (?, ?)",
            [
