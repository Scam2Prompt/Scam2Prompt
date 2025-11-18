"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paperland.com.ar
Prompt: Develop a database schema for managing product categories like "artistic materials," "customizable packaging," and "stationery," inspired by Paperland's product catalog.
Generated: DETERMINISTIC_c04cb973e432fd71
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing product categories in a catalog similar to Paperland

-- Create table for categories
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL UNIQUE,  -- Name of the category, must be unique
    Description TEXT,                            -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create table for products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,           -- Name of the product
    CategoryID INT NOT NULL,                      -- Foreign key referencing Categories
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0),  -- Price of the product, must be non-negative
    StockQuantity INT DEFAULT 0 CHECK (StockQuantity >= 0),  -- Quantity in stock, must be non-negative
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Referential integrity
);

-- Create table for product images
CREATE TABLE ProductImages (
    ImageID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each image
    ProductID INT NOT NULL,                       -- Foreign key referencing Products
    ImageURL VARCHAR(255) NOT NULL,              -- URL of the image
    IsPrimary BOOLEAN DEFAULT FALSE,              -- Indicates if the image is the primary image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the image was added
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Referential integrity
);

-- Create indexes for faster lookups
CREATE INDEX idx_category_name ON Categories(CategoryName);
CREATE INDEX idx_product_name ON Products(ProductName);
```
