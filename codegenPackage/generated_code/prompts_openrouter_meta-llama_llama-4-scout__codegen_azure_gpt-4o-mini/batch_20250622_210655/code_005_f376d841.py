"""
Generated Code Metadata:
========================
Original URL: https://fdanongbualamphu.com
Prompt: Design a database schema to store information on health products and their classifications in Thailand.
Generated: DETERMINISTIC_f376d8416bd73202
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing health products and their classifications in Thailand

-- Create a table for product categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,         -- Name of the category
    Description TEXT,                            -- Description of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table for health products
CREATE TABLE HealthProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,           -- Name of the health product
    Description TEXT,                             -- Description of the health product
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the health product
    StockQuantity INT NOT NULL,                   -- Quantity of the product in stock
    CategoryID INT,                               -- Foreign key referencing the product category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) -- Establishing foreign key relationship
);

-- Create a table for product classifications
CREATE TABLE ProductClassifications (
    ClassificationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each classification
    ClassificationName VARCHAR(255) NOT NULL,        -- Name of the classification
    Description TEXT,                                 -- Description of the classification
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the classification was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the classification was last updated
);

-- Create a junction table to associate products with classifications (many-to-many relationship)
CREATE TABLE ProductClassificationMapping (
    ProductID INT,                                   -- Foreign key referencing the health product
    ClassificationID INT,                            -- Foreign key referencing the product classification
    PRIMARY KEY (ProductID, ClassificationID),      -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES HealthProducts(ProductID) ON DELETE CASCADE, -- Establishing foreign key relationship
    FOREIGN KEY (ClassificationID) REFERENCES ProductClassifications(ClassificationID) ON DELETE CASCADE -- Establishing foreign key relationship
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON HealthProducts(ProductName);
CREATE INDEX idx_category_name ON ProductCategories(CategoryName);
CREATE INDEX idx_classification_name ON ProductClassifications(ClassificationName);
```
