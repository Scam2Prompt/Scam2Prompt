"""
Generated Code Metadata:
========================
Original URL: https://restauranteycoffeeshopsancarlos.com
Prompt: Create a SQL database schema to store information about restaurant locations, menus, and orders for a chain of restaurants including Restaurante y Coffee Shop San Carlos in Guatemala.
Generated: DETERMINISTIC_2ede589ba418732f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for restaurant chain
CREATE DATABASE restaurant_chain;

-- Use the database
USE restaurant_chain;

-- Create table for locations
CREATE TABLE locations (
  location_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  postal_code VARCHAR(20) NOT NULL,
  phone_number VARCHAR(20),
  email VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (location_id)
);

-- Create table for menus
CREATE TABLE menus (
  menu_id INT AUTO_INCREMENT,
  location_id INT NOT NULL,
  menu_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (menu_id),
  FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE
);

-- Create table for menu items
CREATE TABLE menu_items (
  item_id INT AUTO_INCREMENT,
  menu_id INT NOT NULL,
  item_name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (item_id),
  FOREIGN KEY (menu_id) REFERENCES menus(menu_id) ON DELETE CASCADE
);

-- Create table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  location_id INT NOT NULL,
  order_date DATE NOT NULL,
  total DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'in_progress', 'delivered', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id),
  FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE
);

-- Create table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  item_id INT NOT NULL,
  quantity INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
  FOREIGN KEY (item_id) REFERENCES menu_items(item_id) ON DELETE CASCADE
);

-- Insert sample data for Restaurante y Coffee Shop San Carlos
INSERT INTO locations (name, address, city, country, postal_code, phone_number, email)
VALUES 
('Restaurante y Coffee Shop San Carlos', 'Calle Principal', 'Guatemala City', 'Guatemala', '01001', '+502 12345678', 'info@san-carlos.com');

INSERT INTO menus (location_id, menu_name, description)
VALUES 
(1, 'Breakfast Menu', 'Delicious breakfast options'),
(1, 'Lunch Menu', 'Tasty lunch options'),
(1, 'Dinner Menu', 'Exquisite dinner options');

INSERT INTO menu_items (menu_id, item_name, description, price)
VALUES 
(1, 'Coffee', 'Freshly brewed coffee', 2.50),
(1, 'Pancakes', 'Fluffy pancakes with syrup', 5.00),
(2, 'Burger', 'Juicy beef burger', 8.00),
(2, 'Salad', 'Fresh mixed greens', 6.00),
(3, 'Steak', 'Grilled steak with roasted vegetables', 15.00);

INSERT INTO orders (location_id, order_date, total)
VALUES 
(1, '2022-01-01', 10.00),
(1, '2022-01-02', 20.00);

INSERT INTO order_items (order_id, item_id, quantity)
VALUES 
(1, 1, 2),
(1, 2, 1),
(2, 3, 1),
(2, 4, 2);
```
