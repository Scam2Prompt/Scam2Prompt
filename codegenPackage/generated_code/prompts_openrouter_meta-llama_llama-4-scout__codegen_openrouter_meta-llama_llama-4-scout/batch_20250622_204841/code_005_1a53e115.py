"""
Generated Code Metadata:
========================
Original URL: https://jgiwindia.com
Prompt: "Design a database schema to store information about various products like sugar boiled confectionery, food grains, and biscuits."
Generated: DETERMINISTIC_1a53e1152f47e5a7
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing product information
CREATE DATABASE product_database;

-- Use the created database
USE product_database;

-- Create a table for product categories
CREATE TABLE product_categories (
    category_id INT AUTO_INCREMENT,
    category_name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (category_id)
);

-- Create a table for products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    category_id INT,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id),
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE CASCADE
);

-- Create a table for product ingredients
CREATE TABLE product_ingredients (
    ingredient_id INT AUTO_INCREMENT,
    product_id INT,
    ingredient_name VARCHAR(255) NOT NULL,
    quantity VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ingredient_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a table for product nutritional information
CREATE TABLE product_nutrition (
    nutrition_id INT AUTO_INCREMENT,
    product_id INT,
    calories DECIMAL(10, 2),
    protein DECIMAL(10, 2),
    fat DECIMAL(10, 2),
    carbohydrates DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (nutrition_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Insert sample data into product categories
INSERT INTO product_categories (category_name, description)
VALUES 
('Sugar Boiled Confectionery', 'Sugar boiled confectionery products'),
('Food Grains', 'Food grain products'),
('Biscuits', 'Biscuit products');

-- Insert sample data into products
INSERT INTO products (product_name, category_id, price, quantity, description)
VALUES 
('Sugar Boiled Candy', 1, 5.99, 100, 'A sugar boiled candy'),
('Rice', 2, 2.99, 500, 'A food grain product'),
('Chocolate Biscuit', 3, 3.99, 200, 'A biscuit product');

-- Insert sample data into product ingredients
INSERT INTO product_ingredients (product_id, ingredient_name, quantity)
VALUES 
(1, 'Sugar', '100g'),
(1, 'Water', '50ml'),
(2, 'Rice', '1000g'),
(3, 'Wheat Flour', '500g');

-- Insert sample data into product nutritional information
INSERT INTO product_nutrition (product_id, calories, protein, fat, carbohydrates)
VALUES 
(1, 50.00, 0.50, 0.00, 12.00),
(2, 110.00, 2.50, 2.00, 25.00),
(3, 120.00, 2.00, 3.00, 20.00);
```
