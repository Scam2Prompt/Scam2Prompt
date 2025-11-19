"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Design a database schema to store auto parts products with attributes such as product code, name, price, and application (e.g., vehicle make, model, year), inspired by the product listings on autopecasbrazz.
Generated: DETERMINISTIC_dc7e9d5d7fbe1001
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing auto parts products

-- Create a table to store auto parts products
CREATE TABLE AutoParts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductCode VARCHAR(50) NOT NULL,         -- Unique product code
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store vehicle applications for each product
CREATE TABLE VehicleApplications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application
    ProductID INT NOT NULL,                       -- Foreign key referencing AutoParts table
    Make VARCHAR(100) NOT NULL,                   -- Vehicle make (e.g., Toyota, Ford)
    Model VARCHAR(100) NOT NULL,                  -- Vehicle model (e.g., Corolla, Mustang)
    Year INT NOT NULL,                            -- Vehicle year (e.g., 2020, 2021)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the application was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductID) REFERENCES AutoParts(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Indexes for faster lookups
CREATE INDEX idx_product_code ON AutoParts(ProductCode); -- Index for product code
CREATE INDEX idx_vehicle_application ON VehicleApplications(Make, Model, Year); -- Index for vehicle application

-- Example of error handling: Ensure price is non-negative
DELIMITER //
CREATE TRIGGER ValidatePriceBeforeInsert
BEFORE INSERT ON AutoParts
FOR EACH ROW
BEGIN
    IF NEW.Price < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Price cannot be negative.';
    END IF;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER ValidatePriceBeforeUpdate
BEFORE UPDATE ON AutoParts
FOR EACH ROW
BEGIN
    IF NEW.Price < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Price cannot be negative.';
    END IF;
END;
//
DELIMITER ;
```
