"""
Generated Code Metadata:
========================
Original URL: https://shopmetlife.pk
Prompt: Design a database schema to store product information, including product name, price, description, and category, for an e-commerce website like ShopMetlife that sells personal care products.
Generated: DETERMINISTIC_b0c9e909f4b94ebc
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing product information for an e-commerce website

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product, must be non-negative
    Description TEXT,                            -- Description of the product
    CategoryID INT,                              -- Foreign key referencing the ProductCategories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Establishing foreign key relationship
);

-- Index for faster search on product name
CREATE INDEX idx_product_name ON Products(ProductName);

-- Index for faster search on category
CREATE INDEX idx_category_id ON Products(CategoryID);
```
