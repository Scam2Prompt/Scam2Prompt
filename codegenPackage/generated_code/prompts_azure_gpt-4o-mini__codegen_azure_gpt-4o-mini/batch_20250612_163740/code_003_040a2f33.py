"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Develop a sample database schema for a Professional Kitchen Management system that includes tables for food pricing, menu design, and chef responsibilities, as outlined in the courses at Hampton's.
Generated: DETERMINISTIC_040a2f3380345c75
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Professional Kitchen Management System

-- Create a database for the kitchen management system
CREATE DATABASE KitchenManagement;

-- Use the created database
USE KitchenManagement;

-- Table to store food items and their pricing
CREATE TABLE FoodPricing (
    food_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each food item
    food_name VARCHAR(100) NOT NULL,        -- Name of the food item
    price DECIMAL(10, 2) NOT NULL,          -- Price of the food item
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the item was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    CHECK (price >= 0)                      -- Ensure price is non-negative
);

-- Table to store menu designs
CREATE TABLE MenuDesign (
    menu_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each menu
    menu_name VARCHAR(100) NOT NULL,         -- Name of the menu
    description TEXT,                        -- Description of the menu
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the menu was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to link food items to menus
CREATE TABLE MenuItems (
    menu_item_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each menu item
    menu_id INT NOT NULL,                        -- Foreign key referencing MenuDesign
    food_id INT NOT NULL,                        -- Foreign key referencing FoodPricing
    FOREIGN KEY (menu_id) REFERENCES MenuDesign(menu_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (food_id) REFERENCES FoodPricing(food_id) ON DELETE CASCADE, -- Ensure referential integrity
    UNIQUE (menu_id, food_id)                   -- Ensure a food item can only appear once in a menu
);

-- Table to store chef responsibilities
CREATE TABLE ChefResponsibilities (
    chef_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each chef
    chef_name VARCHAR(100) NOT NULL,            -- Name of the chef
    responsibility VARCHAR(255) NOT NULL,       -- Description of the chef's responsibility
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the responsibility was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to link chefs to menus
CREATE TABLE ChefMenuAssignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    chef_id INT NOT NULL,                          -- Foreign key referencing ChefResponsibilities
    menu_id INT NOT NULL,                          -- Foreign key referencing MenuDesign
    FOREIGN KEY (chef_id) REFERENCES ChefResponsibilities(chef_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (menu_id) REFERENCES MenuDesign(menu_id) ON DELETE CASCADE, -- Ensure referential integrity
    UNIQUE (chef_id, menu_id)                     -- Ensure a chef can only be assigned to a menu once
);

-- Sample data insertion (optional)
INSERT INTO FoodPricing (food_name, price) VALUES
('Grilled Chicken', 12.99),
('Caesar Salad', 8.50),
('Chocolate Cake', 5.00);

INSERT INTO MenuDesign (menu_name, description) VALUES
('Lunch Special', 'A delightful selection of lunch items.'),
('Dinner Feast', 'An exquisite dinner menu for special occasions.');

INSERT INTO MenuItems (menu_id, food_id) VALUES
(1, 1), -- Grilled Chicken in Lunch Special
(1, 2), -- Caesar Salad in Lunch Special
(2, 1), -- Grilled Chicken in Dinner Feast
(2, 3); -- Chocolate Cake in Dinner Feast

INSERT INTO ChefResponsibilities (chef_name, responsibility) VALUES
('Chef John', 'Prepare and cook all lunch items.'),
('Chef Sarah', 'Manage dinner service and dessert preparation.');

INSERT INTO ChefMenuAssignments (chef_id, menu_id) VALUES
(1, 1), -- Chef John assigned to Lunch Special
(2, 2); -- Chef Sarah assigned to Dinner Feast
```
