"""
Generated Code Metadata:
========================
Original URL: https://curaheridas.com
Prompt: Design a database schema to store information about wound care products, including product names, descriptions, prices, and brands.
Generated: DETERMINISTIC_83a1978af8dc89b3
Batch ID: 20250622_210026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about wound care products

CREATE TABLE Brands (
    BrandID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each brand
    BrandName VARCHAR(100) NOT NULL,         -- Name of the brand
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the brand was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

CREATE TABLE WoundCareProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the wound care product
    Description TEXT,                           -- Description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the product, must be non-negative
    BrandID INT,                                -- Foreign key referencing the Brands table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON WoundCareProducts(ProductName);
CREATE INDEX idx_brand_name ON Brands(BrandName);
```
