"""
Generated Code Metadata:
========================
Original URL: https://brosbel.pe
Prompt: "Design a database schema to store information about various agricultural products, including fertilizers, bio stimulants, and their applications."
Generated: DETERMINISTIC_384e47212bd87e68
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about agricultural products

-- Create a table for product categories (e.g., Fertilizers, Bio Stimulants)
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table for agricultural products
CREATE TABLE AgriculturalProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(100) NOT NULL,         -- Name of the product
    CategoryID INT NOT NULL,                    -- Foreign key referencing ProductCategories
    Description TEXT,                           -- Description of the product
    ApplicationInstructions TEXT,               -- Instructions for application
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a table for product applications
CREATE TABLE ProductApplications (
    ApplicationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each application
    ProductID INT NOT NULL,                         -- Foreign key referencing AgriculturalProducts
    ApplicationDate DATE NOT NULL,                  -- Date of application
    Quantity DECIMAL(10, 2) NOT NULL,              -- Quantity of product used
    Notes TEXT,                                     -- Additional notes about the application
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the application record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (ProductID) REFERENCES AgriculturalProducts(ProductID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create an index on ProductName for faster searches
CREATE INDEX idx_product_name ON AgriculturalProducts(ProductName);

-- Create an index on ApplicationDate for faster queries on application records
CREATE INDEX idx_application_date ON ProductApplications(ApplicationDate);
```
