"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gvika.in
Prompt: Develop a database schema for storing product information, including categories like "Customized Gifts" and "Home Decor," inspired by Gvika's product organization.
Generated: DETERMINISTIC_8a85683dfa547b47
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing product information and categories

-- Create table to store categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., "Customized Gifts", "Home Decor")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Create table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    Description TEXT,                         -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product (up to 10 digits, 2 decimal places)
    Stock INT NOT NULL DEFAULT 0,             -- Quantity of the product in stock
    CategoryID INT,                           -- Foreign key referencing the Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL -- Handle category deletion gracefully
);

-- Create an index for faster lookup of products by category
CREATE INDEX idx_category_id ON Products(CategoryID);
```
