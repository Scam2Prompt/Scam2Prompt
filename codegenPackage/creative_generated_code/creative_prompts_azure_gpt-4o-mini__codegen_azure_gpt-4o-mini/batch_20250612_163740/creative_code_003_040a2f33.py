"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamptons-uk.com
Prompt: Develop a sample database schema for a Professional Kitchen Management system that includes tables for food pricing, menu design, and chef responsibilities, as outlined in the courses at Hampton's.
Generated: DETERMINISTIC_040a2f3380345c75
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Sample Database Schema for a Professional Kitchen Management System

-- Drop existing tables if they exist to avoid conflicts
DROP TABLE IF EXISTS ChefResponsibilities;
DROP TABLE IF EXISTS MenuDesign;
DROP TABLE IF EXISTS FoodPricing;

-- Table for storing information about food items and their prices
CREATE TABLE FoodPricing (
    id SERIAL PRIMARY KEY,             -- Unique identifier for each food item
    food_name VARCHAR(100) NOT NULL,   -- Name of the food item
    price DECIMAL(10, 2) NOT NULL,      -- Price of the food item
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for designing the menu
CREATE TABLE MenuDesign (
    id SERIAL PRIMARY KEY,              -- Unique identifier for each menu
    menu_name VARCHAR(100) NOT NULL,    -- Name of the menu
    food_item_id INT NOT NULL,          -- Foreign key referencing FoodPricing
    description TEXT,                    -- Description of the menu item
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (food_item_id) REFERENCES FoodPricing(id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table for storing chef responsibilities
CREATE TABLE ChefResponsibilities (
    id SERIAL PRIMARY KEY,              -- Unique identifier for each responsibility
    chef_name VARCHAR(100) NOT NULL,    -- Name of the chef
    responsibility TEXT NOT NULL,        -- Description of the responsibility
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of assignment
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Sample data insertions for FoodPricing
INSERT INTO FoodPricing (food_name, price) VALUES
('Grilled Chicken', 12.99),
('Caesar Salad', 8.50),
('Chocolate Cake', 5.00);

-- Sample data insertions for MenuDesign
INSERT INTO MenuDesign (menu_name, food_item_id, description) VALUES
('Lunch Special', 1, 'Grilled Chicken served with seasonal vegetables.'),
('Dessert Menu', 3, 'Rich chocolate cake topped with whipped cream.');

-- Sample data insertions for ChefResponsibilities
INSERT INTO ChefResponsibilities (chef_name, responsibility) VALUES
('Chef John', 'Oversees all kitchen operations.'),
('Chef Anna', 'Manages food preparation and plating.');

-- End of database schema
```
