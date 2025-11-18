"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Create a database schema to store information about Ecoplast and Casary products, including categories, model numbers, and design samples.
Generated: DETERMINISTIC_3eb1509ebd183533
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema to store information about Ecoplast and Casary products

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category
    Description TEXT                           -- Optional description of the category
);

-- Create a table to store products
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    CategoryID INT NOT NULL,                  -- Foreign key to ProductCategories table
    ModelNumber VARCHAR(255) NOT NULL,        -- Model number of the product
    Brand ENUM('Ecoplast', 'Casary') NOT NULL,-- Brand name (restricted to Ecoplast or Casary)
    DesignSample TEXT,                        -- Optional design sample description or link
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    -- Foreign key constraint to ensure valid CategoryID
    CONSTRAINT FK_Category FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Create an index to optimize queries on ModelNumber
CREATE INDEX IDX_ModelNumber ON Products(ModelNumber);

-- Create an index on CategoryID to speed up category-related queries
CREATE INDEX IDX_CategoryID ON Products(CategoryID);

-- Example: Insert sample categories (optional, for testing purposes)
INSERT INTO ProductCategories (CategoryName, Description)
VALUES 
    ('Plastic Containers', 'Durable and eco-friendly plastic containers'),
    ('Storage Boxes', 'High-quality storage solutions for various needs'),
    ('Design Accessories', 'Fashionable and functional accessories');

-- Example: Insert sample products (optional, for testing purposes)
INSERT INTO Products (ProductName, CategoryID, ModelNumber, Brand, DesignSample)
VALUES 
    ('EcoBox L', 1, 'EB-L123', 'Ecoplast', 'Modern design with a matte finish'),
    ('Casary Storage XL', 2, 'CS-XL456', 'Casary', 'Elegant design with reinforced edges'),
    ('EcoAccessory V1', 3, 'EA-V1', 'Ecoplast', 'Minimalist accessory for everyday use');
```
