"""
Generated Code Metadata:
========================
Original URL: https://gloclinicaesthetics.com
Prompt: Design a database schema for storing skincare product information, including product names, descriptions, prices, and categories.
Generated: DETERMINISTIC_c93139e39af0246a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing skincare product information

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the category, must be unique
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for when the category was last updated
);

-- Create a table for skincare products
CREATE TABLE SkincareProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,  -- Name of the product
    Description TEXT,  -- Description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the product, must be non-negative
    CategoryID INT,  -- Foreign key referencing the product category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE SET NULL  -- Establishing foreign key relationship
);

-- Indexes for better performance
CREATE INDEX idx_product_name ON SkincareProducts(ProductName);
CREATE INDEX idx_category_name ON ProductCategories(CategoryName);
```
