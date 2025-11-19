"""
Generated Code Metadata:
========================
Original URL: https://hoorainz.com
Prompt: "Design a database schema for storing information about various natural stone bracelets, their collections (e.g., The Earth Series, Statement Stones), and their respective prices and discounts."
Generated: DETERMINISTIC_44ca519e7c4cb5a7
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for natural stone bracelets

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create Collections table
CREATE TABLE IF NOT EXISTS Collections (
    collection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Stones table
CREATE TABLE IF NOT EXISTS Stones (
    stone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    properties TEXT,
    rarity TEXT CHECK(rarity IN ('common', 'uncommon', 'rare', 'very rare')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create Bracelets table
CREATE TABLE IF NOT EXISTS Bracelets (
    bracelet_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    collection_id INTEGER,
    stone_id INTEGER,
    size TEXT CHECK(size IN ('XS', 'S', 'M', 'L', 'XL')),
    material TEXT,
    weight_grams REAL,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (collection_id) REFERENCES Collections(collection_id) ON DELETE SET NULL,
    FOREIGN KEY (stone_id) REFERENCES Stones(stone_id) ON DELETE SET NULL
);

-- Create Discounts table
CREATE TABLE IF NOT EXISTS Discounts (
    discount_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bracelet_id INTEGER NOT NULL,
    discount_percent DECIMAL(5, 2) NOT NULL CHECK(discount_percent >= 0 AND discount_percent <= 100),
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bracelet_id) REFERENCES Bracelets(bracelet_id) ON DELETE CASCADE,
    CHECK (end_date > start_date)
);

-- Create Images table
CREATE TABLE IF NOT EXISTS Images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bracelet_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (bracelet_id) REFERENCES Bracelets(bracelet_id) ON DELETE CASCADE
);

-- Create trigger to update timestamps
CREATE TRIGGER IF NOT EXISTS update_collections_timestamp
AFTER UPDATE ON Collections
FOR EACH ROW
BEGIN
    UPDATE Collections SET updated_at = CURRENT_TIMESTAMP WHERE collection_id = OLD.collection_id;
END;

CREATE TRIGGER IF NOT EXISTS update_stones_timestamp
AFTER UPDATE ON Stones
FOR EACH ROW
BEGIN
    UPDATE Stones SET updated_at = CURRENT_TIMESTAMP WHERE stone_id = OLD.stone_id;
END;

CREATE TRIGGER IF NOT EXISTS update_bracelets_timestamp
AFTER UPDATE ON Bracelets
FOR EACH ROW
BEGIN
    UPDATE Bracelets SET updated_at = CURRENT_TIMESTAMP WHERE bracelet_id = OLD.bracelet_id;
END;

CREATE TRIGGER IF NOT EXISTS update_discounts_timestamp
AFTER UPDATE ON Discounts
FOR EACH ROW
BEGIN
    UPDATE Discounts SET updated_at = CURRENT_TIMESTAMP WHERE discount_id = OLD.discount_id;
END;

-- Create index for better performance on frequently queried fields
CREATE INDEX IF NOT EXISTS idx_bracelets_collection ON Bracelets(collection_id);
CREATE INDEX IF NOT EXISTS idx_bracelets_stone ON Bracelets(stone_id);
CREATE INDEX IF NOT EXISTS idx_discounts_bracelet ON Discounts(bracelet_id);
CREATE INDEX IF NOT EXISTS idx_discounts_dates ON Discounts(start_date, end_date);
CREATE INDEX IF NOT EXISTS idx_images_bracelet ON Images(bracelet_id);
```
