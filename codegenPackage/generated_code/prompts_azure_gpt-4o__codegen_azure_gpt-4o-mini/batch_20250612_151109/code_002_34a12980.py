"""
Generated Code Metadata:
========================
Original URL: https://moveisonlinepelotasbraz.blogspot.com
Prompt: Create a database schema in SQL to store furniture product information from "moveisonlinepelotasbraz," including columns for product name, price range, category (e.g., "Sala," "Quarto"), and availability.
Generated: DETERMINISTIC_34a129806760b415
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing furniture product information
CREATE DATABASE IF NOT EXISTS moveisonlinepelotasbraz;

-- Use the created database
USE moveisonlinepelotasbraz;

-- Create a table to store furniture products
CREATE TABLE IF NOT EXISTS furniture_products (
    product_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,        -- Name of the product
    price_range DECIMAL(10, 2) NOT NULL,       -- Price range of the product
    category ENUM('Sala', 'Quarto', 'Cozinha', 'Escritório', 'Jardim') NOT NULL, -- Category of the product
    availability BOOLEAN NOT NULL DEFAULT TRUE,  -- Availability status of the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the product was last updated
);

-- Add an index on the product_name for faster search queries
CREATE INDEX idx_product_name ON furniture_products(product_name);

-- Sample error handling for table creation
DELIMITER //
CREATE PROCEDURE create_furniture_table()
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle the error (e.g., log it, raise a custom error, etc.)
        SELECT 'An error occurred while creating the furniture_products table.';
    END;

    -- Attempt to create the table
    CREATE TABLE IF NOT EXISTS furniture_products (
        product_id INT AUTO_INCREMENT PRIMARY KEY,
        product_name VARCHAR(255) NOT NULL,
        price_range DECIMAL(10, 2) NOT NULL,
        category ENUM('Sala', 'Quarto', 'Cozinha', 'Escritório', 'Jardim') NOT NULL,
        availability BOOLEAN NOT NULL DEFAULT TRUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
END //
DELIMITER ;

-- Call the procedure to create the table
CALL create_furniture_table();
```
