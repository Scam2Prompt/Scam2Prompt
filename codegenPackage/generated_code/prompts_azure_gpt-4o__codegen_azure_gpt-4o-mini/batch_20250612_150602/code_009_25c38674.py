"""
Generated Code Metadata:
========================
Original URL: https://plusmedica-shop.ch
Prompt: Create a database schema for storing product information, including categories like "Probepackungen," "Eisen," and "Haare, Haut & Nägel," as outlined on the PlusMedica Shop website.
Generated: DETERMINISTIC_25c386746fd1653e
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing product information for PlusMedica Shop

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL UNIQUE,  -- Name of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the category was last updated
);

-- Create a table for products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,  -- Name of the product
    Description TEXT,  -- Description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the product, must be non-negative
    StockQuantity INT NOT NULL CHECK (StockQuantity >= 0),  -- Quantity in stock, must be non-negative
    CategoryID INT,  -- Foreign key referencing the ProductCategories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE SET NULL  -- Ensures referential integrity
);

-- Insert initial categories into the ProductCategories table
INSERT INTO ProductCategories (CategoryName) VALUES
('Probepackungen'),
('Eisen'),
('Haare, Haut & Nägel');

-- Example of error handling for inserting a product
DELIMITER //

CREATE PROCEDURE AddProduct(
    IN p_ProductName VARCHAR(255),
    IN p_Description TEXT,
    IN p_Price DECIMAL(10, 2),
    IN p_StockQuantity INT,
    IN p_CategoryID INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Handle the error (e.g., log it, return a message, etc.)
        ROLLBACK;  -- Rollback any changes made during the transaction
        SELECT 'Error occurred while adding the product.' AS ErrorMessage;
    END;

    START TRANSACTION;  -- Start a transaction

    INSERT INTO Products (ProductName, Description, Price, StockQuantity, CategoryID)
    VALUES (p_ProductName, p_Description, p_Price, p_StockQuantity, p_CategoryID);

    COMMIT;  -- Commit the transaction if no errors occurred
END //

DELIMITER ;
```
