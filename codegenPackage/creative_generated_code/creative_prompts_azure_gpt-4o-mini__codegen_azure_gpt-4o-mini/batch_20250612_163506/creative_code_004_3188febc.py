"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itaca.in
Prompt: Design a database schema for storing information about ceramic tiles, including attributes like size, type, and mood-enhancing features, inspired by the offerings on Itaca's site.
Generated: DETERMINISTIC_3188febc30095b8f
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about ceramic tiles

CREATE TABLE TileTypes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each tile type
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the tile type (e.g., "Porcelain", "Ceramic")
    description TEXT, -- Description of the tile type
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

CREATE TABLE TileSizes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each tile size
    width DECIMAL(5, 2) NOT NULL, -- Width of the tile in centimeters
    height DECIMAL(5, 2) NOT NULL, -- Height of the tile in centimeters
    area DECIMAL(8, 2) GENERATED ALWAYS AS (width * height) STORED, -- Automatically calculated area
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

CREATE TABLE TileMoodEnhancements (
    id SERIAL PRIMARY KEY, -- Unique identifier for each mood enhancement feature
    feature_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the mood-enhancing feature (e.g., "Calming", "Energizing")
    description TEXT, -- Description of the feature
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

CREATE TABLE Tiles (
    id SERIAL PRIMARY KEY, -- Unique identifier for each tile
    type_id INT NOT NULL, -- Foreign key referencing TileTypes
    size_id INT NOT NULL, -- Foreign key referencing TileSizes
    mood_enhancement_id INT, -- Foreign key referencing TileMoodEnhancements
    color VARCHAR(50) NOT NULL, -- Color of the tile
    texture VARCHAR(50), -- Texture of the tile (e.g., "Glossy", "Matte")
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the tile, must be non-negative
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    CONSTRAINT fk_tile_type FOREIGN KEY (type_id) REFERENCES TileTypes(id) ON DELETE CASCADE, -- Foreign key constraint for tile type
    CONSTRAINT fk_tile_size FOREIGN KEY (size_id) REFERENCES TileSizes(id) ON DELETE CASCADE, -- Foreign key constraint for tile size
    CONSTRAINT fk_tile_mood FOREIGN KEY (mood_enhancement_id) REFERENCES TileMoodEnhancements(id) ON DELETE SET NULL -- Foreign key constraint for mood enhancement
);

-- Sample queries to insert data into the tables
-- To be executed after creating the tables

-- INSERT INTO TileTypes (name, description) VALUES ('Porcelain', 'Highly durable and water-resistant ceramic.');
-- INSERT INTO TileSizes (width, height) VALUES (30.00, 30.00);
-- INSERT INTO TileMoodEnhancements (feature_name, description) VALUES ('Calming', 'Promotes relaxation and tranquility.');
-- INSERT INTO Tiles (type_id, size_id, mood_enhancement_id, color, texture, price) VALUES (1, 1, 1, 'Blue', 'Glossy', 29.99);
```
