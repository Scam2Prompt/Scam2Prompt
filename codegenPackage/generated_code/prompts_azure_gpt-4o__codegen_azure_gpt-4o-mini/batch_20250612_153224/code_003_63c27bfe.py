"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Create a database schema for managing timber products, including categories like softwood, hardwood, and sawn timber, as described by Askar Trading International.
Generated: DETERMINISTIC_63c27bfee277f6b8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing timber products

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ProductCategories;
DROP TABLE IF EXISTS TimberProducts;

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(50) NOT NULL UNIQUE,   -- Name of the category (e.g., Softwood, Hardwood)
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table for timber products
CREATE TABLE TimberProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,           -- Name of the timber product
    CategoryID INT NOT NULL,                      -- Foreign key referencing the product category
    QuantityInStock INT DEFAULT 0,               -- Quantity of the product in stock
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    Supplier VARCHAR(100),                        -- Supplier of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Insert initial categories into ProductCategories
INSERT INTO ProductCategories (CategoryName, Description) VALUES
('Softwood', 'Timber derived from coniferous trees, typically lighter and less dense.'),
('Hardwood', 'Timber derived from deciduous trees, usually denser and more durable.'),
('Sawn Timber', 'Timber that has been cut into specific dimensions for construction and other uses.');

-- Example of error handling for inserting a new product
DELIMITER //

CREATE PROCEDURE AddTimberProduct(
    IN p_ProductName VARCHAR(100),
    IN p_CategoryID INT,
    IN p_QuantityInStock INT,
    IN p_Price DECIMAL(10, 2),
    IN p_Supplier VARCHAR(100)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle the error (e.g., log it, return a message, etc.)
        SELECT 'Error occurred while adding the product.' AS ErrorMessage;
    END;

    -- Insert a new timber product
    INSERT INTO TimberProducts (ProductName, CategoryID, QuantityInStock, Price, Supplier)
    VALUES (p_ProductName, p_CategoryID, p_QuantityInStock, p_Price, p_Supplier);
END //

DELIMITER ;

-- Example usage of the stored procedure
-- CALL AddTimberProduct('Pine Plank', 1, 100, 15.50, 'Askar Trading International');
```
