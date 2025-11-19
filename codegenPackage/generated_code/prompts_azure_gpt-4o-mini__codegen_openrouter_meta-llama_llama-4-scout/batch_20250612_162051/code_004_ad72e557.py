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
-- Create database schema for Perfect Food Corner menu
CREATE DATABASE perfect_food_corner;

-- Use the created database
USE perfect_food_corner;

-- Create table for dietary options
CREATE TABLE dietary_options (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create table for packaging details
CREATE TABLE packaging_details (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create table for food items
CREATE TABLE food_items (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for food item dietary options
CREATE TABLE food_item_dietary_options (
  food_item_id INT NOT NULL,
  dietary_option_id INT NOT NULL,
  PRIMARY KEY (food_item_id, dietary_option_id),
  FOREIGN KEY (food_item_id) REFERENCES food_items(id) ON DELETE CASCADE,
  FOREIGN KEY (dietary_option_id) REFERENCES dietary_options(id) ON DELETE CASCADE
);

-- Create table for food item packaging details
CREATE TABLE food_item_packaging_details (
  food_item_id INT NOT NULL,
  packaging_detail_id INT NOT NULL,
  PRIMARY KEY (food_item_id, packaging_detail_id),
  FOREIGN KEY (food_item_id) REFERENCES food_items(id) ON DELETE CASCADE,
  FOREIGN KEY (packaging_detail_id) REFERENCES packaging_details(id) ON DELETE CASCADE
);

-- Insert sample data into dietary options table
INSERT INTO dietary_options (name, description)
VALUES
('Vegan', 'Plant-based diet, excludes all animal products'),
('Gluten-free', 'Diet that excludes gluten, a protein found in wheat, barley, and rye'),
('Vegetarian', 'Diet that excludes meat, fish, and poultry');

-- Insert sample data into packaging details table
INSERT INTO packaging_details (name, description)
VALUES
('Single-serve', 'Packaging designed for individual consumption'),
('Family-size', 'Packaging designed for multiple people'),
('Take-out', 'Packaging designed for take-out or delivery');

-- Insert sample data into food items table
INSERT INTO food_items (name, description, price)
VALUES
('Vegan Burger', 'Plant-based burger patty, lettuce, tomato, and vegan mayo', 12.99),
('Grilled Chicken Sandwich', 'Grilled chicken breast, lettuce, tomato, and mayo', 10.99),
('Salad Bowl', 'Mixed greens, vegetables, and choice of protein', 9.99);

-- Insert sample data into food item dietary options table
INSERT INTO food_item_dietary_options (food_item_id, dietary_option_id)
VALUES
(1, 1), -- Vegan Burger is vegan
(1, 3), -- Vegan Burger is vegetarian
(2, 3), -- Grilled Chicken Sandwich is vegetarian
(3, 1), -- Salad Bowl can be vegan
(3, 2), -- Salad Bowl can be gluten-free
(3, 3); -- Salad Bowl is vegetarian

-- Insert sample data into food item packaging details table
INSERT INTO food_item_packaging_details (food_item_id, packaging_detail_id)
VALUES
(1, 1), -- Vegan Burger comes in single-serve packaging
(1, 3), -- Vegan Burger can be taken out
(2, 1), -- Grilled Chicken Sandwich comes in single-serve packaging
(2, 3), -- Grilled Chicken Sandwich can be taken out
(3, 1), -- Salad Bowl comes in single-serve packaging
(3, 2); -- Salad Bowl comes in family-size packaging
```
