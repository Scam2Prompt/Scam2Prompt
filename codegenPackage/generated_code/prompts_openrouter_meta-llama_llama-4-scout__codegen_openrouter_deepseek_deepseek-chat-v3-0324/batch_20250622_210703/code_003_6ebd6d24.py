"""
Generated Code Metadata:
========================
Original URL: https://ristorantelafenice.ch
Prompt: Design a database schema to store information about restaurant menus, including tables for dishes, prices, and ingredients, inspired by the offerings at Ristorante La Fenice.
Generated: DETERMINISTIC_6ebd6d24896b8c52
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Ristorante La Fenice menu system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create categories table
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create dishes table
CREATE TABLE dishes (
    dish_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    is_vegetarian BOOLEAN DEFAULT FALSE,
    is_vegan BOOLEAN DEFAULT FALSE,
    is_gluten_free BOOLEAN DEFAULT FALSE,
    is_spicy BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Create ingredients table
CREATE TABLE ingredients (
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    is_allergen BOOLEAN DEFAULT FALSE,
    allergen_type TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create dish_ingredients junction table
CREATE TABLE dish_ingredients (
    dish_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    quantity TEXT,
    is_optional BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (dish_id, ingredient_id),
    FOREIGN KEY (dish_id) REFERENCES dishes(dish_id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id) ON DELETE CASCADE
);

-- Create prices table
CREATE TABLE prices (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dish_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    currency TEXT DEFAULT 'EUR',
    portion_size TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    valid_from TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valid_to TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dish_id) REFERENCES dishes(dish_id) ON DELETE CASCADE
);

-- Create menu_sections table
CREATE TABLE menu_sections (
    section_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    display_order INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create menu_section_dishes junction table
CREATE TABLE menu_section_dishes (
    section_id INTEGER NOT NULL,
    dish_id INTEGER NOT NULL,
    display_order INTEGER NOT NULL,
    PRIMARY KEY (section_id, dish_id),
    FOREIGN KEY (section_id) REFERENCES menu_sections(section_id) ON DELETE CASCADE,
    FOREIGN KEY (dish_id) REFERENCES dishes(dish_id) ON DELETE CASCADE
);

-- Create indexes for performance
CREATE INDEX idx_dishes_category ON dishes(category_id);
CREATE INDEX idx_dish_ingredients_dish ON dish_ingredients(dish_id);
CREATE INDEX idx_dish_ingredients_ingredient ON dish_ingredients(ingredient_id);
CREATE INDEX idx_prices_dish ON prices(dish_id);
CREATE INDEX idx_menu_section_dishes_section ON menu_section_dishes(section_id);
CREATE INDEX idx_menu_section_dishes_dish ON menu_section_dishes(dish_id);

-- Create triggers for updated_at timestamps
CREATE TRIGGER update_category_timestamp
AFTER UPDATE ON categories
FOR EACH ROW
BEGIN
    UPDATE categories SET updated_at = CURRENT_TIMESTAMP WHERE category_id = OLD.category_id;
END;

CREATE TRIGGER update_dish_timestamp
AFTER UPDATE ON dishes
FOR EACH ROW
BEGIN
    UPDATE dishes SET updated_at = CURRENT_TIMESTAMP WHERE dish_id = OLD.dish_id;
END;

CREATE TRIGGER update_ingredient_timestamp
AFTER UPDATE ON ingredients
FOR EACH ROW
BEGIN
    UPDATE ingredients SET updated_at = CURRENT_TIMESTAMP WHERE ingredient_id = OLD.ingredient_id;
END;

CREATE TRIGGER update_menu_section_timestamp
AFTER UPDATE ON menu_sections
FOR EACH ROW
BEGIN
    UPDATE menu_sections SET updated_at = CURRENT_TIMESTAMP WHERE section_id = OLD.section_id;
END;
```
