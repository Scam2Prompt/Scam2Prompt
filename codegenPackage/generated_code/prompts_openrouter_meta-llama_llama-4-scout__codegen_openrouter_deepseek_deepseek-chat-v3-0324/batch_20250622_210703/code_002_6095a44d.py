"""
Generated Code Metadata:
========================
Original URL: https://kadma-wine.co.il
Prompt: "Generate a sample database schema for storing information about wines, including varieties, vintages, and tasting notes, inspired by Kadma Wine's offerings."
Generated: DETERMINISTIC_6095a44db60e46c3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a wine database schema
-- Inspired by Kadma Wine's offerings

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables

-- Wine varieties table
CREATE TABLE IF NOT EXISTS varieties (
    variety_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    color TEXT CHECK(color IN ('red', 'white', 'rose', 'sparkling', 'dessert')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Regions table
CREATE TABLE IF NOT EXISTS regions (
    region_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    country TEXT NOT NULL,
    description TEXT,
    climate TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Wineries table
CREATE TABLE IF NOT EXISTS wineries (
    winery_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    region_id INTEGER NOT NULL,
    founded_year INTEGER,
    description TEXT,
    website_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (region_id) REFERENCES regions(region_id) ON DELETE CASCADE
);

-- Wines table
CREATE TABLE IF NOT EXISTS wines (
    wine_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    winery_id INTEGER NOT NULL,
    variety_id INTEGER NOT NULL,
    abv REAL CHECK(abv BETWEEN 5 AND 20),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (winery_id) REFERENCES wineries(winery_id) ON DELETE CASCADE,
    FOREIGN KEY (variety_id) REFERENCES varieties(variety_id) ON DELETE CASCADE
);

-- Vintages table
CREATE TABLE IF NOT EXISTS vintages (
    vintage_id INTEGER PRIMARY KEY AUTOINCREMENT,
    wine_id INTEGER NOT NULL,
    year INTEGER NOT NULL CHECK(year BETWEEN 1000 AND 2100),
    price REAL CHECK(price > 0),
    bottle_size TEXT DEFAULT '750ml' CHECK(bottle_size IN ('375ml', '750ml', '1.5L', '3L', '6L')),
    quantity_available INTEGER DEFAULT 0 CHECK(quantity_available >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (wine_id) REFERENCES wines(wine_id) ON DELETE CASCADE,
    UNIQUE(wine_id, year)
);

-- Tasting notes table
CREATE TABLE IF NOT EXISTS tasting_notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vintage_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    appearance TEXT,
    aroma TEXT,
    palate TEXT,
    finish TEXT,
    rating INTEGER CHECK(rating BETWEEN 1 AND 100),
    drinking_window TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vintage_id) REFERENCES vintages(vintage_id) ON DELETE CASCADE
);

-- Users table
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Wine collections table
CREATE TABLE IF NOT EXISTS collections (
    collection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    is_private BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Collection items table
CREATE TABLE IF NOT EXISTS collection_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    collection_id INTEGER NOT NULL,
    vintage_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1 CHECK(quantity > 0),
    purchase_price REAL,
    purchase_date DATE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (collection_id) REFERENCES collections(collection_id) ON DELETE CASCADE,
    FOREIGN KEY (vintage_id) REFERENCES vintages(vintage_id) ON DELETE CASCADE,
    UNIQUE(collection_id, vintage_id)
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_wines_winery ON wines(winery_id);
CREATE INDEX IF NOT EXISTS idx_wines_variety ON wines(variety_id);
CREATE INDEX IF NOT EXISTS idx_vintages_wine ON vintages(wine_id);
CREATE INDEX IF NOT EXISTS idx_tasting_notes_vintage ON tasting_notes(vintage_id);
CREATE INDEX IF NOT EXISTS idx_collection_items_collection ON collection_items(collection_id);
CREATE INDEX IF NOT EXISTS idx_collection_items_vintage ON collection_items(vintage_id);

-- Create triggers for updated_at timestamps

CREATE TRIGGER IF NOT EXISTS update_varieties_timestamp
AFTER UPDATE ON varieties
BEGIN
    UPDATE varieties SET updated_at = CURRENT_TIMESTAMP WHERE variety_id = OLD.variety_id;
END;

CREATE TRIGGER IF NOT EXISTS update_regions_timestamp
AFTER UPDATE ON regions
BEGIN
    UPDATE regions SET updated_at = CURRENT_TIMESTAMP WHERE region_id = OLD.region_id;
END;

CREATE TRIGGER IF NOT EXISTS update_wineries_timestamp
AFTER UPDATE ON wineries
BEGIN
    UPDATE wineries SET updated_at = CURRENT_TIMESTAMP WHERE winery_id = OLD.winery_id;
END;

CREATE TRIGGER IF NOT EXISTS update_wines_timestamp
AFTER UPDATE ON wines
BEGIN
    UPDATE wines SET updated_at = CURRENT_TIMESTAMP WHERE wine_id = OLD.wine_id;
END;

CREATE TRIGGER IF NOT EXISTS update_vintages_timestamp
AFTER UPDATE ON vintages
BEGIN
    UPDATE vintages SET updated_at = CURRENT_TIMESTAMP WHERE vintage_id = OLD.vintage_id;
END;

CREATE TRIGGER IF NOT EXISTS update_tasting_notes_timestamp
AFTER UPDATE ON tasting_notes
BEGIN
    UPDATE tasting_notes SET updated_at = CURRENT_TIMESTAMP WHERE note_id = OLD.note_id;
END;

CREATE TRIGGER IF NOT EXISTS update_users_timestamp
AFTER UPDATE ON users
BEGIN
    UPDATE users SET updated_at = CURRENT_TIMESTAMP WHERE user_id = OLD.user_id;
END;

CREATE TRIGGER IF NOT EXISTS update_collections_timestamp
AFTER UPDATE ON collections
BEGIN
    UPDATE collections SET updated_at = CURRENT_TIMESTAMP WHERE collection_id = OLD.collection_id;
END;

CREATE TRIGGER IF NOT EXISTS update_collection_items_timestamp
AFTER UPDATE ON collection_items
BEGIN
    UPDATE collection_items SET updated_at = CURRENT_TIMESTAMP WHERE item_id = OLD.item_id;
END;
```
