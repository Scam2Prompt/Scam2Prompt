"""
Generated Code Metadata:
========================
Original URL: https://vividolev.com
Prompt: Design a simple database schema to store information about the various products offered by Vivid Olev, including their specifications and applications.
Generated: DETERMINISTIC_0b2a8994c61aa912
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing product information for Vivid Olev

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category
    Description TEXT                           -- Optional description of the category
);

-- Create a table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    CategoryID INT NOT NULL,                   -- Foreign key linking to ProductCategories
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    StockQuantity INT NOT NULL,                -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Enforce category relationship
);

-- Create a table to store product specifications
CREATE TABLE ProductSpecifications (
    SpecificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each specification
    ProductID INT NOT NULL,                         -- Foreign key linking to Products
    SpecificationName VARCHAR(255) NOT NULL,        -- Name of the specification (e.g., "Weight", "Color")
    SpecificationValue VARCHAR(255) NOT NULL,       -- Value of the specification (e.g., "2kg", "Red")
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Enforce product relationship
);

-- Create a table to store product applications
CREATE TABLE ProductApplications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application
    ProductID INT NOT NULL,                       -- Foreign key linking to Products
    ApplicationDescription TEXT NOT NULL,         -- Description of the application (e.g., "Used in industrial lighting")
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) -- Enforce product relationship
);

-- Example indexes for performance optimization
CREATE INDEX idx_product_category ON Products(CategoryID); -- Index for faster category lookups
CREATE INDEX idx_specification_product ON ProductSpecifications(ProductID); -- Index for faster specification lookups
CREATE INDEX idx_application_product ON ProductApplications(ProductID); -- Index for faster application lookups
```
