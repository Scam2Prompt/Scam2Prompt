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
-- Database schema for storing restaurant menu information

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Ingredients CASCADE;
DROP TABLE IF EXISTS Dishes CASCADE;
DROP TABLE IF EXISTS Menus CASCADE;

-- Table to store ingredients
CREATE TABLE Ingredients (
    ingredient_id SERIAL PRIMARY KEY,  -- Unique identifier for each ingredient
    name VARCHAR(100) NOT NULL,         -- Name of the ingredient
    description TEXT,                   -- Description of the ingredient
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the ingredient was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store dishes
CREATE TABLE Dishes (
    dish_id SERIAL PRIMARY KEY,          -- Unique identifier for each dish
    name VARCHAR(100) NOT NULL,          -- Name of the dish
    description TEXT,                    -- Description of the dish
    price DECIMAL(10, 2) NOT NULL,       -- Price of the dish
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the dish was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store the relationship between dishes and ingredients
CREATE TABLE Dish_Ingredients (
    dish_id INT NOT NULL,                -- Foreign key referencing Dishes
    ingredient_id INT NOT NULL,          -- Foreign key referencing Ingredients
    quantity VARCHAR(50),                -- Quantity of the ingredient used in the dish
    PRIMARY KEY (dish_id, ingredient_id),  -- Composite primary key
    FOREIGN KEY (dish_id) REFERENCES Dishes(dish_id) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store menus
CREATE TABLE Menus (
    menu_id SERIAL PRIMARY KEY,          -- Unique identifier for each menu
    name VARCHAR(100) NOT NULL,          -- Name of the menu (e.g., Lunch, Dinner)
    description TEXT,                    -- Description of the menu
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the menu was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store the relationship between menus and dishes
CREATE TABLE Menu_Dishes (
    menu_id INT NOT NULL,                -- Foreign key referencing Menus
    dish_id INT NOT NULL,                -- Foreign key referencing Dishes
    PRIMARY KEY (menu_id, dish_id),      -- Composite primary key
    FOREIGN KEY (menu_id) REFERENCES Menus(menu_id) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (dish_id) REFERENCES Dishes(dish_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_ingredient_name ON Ingredients(name);
CREATE INDEX idx_dish_name ON Dishes(name);
CREATE INDEX idx_menu_name ON Menus(name);
```
