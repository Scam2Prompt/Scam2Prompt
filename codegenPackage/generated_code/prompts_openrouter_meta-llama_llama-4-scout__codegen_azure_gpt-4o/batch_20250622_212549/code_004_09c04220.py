"""
Generated Code Metadata:
========================
Original URL: https://somoscorujasbraz.blogspot.com
Prompt: Design a database schema to store customer reviews and ratings for an e-commerce platform, like Somos Corujas, with fields for review text, rating (1-5), and product ID.
Generated: DETERMINISTIC_09c042205165a37c
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing customer reviews and ratings for an e-commerce platform

-- Table: Products
-- This table stores information about products.
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    ProductDescription TEXT,                  -- Description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp when the product was added
);

-- Table: Reviews
-- This table stores customer reviews and ratings for products.
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each review
    ProductID INT NOT NULL,                   -- Foreign key referencing the Products table
    ReviewText TEXT NOT NULL,                 -- Text of the customer review
    Rating TINYINT NOT NULL CHECK (Rating BETWEEN 1 AND 5), -- Rating (1-5)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
-- Index on ProductID in Reviews table for faster lookups
CREATE INDEX idx_reviews_productid ON Reviews(ProductID);

-- Example: Insert sample data into Products table
-- INSERT INTO Products (ProductName, ProductDescription) VALUES ('Sample Product', 'This is a sample product.');

-- Example: Insert sample data into Reviews table
-- INSERT INTO Reviews (ProductID, ReviewText, Rating) VALUES (1, 'Great product!', 5);
```
