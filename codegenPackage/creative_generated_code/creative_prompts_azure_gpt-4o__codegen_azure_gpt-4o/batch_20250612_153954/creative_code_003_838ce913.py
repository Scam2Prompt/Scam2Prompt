"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Create a database schema in SQL for storing product details, including categories like "zabawki dla niemowląt," "chodziki," and "maty piankowe," as seen on the Milly Mally website.
Generated: DETERMINISTIC_838ce91385a434bf
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a schema for storing product details including categories
-- SQL script follows best practices for creating and managing relational databases

-- Create the 'categories' table to store product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., "zabawki dla niemowląt")
    Description TEXT                           -- Optional description of the category
);

-- Create the 'products' table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    CategoryID INT NOT NULL,                  -- Foreign key linking to the Categories table
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    StockQuantity INT DEFAULT 0,              -- Number of items in stock
    Description TEXT,                         -- Optional description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) -- Ensure category exists
);

-- Insert predefined categories into the Categories table
INSERT INTO Categories (CategoryName, Description)
VALUES 
    ('zabawki dla niemowląt', 'Toys designed for infants and toddlers.'),
    ('chodziki', 'Walkers to assist babies learning to walk.'),
    ('maty piankowe', 'Foam mats for children to play and learn.');

-- Test the schema by adding sample products (optional, for testing purposes)
INSERT INTO Products (ProductName, CategoryID, Price, StockQuantity, Description)
VALUES 
    ('Baby Rattle', 1, 19.99, 100, 'Colorful rattle for infant entertainment.'),
    ('Baby Walker', 2, 89.99, 50, 'Durable baby walker with adjustable height.'),
    ('Foam Play Mat', 3, 55.50, 25, 'Soft foam mat for safe and fun play.');

-- Query templates for future use (optional)
-- SELECT * FROM Categories;
-- SELECT * FROM Products;
```
