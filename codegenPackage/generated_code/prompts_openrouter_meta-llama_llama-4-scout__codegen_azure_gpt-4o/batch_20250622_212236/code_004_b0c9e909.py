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
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product (up to 10 digits, 2 decimal places)
    Description TEXT,                         -- Detailed description of the product
    CategoryID INT NOT NULL,                  -- Foreign key linking to the Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_category_name ON Categories(CategoryName); -- Index on category name for quick lookups
CREATE INDEX idx_product_name ON Products(ProductName);     -- Index on product name for quick lookups
CREATE INDEX idx_category_id ON Products(CategoryID);       -- Index on category ID for quick filtering

-- Example of error handling: Ensure the tables are created only if they don't already exist
-- (This is typically handled by the database management system or migration tools)
```
