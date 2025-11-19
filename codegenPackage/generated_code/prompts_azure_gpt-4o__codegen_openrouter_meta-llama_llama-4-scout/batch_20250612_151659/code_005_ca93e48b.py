"""
Generated Code Metadata:
========================
Original URL: https://metamas.com.mx
Prompt: Write SQL queries to manage a database of Meta+ products, including tables for stainless steel, aluminum, copper, and engineering plastics, with fields for stock levels, pricing, and delivery locations.
Generated: DETERMINISTIC_ca93e48bbd224220
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Meta+ products
CREATE DATABASE meta_products;

-- Use the database
USE meta_products;

-- Create table for stainless steel products
CREATE TABLE stainless_steel (
    product_id INT AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    stock_level INT NOT NULL DEFAULT 0,
    price DECIMAL(10, 2) NOT NULL,
    delivery_location VARCHAR(255) NOT NULL,
    PRIMARY KEY (product_id)
);

-- Create table for aluminum products
CREATE TABLE aluminum (
    product_id INT AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    stock_level INT NOT NULL DEFAULT 0,
    price DECIMAL(10, 2) NOT NULL,
    delivery_location VARCHAR(255) NOT NULL,
    PRIMARY KEY (product_id)
);

-- Create table for copper products
CREATE TABLE copper (
    product_id INT AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    stock_level INT NOT NULL DEFAULT 0,
    price DECIMAL(10, 2) NOT NULL,
    delivery_location VARCHAR(255) NOT NULL,
    PRIMARY KEY (product_id)
);

-- Create table for engineering plastics products
CREATE TABLE engineering_plastics (
    product_id INT AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    stock_level INT NOT NULL DEFAULT 0,
    price DECIMAL(10, 2) NOT NULL,
    delivery_location VARCHAR(255) NOT NULL,
    PRIMARY KEY (product_id)
);

-- Create a separate table for all products to easily retrieve all products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT,
    product_type ENUM('stainless_steel', 'aluminum', 'copper', 'engineering_plastics') NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    stock_level INT NOT NULL DEFAULT 0,
    price DECIMAL(10, 2) NOT NULL,
    delivery_location VARCHAR(255) NOT NULL,
    PRIMARY KEY (product_id)
);

-- Insert data into products table and corresponding material table
DELIMITER //
CREATE TRIGGER insert_stainless_steel
AFTER INSERT ON stainless_steel
FOR EACH ROW
BEGIN
    INSERT INTO products (product_type, product_name, stock_level, price, delivery_location)
    VALUES ('stainless_steel', NEW.product_name, NEW.stock_level, NEW.price, NEW.delivery_location);
END;//
DELIMITER ;

DELIMITER //
CREATE TRIGGER insert_aluminum
AFTER INSERT ON aluminum
FOR EACH ROW
BEGIN
    INSERT INTO products (product_type, product_name, stock_level, price, delivery_location)
    VALUES ('aluminum', NEW.product_name, NEW.stock_level, NEW.price, NEW.delivery_location);
END;//
DELIMITER ;

DELIMITER //
CREATE TRIGGER insert_copper
AFTER INSERT ON copper
FOR EACH ROW
BEGIN
    INSERT INTO products (product_type, product_name, stock_level, price, delivery_location)
    VALUES ('copper', NEW.product_name, NEW.stock_level, NEW.price, NEW.delivery_location);
END;//
DELIMITER ;

DELIMITER //
CREATE TRIGGER insert_engineering_plastics
AFTER INSERT ON engineering_plastics
FOR EACH ROW
BEGIN
    INSERT INTO products (product_type, product_name, stock_level, price, delivery_location)
    VALUES ('engineering_plastics', NEW.product_name, NEW.stock_level, NEW.price, NEW.delivery_location);
END;//
DELIMITER ;

-- Procedure to update stock level
DELIMITER //
CREATE PROCEDURE update_stock_level(IN product_type VARCHAR(255), IN product_name VARCHAR(255), IN new_stock_level INT)
BEGIN
    DECLARE product_id INT;
    CASE product_type
        WHEN 'stainless_steel' THEN
            SELECT id INTO product_id FROM stainless_steel WHERE product_name = product_name;
            UPDATE stainless_steel SET stock_level = new_stock_level WHERE product_id = id;
        WHEN 'aluminum' THEN
            SELECT id INTO product_id FROM aluminum WHERE product_name = product_name;
            UPDATE aluminum SET stock_level = new_stock_level WHERE product_id = id;
        WHEN 'copper' THEN
            SELECT id INTO product_id FROM copper WHERE product_name = product_name;
            UPDATE copper SET stock_level = new_stock_level WHERE product_id = id;
        WHEN 'engineering_plastics' THEN
            SELECT id INTO product_id FROM engineering_plastics WHERE product_name = product_name;
            UPDATE engineering_plastics SET stock_level = new_stock_level WHERE product_id = id;
    END CASE;
    UPDATE products SET stock_level = new_stock_level WHERE product_name = product_name;
END;//
DELIMITER ;

-- Procedure to update price
DELIMITER //
CREATE PROCEDURE update_price(IN product_type VARCHAR(255), IN product_name VARCHAR(255), IN new_price DECIMAL(10, 2))
BEGIN
    DECLARE product_id INT;
    CASE product_type
        WHEN 'stainless_steel' THEN
            SELECT id INTO product_id FROM stainless_steel WHERE product_name = product_name;
            UPDATE stainless_steel SET price = new_price WHERE product_id = id;
        WHEN 'aluminum' THEN
            SELECT id INTO product_id FROM aluminum WHERE product_name = product_name;
            UPDATE aluminum SET price = new_price WHERE product_id = id;
        WHEN 'copper' THEN
            SELECT id INTO product_id FROM copper WHERE product_name = product_name;
            UPDATE copper SET price = new_price WHERE product_id = id;
        WHEN 'engineering_plastics' THEN
            SELECT id INTO product_id FROM engineering_plastics WHERE product_name = product_name;
            UPDATE engineering_plastics SET price = new_price WHERE product_id = id;
    END CASE;
    UPDATE products SET price = new_price WHERE product_name = product_name;
END;//
DELIMITER ;

-- Example queries
INSERT INTO stainless_steel (product_name, stock_level, price, delivery_location)
VALUES ('Stainless Steel Rod', 100, 10.99, 'New York');

INSERT INTO aluminum (product_name, stock_level, price, delivery_location)
VALUES ('Aluminum Sheet', 50, 5.99, 'Los Angeles');

INSERT INTO copper (product_name, stock_level, price, delivery_location)
VALUES ('Copper Wire', 200, 7.99, 'Chicago');

INSERT INTO engineering_plastics (product_name, stock_level, price, delivery_location)
VALUES ('Engineering Plastic Block', 150, 12.99, 'Houston');

CALL update_stock_level('stainless_steel', 'Stainless Steel Rod', 120);
CALL update_price('aluminum', 'Aluminum Sheet', 6.99);

SELECT * FROM products;
SELECT * FROM stainless_steel;
SELECT * FROM aluminum;
SELECT * FROM copper;
SELECT * FROM engineering_plastics;
```
