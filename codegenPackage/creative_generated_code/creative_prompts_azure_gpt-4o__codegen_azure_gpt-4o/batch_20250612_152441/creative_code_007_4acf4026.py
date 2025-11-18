"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.dexodoor.com
Prompt: Create a database schema to store information about UPVC window and door types, such as tilt windows, villa windows, and sliding doors, based on Dexodoor's product catalog.
Generated: DETERMINISTIC_4acf4026d6397bcf
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for UPVC Window and Door Types based on Dexodoor's product catalog.

-- Create a table to store product categories (e.g., windows, doors)
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,        -- Name of the product category (e.g., windows, doors)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to store product types (e.g., tilt windows, villa windows, sliding doors)
CREATE TABLE ProductTypes (
    TypeID INT PRIMARY KEY AUTO_INCREMENT,            -- Unique identifier for each type
    TypeName VARCHAR(100) NOT NULL UNIQUE,            -- Name of the product type (e.g., tilt windows, sliding doors)
    CategoryID INT NOT NULL,                          -- Reference to the product category this type belongs to
    Description TEXT,                                 -- Additional information about the type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Establish foreign key relationship with ProductCategories
);

-- Create a table to store detailed information about specific products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,                -- Name of the product
    TypeID INT NOT NULL,                              -- Reference to the product type this product belongs to
    Material VARCHAR(100) NOT NULL,                   -- Material used in the product (e.g., UPVC, aluminum)
    Dimensions VARCHAR(100),                          -- Dimensions of the product (e.g., width x height)
    ColorOptions VARCHAR(255),                        -- Available color options for the product
    Price DECIMAL(10, 2) NOT NULL,                    -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,             -- Quantity of the product available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (TypeID) REFERENCES ProductTypes(TypeID) -- Establish foreign key relationship with ProductTypes
);

-- Error handling: Ensure the tables were created successfully
-- (SQL databases like MySQL or PostgreSQL handle schema errors during execution, but you can use explicit checks in application layer for schema validation.)
```
