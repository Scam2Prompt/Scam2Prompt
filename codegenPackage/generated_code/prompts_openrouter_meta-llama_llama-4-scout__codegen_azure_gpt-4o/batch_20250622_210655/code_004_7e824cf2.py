"""
Generated Code Metadata:
========================
Original URL: https://saldiana.com.br
Prompt: "Design a database schema to store information about Sal Diana's products, including product lines (e.g., Linha Diana, Linha Apolo), product descriptions, and pricing information."
Generated: DETERMINISTIC_7e824cf291f4a081
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Sal Diana's products

-- Create a table to store product lines
CREATE TABLE ProductLines (
    ProductLineID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product line
    Name VARCHAR(255) NOT NULL,                   -- Name of the product line (e.g., Linha Diana, Linha Apolo)
    Description TEXT                              -- Optional description of the product line
);

-- Create a table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each product
    ProductLineID INT NOT NULL,                   -- Foreign key referencing the ProductLines table
    Name VARCHAR(255) NOT NULL,                   -- Name of the product
    Description TEXT,                             -- Optional description of the product
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (ProductLineID) REFERENCES ProductLines(ProductLineID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store pricing history (optional, for tracking price changes)
CREATE TABLE PricingHistory (
    PricingHistoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each pricing record
    ProductID INT NOT NULL,                          -- Foreign key referencing the Products table
    OldPrice DECIMAL(10, 2) NOT NULL,                -- Previous price of the product
    NewPrice DECIMAL(10, 2) NOT NULL,                -- Updated price of the product
    ChangeDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the price change occurred
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_productline_name ON ProductLines(Name); -- Index for quick lookup of product lines by name
CREATE INDEX idx_product_name ON Products(Name);         -- Index for quick lookup of products by name
CREATE INDEX idx_product_price ON Products(Price);       -- Index for quick lookup of products by price
```
