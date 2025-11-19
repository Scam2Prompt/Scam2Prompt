"""
Generated Code Metadata:
========================
Original URL: https://bodegajeanbousquet.com.ar
Prompt: Design a database schema to store menu and wine information for a restaurant and winery like Bodega Jean Bousquet, including tables for menu items, wine varieties, and customer reservations.
Generated: DETERMINISTIC_ea50fe1a931b9de1
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for restaurant and winery
CREATE DATABASE bodega_jean_bousquet;

-- Use database
USE bodega_jean_bousquet;

-- Create table for menu items
CREATE TABLE menu_items (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `category` ENUM('appetizer', 'entree', 'dessert', 'drink') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for wine varieties
CREATE TABLE wine_varieties (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `varietal` VARCHAR(255) NOT NULL,
  `vintage` INT,
  `price` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for wine inventory
CREATE TABLE wine_inventory (
  `id` INT AUTO_INCREMENT,
  `wine_variety_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`wine_variety_id`) REFERENCES wine_varieties(`id`) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE customers (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for reservations
CREATE TABLE reservations (
  `id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `date` DATE NOT NULL,
  `time` TIME NOT NULL,
  `party_size` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`id`) ON DELETE CASCADE
);

-- Create table for menu item orders
CREATE TABLE orders (
  `id` INT AUTO_INCREMENT,
  `reservation_id` INT,
  `menu_item_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`reservation_id`) REFERENCES reservations(`id`) ON DELETE SET NULL,
  FOREIGN KEY (`menu_item_id`) REFERENCES menu_items(`id`) ON DELETE CASCADE
);

-- Create table for wine orders
CREATE TABLE wine_orders (
  `id` INT AUTO_INCREMENT,
  `reservation_id` INT,
  `wine_variety_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`reservation_id`) REFERENCES reservations(`id`) ON DELETE SET NULL,
  FOREIGN KEY (`wine_variety_id`) REFERENCES wine_varieties(`id`) ON DELETE CASCADE
);
```

```sql
-- sample_data.sql

-- Insert sample menu items
INSERT INTO menu_items (name, description, price, category)
VALUES
  ('Grilled Steak', 'Grilled steak with roasted vegetables', 25.00, 'entree'),
  ('Pan-Seared Salmon', 'Pan-seared salmon with quinoa and steamed broccoli', 22.00, 'entree'),
  ('Bruschetta', 'Toasted bread with fresh tomatoes and basil', 8.00, 'appetizer'),
  ('Tiramisu', 'Ladyfingers soaked in espresso and liqueur', 7.00, 'dessert');

-- Insert sample wine varieties
INSERT INTO wine_varieties (name, description, varietal, vintage, price)
VALUES
  ('Chardonnay', 'Buttery and oaky chardonnay', 'Chardonnay', 2020, 12.00),
  ('Cabernet Sauvignon', 'Full-bodied cabernet sauvignon', 'Cabernet Sauvignon', 2019, 15.00),
  ('Merlot', 'Smooth and approachable merlot', 'Merlot', 2018, 10.00);

-- Insert sample wine inventory
INSERT INTO wine_inventory (wine_variety_id, quantity)
VALUES
  (1, 100),
  (2, 50),
  (3, 200);

-- Insert sample customers
INSERT INTO customers (first_name, last_name, email, phone)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210');

-- Insert sample reservations
INSERT INTO reservations (customer_id, date, time, party_size)
VALUES
  (1, '2024-09-16', '18:00:00', 4),
  (2, '2024-09-17', '19:00:00', 2);

-- Insert sample orders
INSERT INTO orders (reservation_id, menu_item_id, quantity)
VALUES
  (1, 1, 2),
  (1, 3, 1),
  (2, 2, 1);

-- Insert sample wine orders
INSERT INTO wine_orders (reservation_id, wine_variety_id, quantity)
VALUES
  (1, 1, 1),
  (2, 2, 2);
```
