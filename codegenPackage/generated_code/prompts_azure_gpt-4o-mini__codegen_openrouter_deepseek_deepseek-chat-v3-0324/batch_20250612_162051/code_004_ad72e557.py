"""
Generated Code Metadata:
========================
Original URL: https://perfectfoodcorner.com
Prompt: Construct a SQL database schema to store information about various food items, their dietary options, and packaging details, inspired by the menu structure of Perfect Food Corner.
Generated: DETERMINISTIC_ad72e5577a0d3489
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Perfect Food Corner

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create table for dietary options
CREATE TABLE IF NOT EXISTS dietary_options (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Create table for packaging types
CREATE TABLE IF NOT EXISTS packaging_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    is_recyclable BOOLEAN DEFAULT FALSE
);

-- Create table for food categories
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    parent_category_id INTEGER,
    FOREIGN KEY (parent_category_id) REFERENCES categories(id) ON DELETE SET NULL
);

-- Create table for food items
CREATE TABLE IF NOT EXISTS food_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,
    preparation_time INTEGER, -- in minutes
    category_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Create junction table for food items and dietary options (many-to-many)
CREATE TABLE IF NOT EXISTS food_item_dietary_options (
    food_item_id INTEGER NOT NULL,
    dietary_option_id INTEGER NOT NULL,
    PRIMARY KEY (food_item_id, dietary_option_id),
    FOREIGN KEY (food_item_id) REFERENCES food_items(id) ON DELETE CASCADE,
    FOREIGN KEY (dietary_option_id) REFERENCES dietary_options(id) ON DELETE CASCADE
);

-- Create table for packaging options for food items
CREATE TABLE IF NOT EXISTS food_item_packaging (
    food_item_id INTEGER NOT NULL,
    packaging_type_id INTEGER NOT NULL,
    additional_cost DECIMAL(10, 2) DEFAULT 0.00,
    is_default BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (food_item_id, packaging_type_id),
    FOREIGN KEY (food_item_id) REFERENCES food_items(id) ON DELETE CASCADE,
    FOREIGN KEY (packaging_type_id) REFERENCES packaging_types(id) ON DELETE CASCADE
);

-- Create table for ingredients
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    is_allergen BOOLEAN DEFAULT FALSE
);

-- Create junction table for food items and ingredients (many-to-many)
CREATE TABLE IF NOT EXISTS food_item_ingredients (
    food_item_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    quantity TEXT, -- e.g., "100g", "1 cup", etc.
    is_optional BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (food_item_id, ingredient_id),
    FOREIGN KEY (food_item_id) REFERENCES food_items(id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(id) ON DELETE CASCADE
);

-- Create table for nutritional information
CREATE TABLE IF NOT EXISTS nutritional_info (
    food_item_id INTEGER PRIMARY KEY,
    calories INTEGER,
    protein_g DECIMAL(10, 2),
    carbohydrates_g DECIMAL(10, 2),
    fat_g DECIMAL(10, 2),
    fiber_g DECIMAL(10, 2),
    sodium_mg DECIMAL(10, 2),
    FOREIGN KEY (food_item_id) REFERENCES food_items(id) ON DELETE CASCADE
);

-- Create index for frequently queried columns
CREATE INDEX IF NOT EXISTS idx_food_items_category ON food_items(category_id);
CREATE INDEX IF NOT EXISTS idx_food_items_availability ON food_items(is_available);
CREATE INDEX IF NOT EXISTS idx_ingredients_allergen ON ingredients(is_allergen);
```
