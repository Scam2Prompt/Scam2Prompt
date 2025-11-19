"""
Generated Code Metadata:
========================
Original URL: https://pekana.pk
Prompt: Generate a database schema for storing homeopathic product details, including categories, product names (e.g., "PK 84 MUNDIPUR"), prices, and availability status, based on the structure of PEKANA.PK.
Generated: DETERMINISTIC_d5f63c215352ba39
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing homeopathic product details

-- Create a database for homeopathic products
CREATE DATABASE HomeopathicProducts;

-- Use the created database
USE HomeopathicProducts;

-- Table to store product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL UNIQUE,  -- Name of the category
    Description TEXT,                            -- Optional description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,           -- Name of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price of the product, must be non-negative
    AvailabilityStatus ENUM('In Stock', 'Out of Stock', 'Pre-Order') NOT NULL, -- Availability status of the product
    CategoryID INT,                               -- Foreign key referencing Categories
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL -- Foreign key constraint
);

-- Index for faster searching of products by name
CREATE INDEX idx_product_name ON Products(ProductName);

-- Sample data insertion for categories
INSERT INTO Categories (CategoryName, Description) VALUES
('Homeopathic Remedies', 'Various homeopathic remedies for different ailments.'),
('Homeopathic Kits', 'Kits containing multiple homeopathic products.'),
('Homeopathic Supplements', 'Supplements to support health and wellness.');

-- Sample data insertion for products
INSERT INTO Products (ProductName, Price, AvailabilityStatus, CategoryID) VALUES
('PK 84 MUNDIPUR', 15.99, 'In Stock', 1),
('PK 84 MUNDIPUR Kit', 49.99, 'Pre-Order', 2),
('Homeopathic Vitamin C', 12.50, 'Out of Stock', 3);
```
