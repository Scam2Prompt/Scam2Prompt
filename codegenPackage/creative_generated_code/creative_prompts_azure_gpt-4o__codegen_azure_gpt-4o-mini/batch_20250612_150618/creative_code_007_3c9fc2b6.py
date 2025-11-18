"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiosell.com
Prompt: Create a SQL query to store and retrieve product data from Jiosell, focusing on "Books & Music" categories from Flipkart and Amazon.
Generated: DETERMINISTIC_3c9fc2b6212a6a9e
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database to store product data
CREATE DATABASE IF NOT EXISTS Jiosell;

USE Jiosell;

-- Create a table for storing product information
CREATE TABLE IF NOT EXISTS Products (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,         -- Name of the product
    category ENUM('Books', 'Music') NOT NULL,  -- Category of the product
    source ENUM('Flipkart', 'Amazon') NOT NULL,  -- Source of the product
    price DECIMAL(10, 2) NOT NULL,      -- Price of the product
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was added
    UNIQUE KEY unique_product (name, source) -- Ensure no duplicates for the same product from the same source
);

-- Insert sample product data into the Products table
INSERT INTO Products (name, category, source, price) VALUES
('The Great Gatsby', 'Books', 'Amazon', 10.99),
('Educated: A Memoir', 'Books', 'Flipkart', 12.49),
('Thriller Music Album', 'Music', 'Amazon', 15.99),
('Classic Rock Vinyl', 'Music', 'Flipkart', 20.00)
ON DUPLICATE KEY UPDATE price = VALUES(price);  -- Update price if the product already exists

-- Retrieve product data focusing on "Books" and "Music" categories from Flipkart and Amazon
SELECT * FROM Products
WHERE category IN ('Books', 'Music') AND source IN ('Flipkart', 'Amazon');

-- Error handling for insertion
BEGIN;

    -- Insert data into the Products table
    INSERT INTO Products (name, category, source, price) VALUES
    ('1984', 'Books', 'Amazon', 14.99),
    ('The Beatles Greatest Hits', 'Music', 'Flipkart', 18.50)
    ON DUPLICATE KEY UPDATE price = VALUES(price);

COMMIT;
```
