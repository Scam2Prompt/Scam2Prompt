"""
Generated Code Metadata:
========================
Original URL: https://simbatools.com
Prompt: Design a database schema to store product information for an online store selling industrial supplies, including tables for products, prices, and customer reviews.
Generated: DETERMINISTIC_9f258d8f66b1aefb
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online store selling industrial supplies

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    Description TEXT,                           -- Detailed description of the product
    Category VARCHAR(100),                      -- Category of the product (e.g., tools, machinery)
    StockQuantity INT NOT NULL DEFAULT 0,      -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store pricing information for products
CREATE TABLE Prices (
    PriceID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each price entry
    ProductID INT NOT NULL,                     -- Foreign key referencing Products
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    Currency VARCHAR(10) NOT NULL DEFAULT 'USD', -- Currency of the price
    EffectiveDate DATE NOT NULL,                -- Date when the price becomes effective
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store customer reviews for products
CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each review
    ProductID INT NOT NULL,                      -- Foreign key referencing Products
    CustomerName VARCHAR(255) NOT NULL,         -- Name of the customer who wrote the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),  -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                            -- Text of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_product_category ON Products(Category);
CREATE INDEX idx_review_product ON Reviews(ProductID);
CREATE INDEX idx_price_product ON Prices(ProductID);
```
