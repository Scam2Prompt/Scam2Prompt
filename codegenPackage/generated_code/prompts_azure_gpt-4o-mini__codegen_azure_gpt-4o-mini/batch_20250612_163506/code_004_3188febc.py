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

```sql
-- Database schema for storing information about ceramic tiles

CREATE TABLE TileTypes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each tile type
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the tile type (e.g., porcelain, ceramic)
    description TEXT, -- Description of the tile type
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

CREATE TABLE TileSizes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each tile size
    width DECIMAL(5, 2) NOT NULL, -- Width of the tile in centimeters
    height DECIMAL(5, 2) NOT NULL, -- Height of the tile in centimeters
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

CREATE TABLE MoodEnhancingFeatures (
    id SERIAL PRIMARY KEY, -- Unique identifier for each feature
    feature_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the mood-enhancing feature (e.g., color, texture)
    description TEXT, -- Description of the feature
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

CREATE TABLE CeramicTiles (
    id SERIAL PRIMARY KEY, -- Unique identifier for each ceramic tile
    type_id INT NOT NULL, -- Foreign key referencing TileTypes
    size_id INT NOT NULL, -- Foreign key referencing TileSizes
    mood_feature_id INT, -- Foreign key referencing MoodEnhancingFeatures (optional)
    color VARCHAR(50), -- Color of the tile
    price DECIMAL(10, 2) NOT NULL, -- Price of the tile
    stock_quantity INT DEFAULT 0, -- Quantity available in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (type_id) REFERENCES TileTypes(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (size_id) REFERENCES TileSizes(id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (mood_feature_id) REFERENCES MoodEnhancingFeatures(id) ON DELETE SET NULL -- Optional feature
);

-- Indexes for performance optimization
CREATE INDEX idx_tile_type ON CeramicTiles(type_id);
CREATE INDEX idx_tile_size ON CeramicTiles(size_id);
CREATE INDEX idx_mood_feature ON CeramicTiles(mood_feature_id);
```
