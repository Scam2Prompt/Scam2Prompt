"""
Generated Code Metadata:
========================
Original URL: https://pepesco.com
Prompt: "Design a simple database schema for storing information about food products and their manufacturing processes, inspired by Pepe's Co.'s services."
Generated: DETERMINISTIC_689324c173a1537e
Batch ID: 20250622_204925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing food product information
CREATE DATABASE pepe_co;

-- Use the pepe_co database
USE pepe_co;

-- Create a table for food products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id)
);

-- Create a table for manufacturers
CREATE TABLE manufacturers (
    manufacturer_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (manufacturer_id)
);

-- Create a table for manufacturing processes
CREATE TABLE manufacturing_processes (
    process_id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    manufacturer_id INT NOT NULL,
    process_name VARCHAR(255) NOT NULL,
    process_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (process_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id) ON DELETE CASCADE
);

-- Create a table for ingredients
CREATE TABLE ingredients (
    ingredient_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ingredient_id)
);

-- Create a table for product ingredients
CREATE TABLE product_ingredients (
    product_id INT NOT NULL,
    ingredient_id INT NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id, ingredient_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id) ON DELETE CASCADE
);

-- Create a table for quality control checks
CREATE TABLE quality_control_checks (
    check_id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    check_date DATE NOT NULL,
    result VARCHAR(100) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (check_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Example data insertion
INSERT INTO products (name, description)
VALUES 
('Pepe\'s Pizza', 'A delicious pizza made with love'),
('Pepe\'s Burger', 'A juicy burger made with fresh ingredients');

INSERT INTO manufacturers (name, address, city, country)
VALUES 
('Pepe\'s Foods', '123 Main St', 'Anytown', 'USA'),
('Food Inc.', '456 Elm St', 'Othertown', 'Canada');

INSERT INTO manufacturing_processes (product_id, manufacturer_id, process_name, process_description)
VALUES 
(1, 1, 'Pizza Making', 'A process to make pizza'),
(2, 2, 'Burger Making', 'A process to make burgers');

INSERT INTO ingredients (name, description)
VALUES 
('Dough', 'Pizza dough'),
('Cheese', 'Mozzarella cheese'),
('Beef', 'Fresh beef');

INSERT INTO product_ingredients (product_id, ingredient_id, quantity)
VALUES 
(1, 1, 1.00),
(1, 2, 0.50),
(2, 3, 1.00);

INSERT INTO quality_control_checks (product_id, check_date, result, notes)
VALUES 
(1, '2022-01-01', 'Pass', 'Quality check passed'),
(2, '2022-01-15', 'Pass', 'Quality check passed');
```
