"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Create a database schema to store product information for AirstyleArt, including stencils, paints, accessories, and airbrush equipment.
Generated: DETERMINISTIC_b11bf9af71bde2be
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for storing product information for AirstyleArt

-- Create the main Products table to store general product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for the product
    Name VARCHAR(255) NOT NULL,                -- Name of the product
    Description TEXT,                          -- Detailed description of the product
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL,                -- Quantity available in stock
    CategoryID INT NOT NULL,                   -- Foreign key referencing product category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for the last update
);

-- Create the Categories table to store product categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the category
    Name VARCHAR(100) NOT NULL UNIQUE,         -- Name of the category (e.g., stencils, paints, accessories, airbrush equipment)
    Description TEXT                           -- Detailed description of the category
);

-- Create the Manufacturers table to store manufacturer information
CREATE TABLE Manufacturers (
    ManufacturerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the manufacturer
    Name VARCHAR(255) NOT NULL UNIQUE,             -- Name of the manufacturer
    ContactInfo TEXT,                               -- Contact information for the manufacturer
    Website VARCHAR(255)                           -- Website URL of the manufacturer
);

-- Create the ProductDetails table for storing additional product-specific metadata
CREATE TABLE ProductDetails (
    DetailID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for the detail record
    ProductID INT NOT NULL,                        -- Foreign key referencing Products table
    KeyName VARCHAR(100) NOT NULL,                 -- Name of the detail (e.g., color, material, dimensions)
    Value VARCHAR(255) NOT NULL,                   -- Value of the detail
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Create the ProductImages table for storing product images
CREATE TABLE ProductImages (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for the image
    ProductID INT NOT NULL,                        -- Foreign key referencing Products table
    ImageURL VARCHAR(255) NOT NULL,                -- URL of the product image
    AltText VARCHAR(255),                          -- Alternative text for accessibility
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Create constraints to associate products with their manufacturer
ALTER TABLE Products
ADD ManufacturerID INT,
ADD FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID) ON DELETE SET NULL;

-- Indexes for faster querying
CREATE INDEX idx_products_category ON Products(CategoryID); -- Index for products by category
CREATE INDEX idx_products_manufacturer ON Products(ManufacturerID); -- Index for products by manufacturer
CREATE INDEX idx_productdetails_product ON ProductDetails(ProductID); -- Index for product details mapping
CREATE INDEX idx_productimages_product ON ProductImages(ProductID); -- Index for product images mapping
```
