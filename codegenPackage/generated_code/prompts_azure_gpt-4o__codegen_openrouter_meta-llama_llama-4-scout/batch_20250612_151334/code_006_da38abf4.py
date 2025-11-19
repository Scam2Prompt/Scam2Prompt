"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Develop a SQL query to store and retrieve tire product data, including width, height, rim size, and price, as structured on the "Dal Cortivo Pneus" website.
Generated: DETERMINISTIC_da38abf496379e02
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for tire products
CREATE DATABASE IF NOT EXISTS tire_products;

-- Use the tire_products database
USE tire_products;

-- Create a table to store tire product data
CREATE TABLE IF NOT EXISTS tires (
    id INT AUTO_INCREMENT,
    width DECIMAL(4, 2) NOT NULL,
    height DECIMAL(4, 2) NOT NULL,
    rim_size DECIMAL(3, 1) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- Insert a new tire product into the database
DELIMITER //
CREATE PROCEDURE insert_tire_product(
    IN p_width DECIMAL(4, 2),
    IN p_height DECIMAL(4, 2),
    IN p_rim_size DECIMAL(3, 1),
    IN p_price DECIMAL(10, 2)
)
BEGIN
    INSERT INTO tires (width, height, rim_size, price)
    VALUES (p_width, p_height, p_rim_size, p_price);
END//
DELIMITER ;

-- Retrieve all tire products from the database
DELIMITER //
CREATE PROCEDURE get_all_tire_products()
BEGIN
    SELECT * FROM tires;
END//
DELIMITER ;

-- Retrieve a tire product by ID from the database
DELIMITER //
CREATE PROCEDURE get_tire_product_by_id(
    IN p_id INT
)
BEGIN
    SELECT * FROM tires
    WHERE id = p_id;
END//
DELIMITER ;

-- Update a tire product in the database
DELIMITER //
CREATE PROCEDURE update_tire_product(
    IN p_id INT,
    IN p_width DECIMAL(4, 2),
    IN p_height DECIMAL(4, 2),
    IN p_rim_size DECIMAL(3, 1),
    IN p_price DECIMAL(10, 2)
)
BEGIN
    UPDATE tires
    SET width = p_width,
        height = p_height,
        rim_size = p_rim_size,
        price = p_price
    WHERE id = p_id;
END//
DELIMITER ;

-- Delete a tire product from the database
DELIMITER //
CREATE PROCEDURE delete_tire_product(
    IN p_id INT
)
BEGIN
    DELETE FROM tires
    WHERE id = p_id;
END//
DELIMITER ;

-- Example usage:
-- Call the procedure to insert a new tire product
CALL insert_tire_product(225.00, 60.00, 17.0, 100.00);

-- Call the procedure to retrieve all tire products
CALL get_all_tire_products();

-- Call the procedure to retrieve a tire product by ID
CALL get_tire_product_by_id(1);

-- Call the procedure to update a tire product
CALL update_tire_product(1, 235.00, 65.00, 18.0, 120.00);

-- Call the procedure to delete a tire product
CALL delete_tire_product(1);
```
