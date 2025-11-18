"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Write a database schema for storing product details, including categories, sizes, and warranty information, based on the diverse product offerings mentioned on the TDKCO website.
Generated: DETERMINISTIC_fa77c24f81ab91a6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing product details

-- Drop existing tables if they exist to start afresh
DROP TABLE IF EXISTS Warranty;
DROP TABLE IF EXISTS Size;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS Product;

-- Table for storing product categories
CREATE TABLE Category (
    category_id SERIAL PRIMARY KEY,         -- Unique identifier for each category
    name VARCHAR(100) NOT NULL UNIQUE,     -- Name of the category
    description TEXT                        -- Description of the category
);

-- Table for storing product sizes
CREATE TABLE Size (
    size_id SERIAL PRIMARY KEY,             -- Unique identifier for each size
    size_name VARCHAR(50) NOT NULL UNIQUE   -- Name of the size (e.g. S, M, L, XL)
);

-- Table for storing warranty information
CREATE TABLE Warranty (
    warranty_id SERIAL PRIMARY KEY,         -- Unique identifier for each warranty
    duration_months INT NOT NULL,           -- Duration of the warranty in months
    details TEXT                            -- Additional details about the warranty
);

-- Table for storing product details
CREATE TABLE Product (
    product_id SERIAL PRIMARY KEY,          -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,             -- Name of the product
    description TEXT,                        -- Description of the product
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),  -- Price of the product, must be non-negative
    category_id INT NOT NULL,                -- Foreign key referencing Category
    size_id INT NOT NULL,                    -- Foreign key referencing Size
    warranty_id INT,                         -- Foreign key referencing Warranty (nullable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the product was last updated
    FOREIGN KEY (category_id) REFERENCES Category(category_id) ON DELETE CASCADE, -- Referencing category
    FOREIGN KEY (size_id) REFERENCES Size(size_id) ON DELETE CASCADE, -- Referencing size
    FOREIGN KEY (warranty_id) REFERENCES Warranty(warranty_id) ON DELETE SET NULL -- Referencing warranty
);

-- Indexes for faster lookup
CREATE INDEX idx_product_name ON Product(name);
CREATE INDEX idx_category_name ON Category(name);
CREATE INDEX idx_size_name ON Size(size_name);
```
