"""
Generated Code Metadata:
========================
Original URL: https://fanzyfashion.in
Prompt: Design a database schema for an e-commerce database storing information about products, including jeans, jewelry sets, and kid's clothing, with fields for price, discount, and product ratings.
Generated: DETERMINISTIC_17cf8c470858d57d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the e-commerce platform
CREATE DATABASE ecommerce;

-- Use the ecommerce database
USE ecommerce;

-- Create a table for products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    product_description TEXT,
    product_type ENUM('jeans', 'jewelry_set', 'kids_clothing') NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    discount DECIMAL(5, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id)
);

-- Create a table for product ratings
CREATE TABLE product_ratings (
    rating_id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    rating TINYINT NOT NULL,
    review TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (rating_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a table for jeans products
CREATE TABLE jeans (
    product_id INT NOT NULL,
    size VARCHAR(10) NOT NULL,
    material VARCHAR(50) NOT NULL,
    waist_size INT NOT NULL,
    inseam_length INT NOT NULL,
    PRIMARY KEY (product_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a table for jewelry sets
CREATE TABLE jewelry_sets (
    product_id INT NOT NULL,
    set_type VARCHAR(50) NOT NULL,
    metal_type VARCHAR(50) NOT NULL,
    gemstone VARCHAR(50),
    PRIMARY KEY (product_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a table for kid's clothing
CREATE TABLE kids_clothing (
    product_id INT NOT NULL,
    size VARCHAR(10) NOT NULL,
    age_group ENUM('infant', 'toddler', 'child') NOT NULL,
    material VARCHAR(50) NOT NULL,
    PRIMARY KEY (product_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a trigger to prevent deletion of products with existing ratings
DELIMITER $$
CREATE TRIGGER prevent_product_deletion
BEFORE DELETE ON products
FOR EACH ROW
BEGIN
    IF EXISTS (SELECT 1 FROM product_ratings WHERE product_id = OLD.product_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete product with existing ratings';
    END IF;
END$$
DELIMITER ;

-- Example insert statements
INSERT INTO products (product_name, product_description, product_type, price, discount)
VALUES 
('Levi\'s Jeans', 'Classic fit jeans', 'jeans', 49.99, 0.00),
('Silver Jewelry Set', 'Elegant jewelry set', 'jewelry_set', 99.99, 10.00),
('Kids T-Shirt', 'Comfortable kids t-shirt', 'kids_clothing', 9.99, 0.00);

INSERT INTO jeans (product_id, size, material, waist_size, inseam_length)
VALUES (1, '30x32', 'Cotton', 30, 32);

INSERT INTO jewelry_sets (product_id, set_type, metal_type, gemstone)
VALUES (2, 'Necklace and Earrings', 'Sterling Silver', 'Diamond');

INSERT INTO kids_clothing (product_id, size, age_group, material)
VALUES (3, 'Medium', 'toddler', 'Cotton');

INSERT INTO product_ratings (product_id, rating, review)
VALUES 
(1, 4, 'Great fit and quality'),
(2, 5, 'Beautiful jewelry set'),
(3, 3, 'Good quality but runs small');
```
