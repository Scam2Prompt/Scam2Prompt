"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: Design a query to analyze the performance characteristics of Aprisacv's refractory products, including their temperature tolerances and application areas in furnaces.
Generated: DETERMINISTIC_76fc4c38776cb612
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for refractory products analysis
CREATE DATABASE refractory_products;

-- Use the refractory_products database
USE refractory_products;

-- Create a table for refractory products
CREATE TABLE refractory_products (
    id INT AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    temperature_tolerance DECIMAL(5, 2) NOT NULL,
    application_area VARCHAR(255) NOT NULL,
    furnace_type VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

-- Create a table for furnace types
CREATE TABLE furnace_types (
    id INT AUTO_INCREMENT,
    furnace_name VARCHAR(255) NOT NULL,
    description TEXT,
    PRIMARY KEY (id)
);

-- Create a table for product applications
CREATE TABLE product_applications (
    id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    furnace_type_id INT NOT NULL,
    application_area VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (product_id) REFERENCES refractory_products(id),
    FOREIGN KEY (furnace_type_id) REFERENCES furnace_types(id)
);

-- Insert sample data into refractory_products table
INSERT INTO refractory_products (product_name, temperature_tolerance, application_area, furnace_type)
VALUES 
('Aprisacv Refractory Brick', 1800.00, 'Furnace Lining', 'Steel Furnace'),
('Aprisacv Insulation Board', 1200.00, 'Furnace Roof', 'Ceramic Furnace'),
('Aprisacv Castable Refractory', 2000.00, 'Furnace Wall', 'Cement Kiln');

-- Insert sample data into furnace_types table
INSERT INTO furnace_types (furnace_name, description)
VALUES 
('Steel Furnace', 'Used for steel production'),
('Ceramic Furnace', 'Used for ceramic production'),
('Cement Kiln', 'Used for cement production');

-- Insert sample data into product_applications table
INSERT INTO product_applications (product_id, furnace_type_id, application_area)
VALUES 
(1, 1, 'Furnace Lining'),
(2, 2, 'Furnace Roof'),
(3, 3, 'Furnace Wall');

-- Query to analyze performance characteristics of Aprisacv's refractory products
SELECT 
    rp.product_name,
    rp.temperature_tolerance,
    pt.application_area,
    ft.furnace_name AS furnace_type
FROM 
    refractory_products rp
JOIN 
    product_applications pa ON rp.id = pa.product_id
JOIN 
    furnace_types ft ON pa.furnace_type_id = ft.id
WHERE 
    rp.product_name LIKE '%Aprisacv%';

-- Stored procedure to analyze performance characteristics
DELIMITER //
CREATE PROCEDURE analyze_refractory_products()
BEGIN
    SELECT 
        rp.product_name,
        rp.temperature_tolerance,
        pt.application_area,
        ft.furnace_name AS furnace_type
    FROM 
        refractory_products rp
    JOIN 
        product_applications pa ON rp.id = pa.product_id
    JOIN 
        furnace_types ft ON pa.furnace_type_id = ft.id
    WHERE 
        rp.product_name LIKE '%Aprisacv%';
END//
DELIMITER ;

-- Call the stored procedure
CALL analyze_refractory_products();
```
