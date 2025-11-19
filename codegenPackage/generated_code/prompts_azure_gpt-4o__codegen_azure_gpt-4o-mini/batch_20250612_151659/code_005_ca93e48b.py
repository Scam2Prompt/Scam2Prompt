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
-- Create a database for Meta+ products
CREATE DATABASE MetaPlusProducts;

-- Use the created database
USE MetaPlusProducts;

-- Table for Stainless Steel products
CREATE TABLE StainlessSteel (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    stock_level INT NOT NULL CHECK (stock_level >= 0),
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    delivery_location VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for Aluminum products
CREATE TABLE Aluminum (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    stock_level INT NOT NULL CHECK (stock_level >= 0),
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    delivery_location VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for Copper products
CREATE TABLE Copper (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    stock_level INT NOT NULL CHECK (stock_level >= 0),
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    delivery_location VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table for Engineering Plastics products
CREATE TABLE EngineeringPlastics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    stock_level INT NOT NULL CHECK (stock_level >= 0),
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    delivery_location VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Function to add a new product to a specified table
DELIMITER //
CREATE PROCEDURE AddProduct(
    IN productType VARCHAR(50),
    IN productName VARCHAR(255),
    IN stockLevel INT,
    IN productPrice DECIMAL(10, 2),
    IN deliveryLocation VARCHAR(255)
)
BEGIN
    DECLARE tableName VARCHAR(50);
    
    -- Determine the table based on product type
    SET tableName = CASE productType
        WHEN 'StainlessSteel' THEN 'StainlessSteel'
        WHEN 'Aluminum' THEN 'Aluminum'
        WHEN 'Copper' THEN 'Copper'
        WHEN 'EngineeringPlastics' THEN 'EngineeringPlastics'
        ELSE SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Invalid product type';
    END CASE;

    -- Insert the new product into the determined table
    SET @sql = CONCAT('INSERT INTO ', tableName, ' (product_name, stock_level, price, delivery_location) VALUES (?, ?, ?, ?)');
    PREPARE stmt FROM @sql;
    SET @productName = productName;
    SET @stockLevel = stockLevel;
    SET @productPrice = productPrice;
    SET @deliveryLocation = deliveryLocation;
    EXECUTE stmt USING @productName, @stockLevel, @productPrice, @deliveryLocation;
    DEALLOCATE PREPARE stmt;
END //
DELIMITER ;

-- Example of how to call the AddProduct procedure
-- CALL AddProduct('StainlessSteel', 'SS Product 1', 100, 29.99, 'Location A');
```
