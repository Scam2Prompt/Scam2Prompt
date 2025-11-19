"""
Generated Code Metadata:
========================
Original URL: https://chayatime.com
Prompt: Design a database schema to store information about ChayaTime's menu items, including tea, snacks, and milkshakes.
Generated: DETERMINISTIC_b8a56f7951d6dd44
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for ChayaTime's menu items
CREATE DATABASE chaya_time;

-- Use the chaya_time database
USE chaya_time;

-- Create a table for menu categories
CREATE TABLE menu_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for menu items
CREATE TABLE menu_items (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES menu_categories(id) ON DELETE CASCADE
);

-- Create a table for tea menu items
CREATE TABLE tea_menu_items (
  id INT AUTO_INCREMENT,
  menu_item_id INT NOT NULL,
  tea_type VARCHAR(255) NOT NULL,
  milk_options ENUM('whole', 'skim', 'almond', 'soy', 'coconut') DEFAULT 'whole',
  sugar_options ENUM('none', 'one', 'two', 'three') DEFAULT 'none',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (menu_item_id) REFERENCES menu_items(id) ON DELETE CASCADE
);

-- Create a table for snack menu items
CREATE TABLE snack_menu_items (
  id INT AUTO_INCREMENT,
  menu_item_id INT NOT NULL,
  calories INT,
  dietary_restrictions ENUM('gluten-free', 'vegan', 'vegetarian') DEFAULT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (menu_item_id) REFERENCES menu_items(id) ON DELETE CASCADE
);

-- Create a table for milkshake menu items
CREATE TABLE milkshake_menu_items (
  id INT AUTO_INCREMENT,
  menu_item_id INT NOT NULL,
  milkshake_flavor VARCHAR(255) NOT NULL,
  ice_cream_type ENUM('vanilla', 'chocolate', 'strawberry') NOT NULL,
  toppings TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (menu_item_id) REFERENCES menu_items(id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO menu_categories (name, description) 
VALUES 
('Tea', 'Our selection of artisanal teas'),
('Snacks', 'Delicious treats to pair with your tea'),
('Milkshakes', 'Creamy and indulgent milkshakes');

INSERT INTO menu_items (category_id, name, description, price) 
VALUES 
(1, 'Earl Grey', 'A classic black tea flavored with bergamot', 3.50),
(1, 'English Breakfast', 'A strong and malty black tea', 3.25),
(2, 'Scone', 'A freshly baked scone', 4.00),
(3, 'Strawberry Milkshake', 'A creamy milkshake made with fresh strawberries', 6.00);

INSERT INTO tea_menu_items (menu_item_id, tea_type, milk_options, sugar_options) 
VALUES 
(1, 'Black', 'whole', 'one'),
(2, 'Black', 'skim', 'none');

INSERT INTO snack_menu_items (menu_item_id, calories, dietary_restrictions) 
VALUES 
(3, 200, 'vegetarian');

INSERT INTO milkshake_menu_items (menu_item_id, milkshake_flavor, ice_cream_type, toppings) 
VALUES 
(4, 'Strawberry', 'vanilla', 'whipped cream, sprinkles');
```
