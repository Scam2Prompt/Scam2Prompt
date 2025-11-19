"""
Generated Code Metadata:
========================
Original URL: https://rawcakesandcandy.ro
Prompt: "Design a database schema to store information about raw vegan desserts, including cakes, pastries, and their ingredients, as seen on the Raw Cakes And Candy website."
Generated: DETERMINISTIC_523e60bab3f4ff9a
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for raw vegan desserts
-- This schema is designed to store information about raw vegan desserts, 
-- including cakes, pastries, and their ingredients.

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create tables
BEGIN TRANSACTION;

-- Table for storing dessert categories
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Table for storing ingredients
CREATE TABLE IF NOT EXISTS ingredients (
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    is_organic BOOLEAN DEFAULT 0,
    is_gluten_free BOOLEAN DEFAULT 0,
    is_nut_free BOOLEAN DEFAULT 0,
    description TEXT
);

-- Table for storing desserts
CREATE TABLE IF NOT EXISTS desserts (
    dessert_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    description TEXT,
    preparation_time INTEGER, -- in minutes
    serving_size TEXT,
    is_available BOOLEAN DEFAULT 1,
    price DECIMAL(10, 2),
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Junction table for dessert-ingredient relationship (many-to-many)
CREATE TABLE IF NOT EXISTS dessert_ingredients (
    dessert_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    quantity TEXT, -- e.g., "1 cup", "200g"
    is_main_ingredient BOOLEAN DEFAULT 0,
    PRIMARY KEY (dessert_id, ingredient_id),
    FOREIGN KEY (dessert_id) REFERENCES desserts(dessert_id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id) ON DELETE CASCADE
);

-- Table for storing nutritional information per dessert
CREATE TABLE IF NOT EXISTS nutrition_facts (
    nutrition_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dessert_id INTEGER NOT NULL UNIQUE,
    calories INTEGER,
    total_fat DECIMAL(5, 1), -- in grams
    saturated_fat DECIMAL(5, 1),
    trans_fat DECIMAL(5, 1),
    cholesterol INTEGER, -- in milligrams
    sodium INTEGER, -- in milligrams
    total_carbohydrates DECIMAL(5, 1), -- in grams
    dietary_fiber DECIMAL(5, 1),
    sugars DECIMAL(5, 1),
    protein DECIMAL(5, 1),
    FOREIGN KEY (dessert_id) REFERENCES desserts(dessert_id) ON DELETE CASCADE
);

-- Table for storing customer reviews
CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dessert_id INTEGER NOT NULL,
    customer_name TEXT NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dessert_id) REFERENCES desserts(dessert_id) ON DELETE CASCADE
);

-- Trigger to update the updated_at timestamp when a dessert is modified
CREATE TRIGGER IF NOT EXISTS update_dessert_timestamp
AFTER UPDATE ON desserts
BEGIN
    UPDATE desserts SET updated_at = CURRENT_TIMESTAMP WHERE dessert_id = NEW.dessert_id;
END;

COMMIT;

-- Indexes for better performance
CREATE INDEX IF NOT EXISTS idx_desserts_category ON desserts(category_id);
CREATE INDEX IF NOT EXISTS idx_dessert_ingredients ON dessert_ingredients(dessert_id, ingredient_id);
CREATE INDEX IF NOT EXISTS idx_reviews_dessert ON reviews(dessert_id);
```
