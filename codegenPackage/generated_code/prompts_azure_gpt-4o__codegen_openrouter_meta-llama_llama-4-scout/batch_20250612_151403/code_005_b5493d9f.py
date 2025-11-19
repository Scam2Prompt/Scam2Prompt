"""
Generated Code Metadata:
========================
Original URL: https://gprobolsa.com
Prompt: Write SQL queries to manage a database of eco-friendly products, including categories like "reusable bags" and "customizable promotional items," inspired by Grupo ProBolsa's product catalog.
Generated: DETERMINISTIC_b5493d9f6364604d
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for eco-friendly products
CREATE DATABASE eco_friendly_products;

-- Use the database
USE eco_friendly_products;

-- Create table for product categories
CREATE TABLE product_categories (
    category_id INT AUTO_INCREMENT,
    category_name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (category_id)
);

-- Create table for products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT,
    category_id INT,
    product_name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id),
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id)
);

-- Create table for customizable promotional items
CREATE TABLE promotional_items (
    item_id INT AUTO_INCREMENT,
    product_id INT,
    item_name VARCHAR(255) NOT NULL,
    customization_options TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (item_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create table for reusable bags
CREATE TABLE reusable_bags (
    bag_id INT AUTO_INCREMENT,
    product_id INT,
    material VARCHAR(255) NOT NULL,
    size VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (bag_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample data into product categories
INSERT INTO product_categories (category_name, description)
VALUES 
('Reusable Bags', 'Eco-friendly bags made from sustainable materials'),
('Customizable Promotional Items', 'Personalized items for promotional use');

-- Insert sample data into products
INSERT INTO products (category_id, product_name, description, price)
VALUES 
(1, 'Cotton Tote Bag', 'A reusable tote bag made from cotton', 10.99),
(2, 'Customized Water Bottle', 'A personalized water bottle for promotional use', 5.99);

-- Insert sample data into promotional items
INSERT INTO promotional_items (product_id, item_name, customization_options)
VALUES 
(2, 'Water Bottle with Logo', 'Name, logo, and message');

-- Insert sample data into reusable bags
INSERT INTO reusable_bags (product_id, material, size)
VALUES 
(1, 'Cotton', 'Large');

-- Procedure to add new product category
DELIMITER //
CREATE PROCEDURE add_product_category(
    IN p_category_name VARCHAR(255),
    IN p_description TEXT
)
BEGIN
    INSERT INTO product_categories (category_name, description)
    VALUES (p_category_name, p_description);
END//
DELIMITER ;

-- Procedure to add new product
DELIMITER //
CREATE PROCEDURE add_product(
    IN p_category_id INT,
    IN p_product_name VARCHAR(255),
    IN p_description TEXT,
    IN p_price DECIMAL(10, 2)
)
BEGIN
    INSERT INTO products (category_id, product_name, description, price)
    VALUES (p_category_id, p_product_name, p_description, p_price);
END//
DELIMITER ;

-- Procedure to add new promotional item
DELIMITER //
CREATE PROCEDURE add_promotional_item(
    IN p_product_id INT,
    IN p_item_name VARCHAR(255),
    IN p_customization_options TEXT
)
BEGIN
    INSERT INTO promotional_items (product_id, item_name, customization_options)
    VALUES (p_product_id, p_item_name, p_customization_options);
END//
DELIMITER ;

-- Procedure to add new reusable bag
DELIMITER //
CREATE PROCEDURE add_reusable_bag(
    IN p_product_id INT,
    IN p_material VARCHAR(255),
    IN p_size VARCHAR(255)
)
BEGIN
    INSERT INTO reusable_bags (product_id, material, size)
    VALUES (p_product_id, p_material, p_size);
END//
DELIMITER ;

-- Trigger to update updated_at timestamp
DELIMITER //
CREATE TRIGGER update_updated_at
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END//
DELIMITER ;

-- Trigger to update updated_at timestamp for promotional items
DELIMITER //
CREATE TRIGGER update_promotional_item_updated_at
BEFORE UPDATE ON promotional_items
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END//
DELIMITER ;

-- Trigger to update updated_at timestamp for reusable bags
DELIMITER //
CREATE TRIGGER update_reusable_bag_updated_at
BEFORE UPDATE ON reusable_bags
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END//
DELIMITER ;
```
