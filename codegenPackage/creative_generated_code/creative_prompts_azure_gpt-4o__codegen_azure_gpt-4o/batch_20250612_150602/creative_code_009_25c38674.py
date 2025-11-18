"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plusmedica-shop.ch
Prompt: Create a database schema for storing product information, including categories like "Probepackungen," "Eisen," and "Haare, Haut & Nägel," as outlined on the PlusMedica Shop website.
Generated: DETERMINISTIC_25c386746fd1653e
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Script to create a database schema for storing product information
-- The schema includes categories such as "Probepackungen," "Eisen," and "Haare, Haut & Nägel"

-- Create table for categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., "Probepackungen", "Eisen")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create table for products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    Description TEXT,                          -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Stock INT NOT NULL DEFAULT 0,              -- Quantity of the product in stock
    CategoryID INT,                            -- Foreign key linking to Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE SET NULL -- Ensure referential integrity
);

-- Create table for product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each image
    ProductID INT NOT NULL,                    -- Foreign key linking to Products table
    ImageURL VARCHAR(2083) NOT NULL,           -- URL of the product image
    IsPrimary BOOLEAN DEFAULT FALSE,           -- Flag indicating if it's the primary image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the image was added
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Insert predefined categories
INSERT INTO Categories (CategoryName) VALUES
('Probepackungen'), -- Sample packs
('Eisen'),          -- Iron supplements
('Haare, Haut & Nägel'); -- Hair, skin, and nails

-- Example error handling: Ensure necessary constraints
-- For safety, verify constraints programmatically in application code (if applicable)
-- For example: Ensure CategoryID exists before inserting into Products
```
