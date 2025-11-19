"""
Generated Code Metadata:
========================
Original URL: https://kingoficecream.com
Prompt: Design a database schema to store menu items and sales data for a snow cone truck business, including items offered by King Of Icecream.
Generated: DETERMINISTIC_3be1837b522c8d50
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for King Of Icecream snow cone truck business
CREATE DATABASE king_of_icecream;

-- Use the database
USE king_of_icecream;

-- Create table for menu items
CREATE TABLE menu_items (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for sales data
CREATE TABLE sales (
  `id` INT AUTO_INCREMENT,
  `menu_item_id` INT NOT NULL,
  `sale_date` DATE NOT NULL,
  `quantity` INT NOT NULL,
  `total_revenue` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`menu_item_id`) REFERENCES menu_items(`id`)
);

-- Create table for flavors
CREATE TABLE flavors (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create many-to-many relationship table for menu items and flavors
CREATE TABLE menu_item_flavors (
  `menu_item_id` INT NOT NULL,
  `flavor_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`menu_item_id`, `flavor_id`),
  FOREIGN KEY (`menu_item_id`) REFERENCES menu_items(`id`),
  FOREIGN KEY (`flavor_id`) REFERENCES flavors(`id`)
);

-- Create table for toppings
CREATE TABLE toppings (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `price` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create many-to-many relationship table for menu items and toppings
CREATE TABLE menu_item_toppings (
  `menu_item_id` INT NOT NULL,
  `topping_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`menu_item_id`, `topping_id`),
  FOREIGN KEY (`menu_item_id`) REFERENCES menu_items(`id`),
  FOREIGN KEY (`topping_id`) REFERENCES toppings(`id`)
);

-- Insert sample data
INSERT INTO menu_items (name, description, price)
VALUES 
  ('Snow Cone', 'A classic snow cone', 3.50),
  ('Ice Cream Sandwich', 'A cool ice cream sandwich', 4.00),
  ('Snow Cone Combo', 'A snow cone with a topping', 5.00);

INSERT INTO flavors (name)
VALUES 
  ('Blue Raspberry'),
  ('Strawberry'),
  ('Lemon-Lime');

INSERT INTO menu_item_flavors (menu_item_id, flavor_id)
VALUES 
  (1, 1),
  (1, 2),
  (2, 3);

INSERT INTO toppings (name, price)
VALUES 
  ('Sprinkles', 0.50),
  ('Whipped Cream', 1.00);

INSERT INTO menu_item_toppings (menu_item_id, topping_id)
VALUES 
  (3, 1),
  (3, 2);

INSERT INTO sales (menu_item_id, sale_date, quantity, total_revenue)
VALUES 
  (1, '2022-01-01', 10, 35.00),
  (2, '2022-01-02', 5, 20.00),
  (3, '2022-01-03', 8, 40.00);
```
